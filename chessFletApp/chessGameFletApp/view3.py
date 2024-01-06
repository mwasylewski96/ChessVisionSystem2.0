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
        self.develop_mode = get_view_config()["MAIN"]["DEVELOP_MODE"]

        self.execute_procedure_of_move_white = execute_procedure_of_move_white
        self.execute_procedure_of_move_black = execute_procedure_of_move_black

        self.black_time_to_save_in_json = None
        self.white_time_to_save_in_json = None
        self.black_time_to_show_on_button = None
        self.white_time_to_show_on_button = None

        self.button_white_control_text = None  # has attribute value which is a text to show ??
        self.button_black_control_text = None  # has attribute value which is a text to show ??
        self.button_black = None
        self.button_white = None

        self.asyncio_task_white = None
        self.asyncio_task_black = None

        self.asyncio_task_white_event = asyncio.Event()
        self.asyncio_task_black_event = asyncio.Event()

        self.button_white_state = None
        self.button_black_state = None
        self.set_current_state_on_button_to_show_it()
        self.write_current_time_on_button_timers_to_show_it()

    async def did_mount_async(self):
        config = get_view_3_config()
        min_black = config["BUTTON_BLACK"]["TIME"]["MIN"]
        sec_black = config["BUTTON_BLACK"]["TIME"]["SEC"]
        min_white = config["BUTTON_WHITE"]["TIME"]["MIN"]
        sec_white = config["BUTTON_WHITE"]["TIME"]["SEC"]
        init_open = self.black_time_to_save_in_json["MIN"] == min_black and \
            self.black_time_to_save_in_json["SEC"] == sec_black and \
            self.white_time_to_save_in_json["MIN"] == min_white and \
            self.white_time_to_save_in_json["SEC"] == sec_white
        print("STATE OF INIT OPEN: ", init_open)
        if not init_open:
            if self.button_white_state:
                self.asyncio_task_black_event.clear()
                self.asyncio_task_white_event.set()
                await self.run_white_asyncio_task()
            if self.button_black_state:
                self.asyncio_task_white_event.clear()
                self.asyncio_task_black_event.set()
                await self.run_black_asyncio_task()

    def set_current_state_on_button_to_show_it(
            self
    ):
        self.set_buttons_states_to_show_it(
            self.read_current_states_saved_in_json()
        )

    @staticmethod
    def read_current_states_saved_in_json():
        config = get_view_3_config()
        with open(config["PATH"]["BUTTONS"], "r") as file:
            data = json.load(file)
        return data

    def set_buttons_states_to_show_it(
            self,
            states
    ):
        self.button_white_state = states["white_state"]
        self.button_black_state = states["black_state"]

    def write_current_time_on_button_timers_to_show_it(
            self
    ):
        self.set_buttons_timers_texts_to_show_current_time(
            self.read_current_time_saved_in_json()
        )

    @staticmethod
    def read_current_time_saved_in_json():
        config = get_view_3_config()
        with open(config["PATH"]["TIMERS"], "r") as file:
            data = json.load(file)
        return data

    def set_buttons_timers_texts_to_show_current_time(
            self,
            data
    ):
        self.set_new_current_time_to_show_on_button_and_to_save_in_json(
            color="white",
            time=data["white_time"]
        )
        self.set_new_current_time_to_show_on_button_and_to_save_in_json(
            color="black",
            time=data["black_time"]
        )

    def set_new_current_time_to_show_on_button_and_to_save_in_json(
            self,
            color,
            time
    ):
        print(color, " in set time: ", time)

        if time["MIN"] <= 9:
            __min = f"0{time['MIN']}"
        else:
            __min = f"{time['MIN']}"

        if time["SEC"] <= 9:
            __sec = f"0{time['SEC']}"
        else:
            __sec = f"{time['SEC']}"

        __set_time = f"{__min}:{__sec}"

        if color == "black":
            self.black_time_to_save_in_json = time
            self.black_time_to_show_on_button = __set_time

        if color == "white":
            self.white_time_to_save_in_json = time
            self.white_time_to_show_on_button = __set_time

    async def update_time(
            self,
            color: Literal['white', "black"]
    ):
        if color == "white":
            time = self.white_time_to_save_in_json
        if color == "black":
            time = self.black_time_to_save_in_json

        if time["SEC"] == 0:
            time["MIN"] -= 1
            time["SEC"] = 59
        else:
            time["SEC"] -= 1

        self.set_new_current_time_to_show_on_button_and_to_save_in_json(
            color=color,
            time=time
        )

    async def run_white_asyncio_task(self):
        self.asyncio_task_white = asyncio.create_task(self.__run_asyncio_task_white())

    async def run_black_asyncio_task(self):
        self.asyncio_task_black = asyncio.create_task(self.__run_asyncio_task_black())

    async def __run_asyncio_task_white(
            self
    ):
        while self.asyncio_task_white_event.is_set():
            await asyncio.sleep(1)
            if self.asyncio_task_white_event.is_set():
                await self.update_time(
                    color="black"
                )
                self.button_black_control_text.value = self.black_time_to_show_on_button
            try:
                await self.update_async()
            except AssertionError:
                pass  # TODO This error does not play a role but explain in future.

    async def __run_asyncio_task_black(
            self
    ):
        while self.asyncio_task_black_event.is_set():
            await asyncio.sleep(1)
            if self.asyncio_task_black_event.is_set():
                await self.update_time(
                    color="white"
                )
                self.button_white_control_text.value = self.white_time_to_show_on_button
            try:
                await self.update_async()
            except AssertionError:
                pass  # TODO This error does not play a role but explain in future.

    async def on_button_white(self):
        print("in button white")
        self.button_white.disabled = True
        await self.update_async()
        self.asyncio_task_black_event.clear()
        self.asyncio_task_white_event.set()
        self.button_black.disabled = False
        if not self.develop_mode:
            await self.loop.create_task(self.execute_procedure_of_move_white())
        await self.run_white_asyncio_task()
        # code with emitting move black to server

    async def on_button_black(self):
        print("in button black")
        self.button_black.disabled = True
        await self.update_async()
        self.asyncio_task_white_event.clear()
        self.asyncio_task_black_event.set()
        self.button_white.disabled = False
        if not self.develop_mode:
            await self.loop.create_task(self.execute_procedure_of_move_black())
        await self.run_black_asyncio_task()
        self.asyncio_task_black = None
        # code with emitting move black to server

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
        self.button_black_control_text = ft.Text(
            value=self.black_time_to_show_on_button,
            size=config["SIZE"]
        )
        self.button_black = ft.ElevatedButton(
            disabled=self.button_black_state,
            width=config["WIDTH"],
            content=self.button_black_control_text,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(
                    radius=config["RADIUS"]
                ),
                bgcolor={
                    ft.MaterialState.DISABLED: config["BG_COLOR"]["DISABLED"],
                    ft.MaterialState.DEFAULT: config["BG_COLOR"]["DEFAULT"]
                },
                color={
                    ft.MaterialState.DISABLED: config["COLOR"]["DISABLED"],
                    ft.MaterialState.DEFAULT: config["COLOR"]["DEFAULT"]
                }
            ),
            on_click=lambda _: self.loop.create_task(self.on_button_black())
        )
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.button_black
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
        self.button_white_control_text = ft.Text(
            value=self.white_time_to_show_on_button,
            size=config["SIZE"]
        )
        self.button_white = ft.ElevatedButton(
            disabled=self.button_white_state,
            width=config["WIDTH"],
            content=self.button_white_control_text,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(
                    radius=config["RADIUS"]
                ),
                bgcolor={
                    ft.MaterialState.DISABLED: config["BG_COLOR"]["DISABLED"],
                    ft.MaterialState.DEFAULT: config["BG_COLOR"]["DEFAULT"]
                },
                color={
                    ft.MaterialState.DISABLED: config["COLOR"]["DISABLED"],
                    ft.MaterialState.DEFAULT: config["COLOR"]["DEFAULT"]
                }
            ),
            on_click=lambda _: self.loop.create_task(self.on_button_white())
        )
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.button_white
                    ]
                )
            ]),
            bottom=config["BOTTOM"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    @staticmethod
    async def save_current_time_and_state_to_json(
            state_of_timers,
            states_of_buttons
    ):
        config = get_view_3_config()
        with open(config["PATH"]["TIMERS"], 'w') as json_file:
            json.dump(state_of_timers, json_file)
        with open(config["PATH"]["BUTTONS"], 'w') as json_file:
            json.dump(states_of_buttons, json_file)

    async def on_pause_game(
            self
    ):
        white_button_state = self.button_white.disabled
        black_button_state = self.button_black.disabled
        self.button_white.disabled = True
        self.button_black.disabled = True
        await self.update_async()
        self.asyncio_task_white_event.clear()
        self.asyncio_task_black_event.clear()
        print(f"WHITE STATE to save: {white_button_state}")
        print(f"BLACK STATE to save: {black_button_state}")
        print(f"WHITE TIME to save: {self.white_time_to_save_in_json}")
        print(f"BLACK TIME to save: {self.black_time_to_save_in_json}")
        current_states_of_timer_to_save_to_json = {
            "white_time": self.white_time_to_save_in_json,
            "black_time": self.black_time_to_save_in_json,
        }
        current_states_of_buttons_to_save_to_json = {
            "white_state": white_button_state,
            "black_state": black_button_state
        }
        await self.save_current_time_and_state_to_json(
            state_of_timers=current_states_of_timer_to_save_to_json,
            states_of_buttons=current_states_of_buttons_to_save_to_json
        )
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