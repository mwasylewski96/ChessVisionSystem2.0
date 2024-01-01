import flet as ft
from chessFletApp.config_app import get_view_config, get_view_4_config
from chessFletApp.chessGameFletApp.view import ViewApp

width = 411
height = 700
bg_col = "transparent"

top_chess_clock = 40
top_button_end_game = 300
top_buttons = 630

body = ft.Container(
    ft.Stack(
        [
            ft.Image(
                src="assets/background.png",
                width=width,
                height=height
            ),
            ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Text(
                                "CHESS CLOCK",
                                size=50,
                                color=ft.colors.WHITE,
                                italic=True,
                                weight=ft.FontWeight.W_500
                            )
                        ]
                    )
                ]),
                alignment=ft.alignment.center,
                width=width,
                height=100,
                bgcolor=bg_col,
                top=top_chess_clock
            ),
            ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(
                                content=ft.Text(value="END GAME", size=30),
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.DEEP_PURPLE_200,
                                    color=ft.colors.WHITE
                                )),
                        ]
                    )
                ]),
                top=top_button_end_game,
                width=width,
                height=50,
                bgcolor=bg_col
            ),
            ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(
                                content=ft.Text(value="BACK", size=30),
                                style=ft.ButtonStyle(
                                bgcolor=ft.colors.DEEP_PURPLE_200,
                                color=ft.colors.WHITE
                            )),
                            ft.ElevatedButton(
                                content=ft.Text(value="START NEW GAME", size=25),
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.DEEP_PURPLE_200,
                                    color=ft.colors.WHITE
                                )),
                        ]
                    )
                ]),
                top=top_buttons,
                width=width,
                height=50,
                bgcolor=bg_col
            )
        ]
    )
)


class View4(ViewApp):

    def get_view(
            self
    ):
        return ft.View(
            route="/view4",
            controls=[
                self.get_main_container_stack()
            ]
        )

    def get_main_container_stack(
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

    @staticmethod
    def put_buttons_back_start_new_game():
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
                            )
                        ),
                        ft.ElevatedButton(
                            content=ft.Text(
                                value=config["BUTTON_START_NEW_GAME"]["VALUE"],
                                size=config["BUTTON_START_NEW_GAME"]["SIZE"]
                            ),
                            style=ft.ButtonStyle(
                                bgcolor=config["BUTTON_START_NEW_GAME"]["BG_COLOR"],
                                color=config["BUTTON_START_NEW_GAME"]["COLOR"]
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


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = "Chess Clock"

    view = View4()
    main_cnt = view.get_main_container_stack()
    # vieww = view.get_view()
    # page.views.clear()
    # page.views.append(
    #     view
    # )
    page.add(
        main_cnt
    )


ft.app(target=main)