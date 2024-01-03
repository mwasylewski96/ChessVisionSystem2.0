import flet as ft
from chessFletApp.config_app import get_view_config, get_view_3_config
from chessFletApp.chessGameFletApp.view import ViewApp


class View3(ViewApp, ft.UserControl):

    def __init__(
            self,
            page,
            loop,
            pause_process
    ):
        super().__init__()
        self.page = page
        self.loop = loop
        self.pause_process = pause_process
        self.black_time = get_view_3_config()["BUTTON_BLACK"]["TIME"]
        self.white_time = get_view_3_config()["BUTTON_WHITE"]["TIME"]

    # def get_view(
    #         self
    # ):
    #     return ft.View(
    #         route="/view3",
    #         controls=[
    #             self.get_main_container_stack()
    #         ]
    #     )

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

    def set_new_time(
            self,
            button_color,
            time
    ):
        if button_color == "black":
            self.black_time = time
        if button_color == "white":
            self.white_time = time

    def read_timers(
            self,
    ):
        return {
            "white_time": self.white_time,
            "black_time": self.black_time
        }

    def put_button_black(
            self
    ):
        main_config = get_view_config()["MAIN"]
        config = get_view_3_config()["BUTTON_BLACK"]
        return ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(
                                content=ft.Text(value=self.black_time, size=config["SIZE"]),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=config["RADIUS"]),
                                    bgcolor=config["BG_COLOR"],
                                    color=config["COLOR"]
                                )),
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
        return ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(
                                content=ft.Text(value=self.white_time, size=config["SIZE"]),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=config["RADIUS"]),
                                    bgcolor=config["BG_COLOR"],
                                    color=config["COLOR"]
                                )),
                        ]
                    )
                ]),
                bottom=config["BOTTOM"],
                width=main_config["WIDTH"],
                height=config["HEIGHT"],
                bgcolor=main_config["BG_COLOR"]
            )

    async def on_pause_game(self):
        await self.loop.create_task(self.pause_process(self.read_timers()))
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