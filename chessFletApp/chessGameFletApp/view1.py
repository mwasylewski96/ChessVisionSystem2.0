import flet as ft
from chessFletApp.config_app import get_view_config, get_view_1_config
from chessFletApp.chessGameFletApp.view import ViewApp

# width = 411
# height = 700
# bg_col = "transparent"
#
# top_chess_clock = 40
# top_white_event_black = 500
# top_entries = 550
# top_buttons = 630
#
# body = ft.Container(
#     ft.Stack(
#         [
#             ft.Image(
#                 src="assets/background.png",
#                 width=width,
#                 height=height
#             ),
#             ft.Container(
#                 ft.Column([
#                     ft.Row(
#                         alignment=ft.MainAxisAlignment.SPACE_EVENLY,
#                         controls=[
#                             ft.Text(
#                                 "CHESS CLOCK",
#                                 size=50,
#                                 color=ft.colors.WHITE,
#                                 italic=True,
#                                 weight=ft.FontWeight.W_500
#                             )
#                         ]
#                     )
#                 ]),
#                 alignment=ft.alignment.center,
#                 width=width,
#                 height=100,
#                 bgcolor=bg_col,
#                 top=top_chess_clock
#             ),
#             ft.Container(
#                 ft.Column([
#                     ft.Row(
#                         alignment=ft.MainAxisAlignment.SPACE_EVENLY,
#                         controls=[
#                             ft.Text("WHITE", size=30, color=ft.colors.WHITE, italic=True, weight=ft.FontWeight.W_500),
#                             ft.Text("EVENT", size=30, color=ft.colors.WHITE, italic=True, weight=ft.FontWeight.W_500),
#                             ft.Text("BLACK", size=30, color=ft.colors.WHITE, italic=True, weight=ft.FontWeight.W_500),
#                         ]
#                     ),
#                 ]),
#                 top=top_white_event_black,
#                 width=width,
#                 height=50,
#                 bgcolor=bg_col
#             ),
#             ft.Container(
#                 ft.Column([
#                     ft.Row(
#                         alignment=ft.MainAxisAlignment.SPACE_EVENLY,
#                         controls=[
#                             ft.TextField(color=ft.colors.WHITE, width=120, bgcolor=ft.colors.DEEP_PURPLE_200),
#                             ft.TextField(color=ft.colors.WHITE, width=120, bgcolor=ft.colors.DEEP_PURPLE_200),
#                             ft.TextField(color=ft.colors.WHITE, width=120, bgcolor=ft.colors.DEEP_PURPLE_200),
#                         ]
#                     )
#                 ]),
#                 top=top_entries,
#                 width=width,
#                 height=50,
#                 bgcolor=bg_col
#             ),
#             ft.Container(
#                 ft.Column([
#                     ft.Row(
#                         alignment=ft.MainAxisAlignment.SPACE_EVENLY,
#                         controls=[
#                             ft.ElevatedButton(
#                                 content=ft.Text(value="APPLY", size=30),
#                                 style=ft.ButtonStyle(
#                                 bgcolor=ft.colors.DEEP_PURPLE_200,
#                                 color=ft.colors.WHITE
#                             )),
#                             ft.ElevatedButton(
#                                 content=ft.Text(value="NEXT", size=30),
#                                 style=ft.ButtonStyle(
#                                     bgcolor=ft.colors.DEEP_PURPLE_200,
#                                     color=ft.colors.WHITE
#                                 )),
#                         ]
#                     )
#                 ]),
#                 top=top_buttons,
#                 width=width,
#                 height=50,
#                 bgcolor=bg_col
#             )
#         ]
#     )
# )


class View1(ViewApp):

    def __init__(
            self
    ):
        self.entry_white_value = None
        self.entry_event_value = None
        self.entry_black_value = None

    def get_view(
            self
    ):
        return ft.View(
            route="/view1",
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
                    self.put_texts_white_event_black(),
                    self.put_entries_white_event_black(),
                    self.put_buttons_apply_next()
                ]
            )
        )

    @staticmethod
    def put_buttons_apply_next():
        main_config = get_view_config()["MAIN"]
        config_apply_next = get_view_1_config()["BUTTONS_APPLY_NEXT"]
        config_apply = config_apply_next["BUTTON_APPLY"]
        config_next = config_apply_next["BUTTON_NEXT"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Text(value=config_apply["VALUE"], size=config_apply["SIZE"]),
                            style=ft.ButtonStyle(
                                bgcolor=config_apply["BG_COLOR"],
                                color=config_apply["COLOR"]
                            )),
                        ft.ElevatedButton(
                            content=ft.Text(value=config_next["VALUE"], size=config_next["SIZE"]),
                            style=ft.ButtonStyle(
                                bgcolor=config_next["BG_COLOR"],
                                color=config_next["COLOR"]
                            )),
                    ]
                )
            ]),
            top=config_apply_next["TOP"],
            width=main_config["WIDTH"],
            height=config_apply_next["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    @staticmethod
    def put_texts_white_event_black():
        main_config = get_view_config()["MAIN"]
        config = get_view_1_config()["TEXTS_WHITE_EVENT_BLACK"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        ft.Text(value=config["VALUE_WHITE"], size=config["SIZE"], color=config["COLOR"], italic=True, weight=config["WEIGHT"]),
                        ft.Text(value=config["VALUE_EVENT"], size=config["SIZE"], color=config["COLOR"], italic=True, weight=config["WEIGHT"]),
                        ft.Text(value=config["VALUE_BLACK"], size=config["SIZE"], color=config["COLOR"], italic=True, weight=config["WEIGHT"])
                    ]
                ),
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    def get_entries_values(
            self
    ):
        self.entry_white_value = self.entry_white.value
        self.entry_event_value = self.entry_event.value
        self.entry_black_value = self.entry_black.value

    def put_entries_white_event_black(
            self
    ):
        main_config = get_view_config()["MAIN"]
        config = get_view_1_config()["ENTRIES_WHITE_EVENT_BLACK"]

        self.entry_white = ft.TextField(
            color=config["COLOR"], width=config["WIDTH"], bgcolor=config["BG_COLOR"]
        )
        self.entry_event = ft.TextField(
            color=config["COLOR"], width=config["WIDTH"], bgcolor=config["BG_COLOR"]
        )
        self.entry_black = ft.TextField(
            color=config["COLOR"], width=config["WIDTH"], bgcolor=config["BG_COLOR"]
        )

        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.entry_white,
                        self.entry_event,
                        self.entry_black,
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

    view = View1()
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