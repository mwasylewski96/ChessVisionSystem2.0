import asyncio
import json
from datetime import datetime, timedelta
import time
import flet as ft
from chessFletApp.config_app import get_view_config, get_view_3_config
from chessFletApp.chessGameFletApp.view import ViewApp
import threading
from typing import Literal


class View3(ViewApp, ft.UserControl):

    def __init__(
            self,
            page,
            loop,
            execute_procedure_of_move_white,
            execute_procedure_of_move_black,
    ):
        super().__init__()
        self.page = page
        self.loop = loop
        self.execute_procedure_of_move_white = execute_procedure_of_move_white
        self.execute_procedure_of_move_black = execute_procedure_of_move_black

        self.black_time = None
        self.white_time = None
        self.button_white = None
        self.button_black = None

        self.task_white = None
        self.task_black = None

        self.white_timer_thread = None
        self.white_timer_event = None

        self.black_timer_thread = None
        self.black_timer_event = None

        # self.setup_timers_threads()
        # self.run_timers_threads()

        # self.__run_thread_timer_white()
        # # self.__run_thread_timer_black()

        self.write_temp_data_to_timers()

    def write_temp_data_to_timers(
            self
    ):
        self.set_buttons_timers_values(
            self.read_temp_time_data_chess_game()
        )

    @staticmethod
    def read_temp_time_data_chess_game():
        config = get_view_3_config()
        with open(config["PATH"], "r") as file:
            data = json.load(file)
        return data

    def set_buttons_timers_values(
            self,
            data
    ):
        self.set_new_init_time("white", data["white_time"])
        self.set_new_init_time("black", data["black_time"])

    def set_new_init_time(
            self,
            button_color,
            time
    ):
        print("in set time: ", time)

        if time["MIN"] <= 9:
            __min = f"0{time['MIN']}"
        else:
            __min = f"{time['MIN']}"

        if time["SEC"] <= 9:
            __sec = f"0{time['SEC']}"
        else:
            __sec = f"{time['SEC']}"

        __set_time = f"{__min}:{__sec}"

        if button_color == "black":
            self.black_time = __set_time

        if button_color == "white":
            self.white_time = __set_time

    def set_new_time(
            self,
            button_color,
            time
    ):
        print("in set time: ", time)

        if time["MIN"] <= 9:
            __min = f"0{time['MIN']}"
        else:
            __min = f"{time['MIN']}"

        if time["SEC"] <= 9:
            __sec = f"0{time['SEC']}"
        else:
            __sec = f"{time['SEC']}"

        __set_time = f"{__min}:{__sec}"

        if button_color == "black":
            self.button_black.value = __set_time
            self.black_time = {
                "black_time": {
                    "MIN": time["MIN"],
                    "SEC": time["SEC"]
                }
            }
            print(self.black_time)

        if button_color == "white":
            self.button_white.value = __set_time
            self.white_time = {
                "white_time": {
                    "MIN": time["MIN"],
                    "SEC": time["SEC"]
                }
            }
            print(self.white_time)

    def read_timer(
            self,
            color: Literal['white', "black"]
    ):
        if color == "white":
            return {
                "white_time": datetime.strptime(self.button_white.value, "%M:%S")
            }
        if color == "black":
            return {
                "black_time": datetime.strptime(self.button_black.value, "%M:%S")
            }

    def update_time(
            self,
            color: Literal['white', "black"]
    ):
        if color == "white":
            time = self.read_timer(
                color="white"
            )["white_time"]
        if color == "black":
            time = self.read_timer(
                color="black"
            )["black_time"]

        new_time = time - timedelta(seconds=1)

        return {
            "MIN": new_time.minute,
            "SEC": new_time.second
        }

    async def run_white_task(self):
        self.task_white = asyncio.create_task(self.__run_thread_timer_white())

    async def run_black_task(self):
        self.task_black = asyncio.create_task(self.__run_thread_timer_black())

    async def __run_thread_timer_white(
            self
    ):
        while self.white_timer_event:
            await asyncio.sleep(1)
            if self.white_timer_event:
                new_time = self.update_time(
                    color="black"
                )
                self.set_new_time(
                    button_color="black",
                    time=new_time
                )
            await self.update_async()

    async def __run_thread_timer_black(
            self
    ):
        while self.black_timer_event:
            await asyncio.sleep(1)
            if self.black_timer_event:
                new_time = self.update_time(
                    color="white"
                )
                self.set_new_time(
                    button_color="white",
                    time=new_time
                )
            await self.update_async()

    async def on_button_white(self):
        print("in button white")
        self.white_timer_event = True
        self.black_timer_event = False
        await self.run_white_task()
        # code with emitting move black to server

    async def on_button_black(self):
        print("in button black")
        self.white_timer_event = False
        self.black_timer_event = True
        await self.run_black_task()
        # code with emitting move black to server

    @staticmethod
    async def pause_game(
            state_of_timers
    ):
        config = get_view_3_config()
        with open(config["PATH"], 'w') as json_file:
            json.dump(state_of_timers, json_file)

    def build(
            self
    ):
        return ft.Container(
            ft.Stack(
                [
                    self.put_background_image(),
                    self.put_button_pause(),
                    self.put_button_black(),
                    self.put_button_white()
                ]
            )
        )

    def put_button_black(
            self
    ):
        main_config = get_view_config()["MAIN"]
        config = get_view_3_config()["BUTTON_BLACK"]
        self.button_black = ft.Text(
            value=self.black_time,
            size=config["SIZE"]
        )
        return ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(
                                content=self.button_black,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(
                                        radius=config["RADIUS"]
                                    ),
                                    bgcolor=config["BG_COLOR"],
                                    color=config["COLOR"]
                                ),
                                on_click=lambda _: self.loop.create_task(self.on_button_black())
                            )
                        ]
                    )
                ]),
                rotate=config["ROTATE"],
                top=config["TOP"],
                width=main_config["WIDTH"],
                height=config["HEIGHT"],
                bgcolor=main_config["BG_COLOR"]
            )

    def put_button_white(
            self
    ):
        main_config = get_view_config()["MAIN"]
        config = get_view_3_config()["BUTTON_WHITE"]
        self.button_white = ft.Text(
            value=self.white_time,
            size=config["SIZE"]
        )
        return ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(
                                content=self.button_white,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(
                                        radius=config["RADIUS"]
                                    ),
                                    bgcolor=config["BG_COLOR"],
                                    color=config["COLOR"]
                                ),
                                on_click=lambda _: self.loop.create_task(self.on_button_white())
                            ),
                        ]
                    )
                ]),
                bottom=config["BOTTOM"],
                width=main_config["WIDTH"],
                height=config["HEIGHT"],
                bgcolor=main_config["BG_COLOR"]
            )

    async def on_pause_game(
            self
    ):
        self.black_timer_event = False
        self.white_timer_event = False
        await asyncio.sleep(0.5)
        print(f"AAAAA {self.white_time}")
        print(f"BBBBB {self.black_time}")
        await self.pause_game({
            **self.white_time,
            **self.black_time
        })
        # self.write_temp_data_to_timers()
        await self.page.go_async('/view4')

    def put_button_pause(self):
        main_config = get_view_config()["MAIN"]
        config = get_view_3_config()["BUTTON_PAUSE"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.IconButton(
                            icon=config["ICON"],
                            icon_color=config["COLOR"],
                            icon_size=config["SIZE"],
                            on_click=lambda _: self.loop.create_task(self.on_pause_game())
                        ),
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )