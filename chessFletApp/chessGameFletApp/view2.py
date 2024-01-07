import flet as ft
import json
from config_app import get_mode_version, get_view_config, get_view_1_config, get_view_2_config
from view import ViewApp


class View2(ViewApp, ft.UserControl):

    def __init__(
            self,
            page,
            loop,
            start_chess_game,
            write_event_and_players_data_chess_game
    ):
        super().__init__()
        self.page = page
        self.loop = loop
        self.start_chess_game = start_chess_game
        self.write_event_and_players_data_chess_game = write_event_and_players_data_chess_game
        mode_version = get_mode_version()
        self.develop_mode = get_view_config()[mode_version]["MAIN"]["DEVELOP_MODE"]

    def build(
            self
    ):
        return ft.Container(
            ft.Stack(
                [
                    self.put_background_image(),
                    self.put_text_chess_clock(),
                    self.put_text_prepare_chessboard(),
                    self.put_button_start_game(),
                    self.put_button_back()
                ]
            )
        )

    @staticmethod
    def put_text_prepare_chessboard():
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_2_config()[mode_version]["TEXT_PREPARE_CHESSBOARD"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        ft.Text(
                            value=config["VALUE"],
                            size=config["SIZE"],
                            color=config["COLOR"],
                            italic=True,
                            weight=config["WEIGHT"]
                        )
                    ]
                )
            ]),
            alignment=ft.alignment.center,
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"],
            top=config["TOP"]
        )

    async def on_start_game(self):
        if not self.develop_mode:
            await self.loop.create_task(self.start_chess_game())
            await self.loop.create_task(
                self.write_event_and_players_data_chess_game(
                    self.read_event_and_players_data_chess_game()
                )
            )
        await self.page.go_async('/view3')

    @staticmethod
    def read_event_and_players_data_chess_game():
        mode_version = get_mode_version()
        config = get_view_1_config()[mode_version]
        with open(config["PATH"], "r") as file:
            data = json.load(file)
        return data

    def put_button_start_game(self):
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_2_config()[mode_version]["BUTTON_START_GAME"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Text(
                                value=config["VALUE"],
                                size=config["SIZE"]
                            ),
                            style=ft.ButtonStyle(
                                bgcolor=config["BG_COLOR"],
                                color=config["COLOR"]
                            ),
                            on_click=lambda _: self.loop.create_task(self.on_start_game())
                        )
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    def put_button_back(self):
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_config()[mode_version]["BUTTON_BACK"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Text(
                                value=config["VALUE"],
                                size=config["SIZE"]
                            ),
                            style=ft.ButtonStyle(
                                bgcolor=config["BG_COLOR"],
                                color=config["COLOR"]
                            ),
                            on_click=lambda _: self.loop.create_task(self.page.go_async('/view1'))
                        )
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            left=config["LEFT2"],
            bgcolor=main_config["BG_COLOR"]
        )