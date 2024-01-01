import flet as ft
from chessFletApp.config_app import get_view_config, get_view_2_config
from chessFletApp.chessGameFletApp.view import ViewApp


class View2(ViewApp, ft.UserControl):

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
    #         route="/view2",
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
                    self.put_text_prepare_chessboard(),
                    self.put_button_start_game(),
                    self.put_button_back()
                ]
            )
        )

    @staticmethod
    def put_text_prepare_chessboard():
        main_config = get_view_config()["MAIN"]
        config = get_view_2_config()["TEXT_PREPARE_CHESSBOARD"]
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

    def put_button_start_game(self):
        main_config = get_view_config()["MAIN"]
        config = get_view_2_config()["BUTTON_START_GAME"]
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
                            ),
                            on_click=lambda _: self.page.go('/view3')
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
        main_config = get_view_config()["MAIN"]
        config = get_view_config()["BUTTON_BACK"]
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
                            on_click=lambda _: self.page.go('/view1')
                        ),
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            left=config["LEFT2"],
            bgcolor=main_config["BG_COLOR"]
        )