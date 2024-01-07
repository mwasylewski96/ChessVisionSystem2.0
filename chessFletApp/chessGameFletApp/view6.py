import flet as ft
import json
from config_app import get_view_config, get_view_1_config,\
    get_view_3_config, get_view_6_config
from view import ViewApp


class View6(ViewApp, ft.UserControl):

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
                    self.put_text_congratulations(),
                    self.put_button_menu()
                ]
            )
        )

    @staticmethod
    def put_text_congratulations():
        main_config = get_view_config()["MAIN"]
        config = get_view_6_config()["TEXT_CONGRATULATIONS"]
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

    async def on_button_menu(
            self
    ):
        self.write_init_clean_entries_to_json()
        self.write_init_clean_timers_to_json()
        self.write_init_clean_button_states_to_json()
        await self.loop.create_task(self.page.go_async('/view1'))

    def put_button_menu(
            self
    ):
        main_config = get_view_config()["MAIN"]
        config = get_view_6_config()["BUTTON_MENU"]
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
                            on_click=lambda _: self.loop.create_task(self.on_button_menu())
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
    def write_init_clean_button_states_to_json():
        config = get_view_3_config()
        data = {
            "white_state": False,
            "black_state": True,
        }
        with open(config["PATH"]["BUTTONS"], 'w') as json_file:
            json.dump(data, json_file)

    @staticmethod
    def write_init_clean_entries_to_json():
        config = get_view_1_config()
        data = {
            "white": "",
            "event": "",
            "black": ""
        }
        with open(config["PATH"], 'w') as json_file:
            json.dump(data, json_file)

    @staticmethod
    def write_init_clean_timers_to_json():
        config = get_view_3_config()
        data = {
            "white_time": config["BUTTON_WHITE"]["TIME"],
            "black_time": config["BUTTON_BLACK"]["TIME"]
        }
        with open(config["PATH"]["TIMERS"], 'w') as json_file:
            json.dump(data, json_file)

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