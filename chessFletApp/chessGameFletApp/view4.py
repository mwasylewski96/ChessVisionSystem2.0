import flet as ft
from config_app import get_mode_version, get_view_config, get_view_4_config
from view import ViewApp


class View4(ViewApp, ft.UserControl):

    def __init__(
            self,
            page,
            loop
    ):
        super().__init__()
        self.page = page
        self.loop = loop

    def build(
            self
    ):
        return ft.Container(
            ft.Stack(
                [
                    self.put_background_image(),
                    self.put_text_chess_clock(),
                    self.put_button_resume(),
                    self.put_button_quit()
                ]
            )
        )

    def put_button_quit(
            self
    ):
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_4_config()[mode_version]["BUTTON_QUIT"]
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
                            on_click=lambda _: self.loop.create_task(self.page.go_async('/view5'))
                        ),
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    def put_button_resume(
            self
    ):
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_4_config()[mode_version]["BUTTON_RESUME"]
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
                            on_click=lambda _: self.loop.create_task(self.page.go_async('/view3'))
                        )
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

# def main(page: ft.Page):
#     page.window_width = 450
#     page.window_height = 770
#
#     page.add(
#         View4(page=page)
#     )
#
#
# if __name__ == "__main__":
#     ft.app(target=main)