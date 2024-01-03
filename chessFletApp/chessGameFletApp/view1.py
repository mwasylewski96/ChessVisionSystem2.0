import flet as ft
from chessFletApp.config_app import get_view_config, get_view_1_config
from chessFletApp.chessGameFletApp.view import ViewApp


class View1(ViewApp, ft.UserControl):

    def __init__(
            self,
            page,
            loop
    ):
        super().__init__()
        self.page = page
        self.loop = loop
        self.entry_white_value = None
        self.entry_event_value = None
        self.entry_black_value = None

    # def get_view(
    #         self
    # ):
    #     return ft.View(
    #         route="/view1",
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
                    self.put_texts_white_event_black(),
                    self.put_entries_white_event_black(),
                    self.put_buttons_apply_next()
                ]
            )
        )

    def put_buttons_apply_next(
            self
    ):
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
                            )
                            # on_click=lambda _: self.page.go('/view2')
                        ),
                        ft.ElevatedButton(
                            content=ft.Text(value=config_next["VALUE"], size=config_next["SIZE"]),
                            style=ft.ButtonStyle(
                                bgcolor=config_next["BG_COLOR"],
                                color=config_next["COLOR"]
                            ),
                            on_click=lambda _: self.loop.create_task(self.page.go_async('/view2'))
                        ),
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