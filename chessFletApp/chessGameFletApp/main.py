import asyncio
import json
import flet as ft
import socketio
from views import view_handler
from config_app import get_mode_version, get_view_config, get_view_1_config, get_view_3_config


class ChessFletApp:

    def __init__(
            self
    ):
        print("Initializing Chess Flet App client...")

        self.sio = socketio.AsyncClient()
        self.chess_game_namespace = "/chess_game"
        self.loop = asyncio.get_event_loop()
        self.mode_version = get_mode_version()
        self.config = get_view_config()[f'{self.mode_version}']["MAIN"]
        self.develop_mode = self.config["DEVELOP_MODE"]

        @self.sio.on('connect', namespace=self.chess_game_namespace)
        async def on_chess_game_namespace_connect():
            print(f"Connected to chess server `{self.chess_game_namespace}` namespace")

        @self.sio.on(f'start_chess_game_chess_flet_app_response', namespace=self.chess_game_namespace)
        async def on_start_chess_game_chess_flet_app_response(response):
            print(f"Received: {response} on `{self.chess_game_namespace}` namespace.")
            if response["success"]:
                print("STARTED GAME")

        @self.sio.on('write_event_and_players_data_chess_game_local_gui_response', namespace=self.chess_game_namespace)
        async def on_write_event_and_players_data_chess_game_chess_flet_app_response(response):
            print(f"Received: {response} on {self.chess_game_namespace} namespace.")
            if response["success"]:
                print("DATA SAVED IN GAME")

        @self.sio.on('execute_procedure_of_move_chess_flet_app_response', namespace=self.chess_game_namespace)
        async def on_execute_procedure_of_move_chess_flet_app_response(response):
            print(f"Received: {response} on {self.chess_game_namespace} namespace.")

        @self.sio.on('end_chess_game_chess_flet_app_response', namespace=self.chess_game_namespace)
        async def on_end_chess_game_chess_flet_app_response(response):
            print(f"Received: {response} on {self.chess_game_namespace} namespace.")

        self.write_init_clean_button_states_to_json()
        self.write_init_clean_entries_to_json()
        self.write_init_clean_timers_to_json()
        self.loop.run_until_complete(self.start_server())

    def write_init_clean_button_states_to_json(
            self
    ):
        config = get_view_3_config()[f'{self.mode_version}']
        data = {
            "white_state": False,
            "black_state": True,
        }
        with open(config["PATH"]["BUTTONS"], 'w') as json_file:
            json.dump(data, json_file)

    def write_init_clean_entries_to_json(
            self
    ):
        config = get_view_1_config()[f'{self.mode_version}']
        data = {
            "white": "",
            "event": "",
            "black": ""
        }
        with open(config["PATH"], 'w') as json_file:
            json.dump(data, json_file)

    def write_init_clean_timers_to_json(
            self
    ):
        config = get_view_3_config()[f'{self.mode_version}']
        data = {
            "white_time": config["BUTTON_WHITE"]["TIME"],
            "black_time": config["BUTTON_BLACK"]["TIME"]
        }
        with open(config["PATH"]["TIMERS"], 'w') as json_file:
            json.dump(data, json_file)

    async def start_server(
            self
    ):
        print("Starting server...")
        if not self.develop_mode:
            await self.sio.connect(
                "http://192.168.0.106:8080",
                namespaces=[self.chess_game_namespace]
            )

    async def start_chess_game(
            self
    ):
        print(f"Emitting `start_chess_game` on namespace: `{self.chess_game_namespace}`")
        if not self.develop_mode:
            await self.sio.emit(
                "start_chess_game",
                namespace=self.chess_game_namespace
            )

    async def write_event_and_players_data_chess_game(
            self,
            data
    ):
        data_to_send = {
            "event": data["event"],
            "white_player": data["white"],
            "black_player": data["black"]
        }
        print(f"Emitting `write_event_and_players_data_chess_game` on namespace: `{self.chess_game_namespace}`")
        if not self.develop_mode:
            await self.sio.emit(
                "write_event_and_players_data_chess_game",
                data=data_to_send,
                namespace=self.chess_game_namespace
            )
        print(f"SENDING: {data_to_send}")

    async def execute_procedure_of_move_white(
            self
    ):
        data_to_send = {
            "color": "white"
        }
        print(f"Emitting `execute_procedure_of_move` on namespace: `{self.chess_game_namespace}`")
        if not self.develop_mode:
            await self.sio.emit(
                "execute_procedure_of_move",
                data=data_to_send,
                namespace=self.chess_game_namespace
            )

    async def execute_procedure_of_move_black(
            self
    ):
        data_to_send = {
            "color": "black"
        }
        print(f"Emitting `execute_procedure_of_move` on namespace: `{self.chess_game_namespace}`")
        if not self.develop_mode:
            await self.sio.emit(
                "execute_procedure_of_move",
                data=data_to_send,
                namespace=self.chess_game_namespace
            )

    async def end_chess_game(
            self,
            result
    ):
        data_to_send = {
            "result_of_game": result
        }
        print(f"Emitting `end_chess_game` on namespace: `{self.chess_game_namespace}`")
        if not self.develop_mode:
            await self.sio.emit(
                "end_chess_game",
                data=data_to_send,
                namespace=self.chess_game_namespace
            )
        print(f"SEND {data_to_send}")

    async def main(
            self,
            page: ft.Page
    ):
        page.title = self.config["PAGE_TITLE"]
        page.window_width = 450
        page.window_height = 770

        async def route_change(route):
            page.views.clear()
            page.views.append(
                view_handler(
                    page=page,
                    loop=self.loop,
                    start_chess_game=self.start_chess_game,
                    write_event_and_players_data_chess_game=self.write_event_and_players_data_chess_game,
                    execute_procedure_of_move_white=self.execute_procedure_of_move_white,
                    execute_procedure_of_move_black=self.execute_procedure_of_move_black,
                    end_chess_game=self.end_chess_game
                )
            )
        page.on_route_change = route_change
        await page.go_async("/view1")


# if __name__ == "__main__":
flt_app = ChessFletApp()
ft.app(target=flt_app.main)