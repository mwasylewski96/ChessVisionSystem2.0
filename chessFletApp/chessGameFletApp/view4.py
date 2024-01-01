import flet as ft
from chessFletApp.config_app import get_view_config, get_view_4_config
from chessFletApp.chessGameFletApp.view import ViewApp


class View4(ViewApp, ft.UserControl):

    def __init__(
            self,
            page
    ):
        super().__init__()
        self.page = page

    # def get_view(
    #         self
    # ):
    #     return ft.View(
    #         route="/view4",
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
                    self.put_text_chess_clock(),
                    self.put_button_end_game(),
                    self.put_buttons_back_start_new_game()
                ]
            )
        )

    @staticmethod
    def put_button_end_game():
        main_config = get_view_config()["MAIN"]
        config = get_view_4_config()["BUTTON_END_GAME"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Text(value=config["VALUE"], size=config["SIZE"]),
                            style=ft.ButtonStyle(
                                bgcolor=config["BG_COLOR"],
                                color=config["COLOR"]
                            )
                        ),
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    def put_buttons_back_start_new_game(self):
        main_config = get_view_config()["MAIN"]
        config_back = get_view_config()["BUTTON_BACK"]
        config = get_view_4_config()["BUTTONS_BACK_START_NEW_GAME"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Text(
                                value=config_back["VALUE"],
                                size=config["BUTTON_BACK"]["SIZE"]
                            ),
                            style=ft.ButtonStyle(
                                bgcolor=config["BUTTON_BACK"]["BG_COLOR"],
                                color=config["BUTTON_BACK"]["COLOR"]
                            ),
                            on_click=lambda _: self.page.go('/view3')
                        ),
                        ft.ElevatedButton(
                            content=ft.Text(
                                value=config["BUTTON_START_NEW_GAME"]["VALUE"],
                                size=config["BUTTON_START_NEW_GAME"]["SIZE"]
                            ),
                            style=ft.ButtonStyle(
                                bgcolor=config["BUTTON_START_NEW_GAME"]["BG_COLOR"],
                                color=config["BUTTON_START_NEW_GAME"]["COLOR"]
                            ),
                            on_click=lambda _: self.page.go('/view1')
                        ),
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )