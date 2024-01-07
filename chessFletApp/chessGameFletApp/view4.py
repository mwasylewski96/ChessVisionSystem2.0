import flet as ft
from config_app import get_view_config, get_view_4_config
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
        main_config = get_view_config()["MAIN"]
        config = get_view_4_config()["BUTTON_QUIT"]
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
        main_config = get_view_config()["MAIN"]
        config = get_view_4_config()["BUTTON_RESUME"]
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

    # def get_slider_value(self):
    #     return self.slider_end_game.value
    #
    # def put_slider_result_of_end_game(self):
    #     main_config = get_view_config()["MAIN"]
    #     config = get_view_4_config()["SLIDER_END_GAME"]
    #     self.slider_end_game = ft.Slider(
    #                         min=config["MIN"],
    #                         max=config["MAX"],
    #                         divisions=config["DIVISIONS"],
    #                         active_color=config["ACTIVE_COLOR"],
    #                         inactive_color=config["INACTIVE_COLOR"],
    #                         thumb_color=config["THUMB_COLOR"],
    #                         value=config["INIT_VALUE"],
    #                         width=config["SLIDER_WIDTH"],
    #                     )
    #     return ft.Container(
    #         ft.Column([
    #             ft.Row(
    #                 alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    #                 controls=[
    #                     self.slider_end_game
    #                 ]
    #             )
    #         ]),
    #         top=config["TOP"],
    #         width=main_config["WIDTH"],
    #         height=config["HEIGHT"],
    #         bgcolor=main_config["BG_COLOR"]
    #     )

    # @staticmethod
    # def put_white_draw_black_image():
    #     main_config = get_view_config()["MAIN"]
    #     config = get_view_4_config()["WHITE_DRAW_BLACK_IMAGE"]
    #     return ft.Container(
    #         ft.Column([
    #             ft.Row(
    #                 alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    #                 controls=[
    #                     ft.Image(
    #                         src=config["SRC_WHITE"],
    #                         width=config["SRC_WIDTH"],
    #                         height=config["SRC_HEIGHT"]
    #                     ),
    #                     ft.Image(
    #                         src=config["SRC_DRAW"],
    #                         width=config["SRC_WIDTH"],
    #                         height=config["SRC_HEIGHT"]
    #                     ),
    #                     ft.Image(
    #                         src=config["SRC_BLACK"],
    #                         width=config["SRC_WIDTH"],
    #                         height=config["SRC_HEIGHT"]
    #                     )
    #                 ]
    #             )
    #         ]),
    #         top=config["TOP"],
    #         width=main_config["WIDTH"],
    #         height=config["HEIGHT"],
    #         bgcolor=config["BG_COLOR"]
    #     )


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