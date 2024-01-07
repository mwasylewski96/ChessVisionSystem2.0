import flet as ft
from config_app import get_mode_version, get_view_config, get_view_1_config
from view import ViewApp
import json


class View1(ViewApp, ft.UserControl):

    def __init__(
            self,
            page,
            loop
    ):
        super().__init__()
        self.page = page
        self.loop = loop
        self.entry_white = None
        self.entry_black = None
        self.entry_event = None
        self.entry_white_value = None
        self.entry_event_value = None
        self.entry_black_value = None
        self.set_last_saved_temp_data_to_entries()

    def build(
            self
    ):
        return ft.Container(
            ft.Stack(
                [
                    self.put_background_image(),
                    self.put_text_chess_clock(),
                    self.put_texts_white_black(),
                    self.put_text_event(),
                    self.put_entries_white_black(),
                    self.put_entry_event(),
                    self.put_button_next()
                ]
            )
        )

    def set_last_saved_temp_data_to_entries(
            self
    ):
        self.set_entries_values(
            self.read_event_and_players_data_chess_game()
        )

    @staticmethod
    def read_event_and_players_data_chess_game():
        mode_version = get_mode_version()
        config = get_view_1_config()[mode_version]
        with open(config["PATH"], "r") as file:
            data = json.load(file)
        return data

    def set_entries_values(
            self,
            data
    ):
        self.entry_white_value = data["white"]
        self.entry_event_value = data["event"]
        self.entry_black_value = data["black"]

    async def on_button_next(
            self
    ):
        self.write_entries_to_json(
            self.get_entries_values()
        )
        await self.loop.create_task(self.page.go_async('/view2'))

    def get_entries_values(
            self
    ):
        self.entry_white_value = self.entry_white.value
        self.entry_event_value = self.entry_event.value
        self.entry_black_value = self.entry_black.value
        return {
            "white": self.entry_white_value,
            "event": self.entry_event_value,
            "black": self.entry_black_value,
        }

    @staticmethod
    def write_entries_to_json(
            data
    ):
        mode_version = get_mode_version()
        config = get_view_1_config()[mode_version]
        with open(config["PATH"], 'w') as json_file:
            json.dump(data, json_file)

    def put_button_next(
            self
    ):
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_1_config()[mode_version]["BUTTON_NEXT"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
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
                            on_click=lambda _: self.loop.create_task(
                               self.on_button_next()
                            )
                        ),
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            right=config["RIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    @staticmethod
    def put_texts_white_black():
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_1_config()[mode_version]["TEXTS_WHITE_BLACK"]
        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        ft.Text(
                            value=config["VALUE_WHITE"],
                            size=config["SIZE"],
                            color=config["COLOR"],
                            italic=True,
                            weight=config["WEIGHT"]
                        ),
                        ft.Text(
                            value=config["VALUE_BLACK"],
                            size=config["SIZE"],
                            color=config["COLOR"],
                            italic=True,
                            weight=config["WEIGHT"]
                        )
                    ]
                ),
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    @staticmethod
    def put_text_event():
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_1_config()[mode_version]["TEXT_EVENT"]
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
                            weight=config["WEIGHT"],
                        ),
                    ]
                ),
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    def put_entries_white_black(
            self
    ):
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_1_config()[mode_version]["ENTRIES_WHITE_BLACK"]

        self.entry_white = ft.TextField(
            value=self.entry_white_value,
            color=config["COLOR"],
            width=config["WIDTH"],
            bgcolor=config["BG_COLOR"],
            hint_text=config["HINT_WHITE"]
        )
        self.entry_black = ft.TextField(
            value=self.entry_black_value,
            color=config["COLOR"],
            width=config["WIDTH"],
            bgcolor=config["BG_COLOR"],
            hint_text=config["HINT_BLACK"]
        )

        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.entry_white,
                        self.entry_black,
                    ]
                )
            ]),
            top=config["TOP"],
            width=main_config["WIDTH"],
            height=config["HEIGHT"],
            bgcolor=main_config["BG_COLOR"]
        )

    def put_entry_event(
            self
    ):
        mode_version = get_mode_version()
        main_config = get_view_config()[mode_version]["MAIN"]
        config = get_view_1_config()[mode_version]["ENTRY_EVENT"]

        self.entry_event = ft.TextField(
            value=self.entry_event_value,
            color=config["COLOR"],
            width=config["WIDTH"],
            bgcolor=config["BG_COLOR"],
            hint_text=config["HINT"]
        )

        return ft.Container(
            ft.Column([
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        self.entry_event,
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
#         View1(page=page)
#     )
#
#
# if __name__ == "__main__":
#     ft.app(target=main)