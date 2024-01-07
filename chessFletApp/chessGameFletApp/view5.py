import flet as ft
from config_app import get_mode_version, get_view_config, get_view_5_config
from view import ViewApp


class View5(ViewApp, ft.UserControl):

    def __init__(
            self,
            page,
            loop,
            end_chess_game
    ):
        super().__init__()
        self.page = page
        self.loop = loop
        mode_version = get_mode_version()
        self.develop_mode = get_view_config()[mode_version]["MAIN"]["DEVELOP_MODE"]
        self.end_chess_game = end_chess_game

        self.button_white_win = None
        self.button_draw = None
        self.button_black_win = None

    def build(
            self
    ):
        return ft.Container(
            ft.Stack(
                [
                    self.put_background_image(),
                    self.put_text_chess_clock(),
                    self.put_text_choose_winner(),
                    self.put_buttons_wins_white_draw_black(),
                    self.put_button_back()
                ]
            )
        )

    @staticmethod
    def put_text_choose_winner():
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_5_config()[mode_version]["TEXT_CHOOSE_WINNER"]
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

    async def on_button_white_win(
            self
    ):
        if not self.develop_mode:
            await self.loop.create_task(
                self.end_chess_game(
                    result="1-0"
                )
            )
        await self.page.go_async('/view6')

    async def on_button_draw(
            self
    ):
        if not self.develop_mode:
            await self.loop.create_task(
                self.end_chess_game(
                    result="1/2-1/2"
                )
            )
        await self.page.go_async('/view6')

    async def on_button_black_win(
            self
    ):
        if not self.develop_mode:
            await self.loop.create_task(
                self.end_chess_game(
                    result="0-1"
                )
            )
        await self.page.go_async('/view6')

    def put_buttons_wins_white_draw_black(
            self
    ):
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_5_config()[mode_version]["BUTTONS_WHITE_DRAW_BLACK"]

        self.button_white_win = ft.TextButton(
            width=config["WIDTH"],
            content=ft.Image(
                src=config["SRC_WHITE"],
                width=config["WIDTH"],
                height=config["HEIGHT"]
            ),
            on_click=lambda _: self.loop.create_task(self.on_button_white_win()),
        )
        self.button_draw = ft.TextButton(
            width=config["WIDTH"],
            content=ft.Image(
                src=config["SRC_DRAW"],
                width=config["WIDTH"],
                height=config["HEIGHT"]
            ),
            on_click=lambda _: self.loop.create_task(self.on_button_draw())
        )
        self.button_black_win = ft.TextButton(
            width=config["WIDTH"],
            content=ft.Image(
                expand=True,
                src=config["SRC_BLACK"],
                width=config["WIDTH"],
                height=config["HEIGHT"]
            ),
            on_click=lambda _: self.loop.create_task(self.on_button_black_win()),
        )

        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.button_white_win,
                        self.button_draw,
                        self.button_black_win
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    def put_button_back(
            self
    ):
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
                            on_click=lambda _: self.loop.create_task(self.page.go_async('/view4'))
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