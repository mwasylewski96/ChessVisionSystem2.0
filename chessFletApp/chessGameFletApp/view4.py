import flet as ft
from chessFletApp.config_app import get_view_config, get_view_4_config
from chessFletApp.chessGameFletApp.view import ViewApp


class View4(ViewApp, ft.UserControl):

    def __init__(
            self,
            page,
            loop,
            end_chess_game
    ):
        super().__init__()
        self.page = page
        self.loop = loop
        self.end_chess_game = end_chess_game
        self.slider_end_game = None

    def build(
            self
    ):
        return ft.Container(
            ft.Stack(
                [
                    self.put_background_image(),
                    self.put_text_chess_clock(),
                    self.put_button_end_game(),
                    self.put_buttons_back_start_new_game(),
                    self.put_slider_result_of_end_game(),
                    self.put_white_draw_black_image()
                ]
            )
        )

    def put_button_end_game(self):
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
                            ),
                            on_click=lambda: self.loop.create_task(self.on_end_game_event())
                        ),
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    async def on_end_game_event(self):
        await self.end_chess_game(self.get_slider_value())

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
                            on_click=lambda _: self.loop.create_task(self.page.go_async('/view3'))
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

    def get_slider_value(self):
        return self.slider_end_game.value

    def put_slider_result_of_end_game(self):
        main_config = get_view_config()["MAIN"]
        config = get_view_4_config()["SLIDER_END_GAME"]
        self.slider_end_game = ft.Slider(
                            min=config["MIN"],
                            max=config["MAX"],
                            divisions=config["DIVISIONS"],
                            active_color=config["ACTIVE_COLOR"],
                            inactive_color=config["INACTIVE_COLOR"],
                            thumb_color=config["THUMB_COLOR"],
                            value=config["INIT_VALUE"],
                            width=config["SLIDER_WIDTH"],
                        )
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.slider_end_game
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    @staticmethod
    def put_white_draw_black_image():
        main_config = get_view_config()["MAIN"]
        config = get_view_4_config()["WHITE_DRAW_BLACK_IMAGE"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        ft.Image(
                            src=config["SRC_WHITE"],
                            width=config["SRC_WIDTH"],
                            height=config["SRC_HEIGHT"]
                        ),
                        ft.Image(
                            src=config["SRC_DRAW"],
                            width=config["SRC_WIDTH"],
                            height=config["SRC_HEIGHT"]
                        ),
                        ft.Image(
                            src=config["SRC_BLACK"],
                            width=config["SRC_WIDTH"],
                            height=config["SRC_HEIGHT"]
                        )
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=config["BG_COLOR"]
            # bgcolor=main_config["BG_COLOR"]
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