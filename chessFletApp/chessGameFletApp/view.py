from config_app import get_view_config
import flet as ft


class ViewApp:

    @staticmethod
    def put_background_image():
        main_config = get_view_config()["MAIN"]
        return ft.Image(
                src=main_config["IMG_SRC"],
                width=main_config["WIDTH"],
                height=main_config["HEIGHT"]
            )

    @staticmethod
    def put_text_chess_clock():
        config = get_view_config()
        return ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Text(
                                value=config["TEXT_CHESS_CLOCK"]["VALUE"],
                                size=config["TEXT_CHESS_CLOCK"]["SIZE"],
                                color=config["TEXT_CHESS_CLOCK"]["COLOR"],
                                italic=True,
                                weight=config["TEXT_CHESS_CLOCK"]["WEIGHT"]
                            )
                        ]
                    )
                ]),
                alignment=ft.alignment.center,
                width=config["MAIN"]["WIDTH"],
                height=config["TEXT_CHESS_CLOCK"]["HEIGHT"],
                bgcolor=config["MAIN"]["BG_COLOR"],
                top=config["TEXT_CHESS_CLOCK"]["TOP"]
            )