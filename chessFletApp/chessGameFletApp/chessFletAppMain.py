import asyncio
import json

import flet as ft
import socketio
from views import view_handler


class ChessFletApp:

    def __init__(
            self
    ):
        print("Initializing GUI client...")

        self.sio = socketio.AsyncClient()
        self.chess_game_namespace = "/chess_game"
        self.loop = asyncio.get_event_loop()

        @self.sio.on('connect', namespace=self.chess_game_namespace)
        async def on_chess_game_namespace_connect():
            print(f"Connected to chess server `{self.chess_game_namespace}` namespace")

        @self.sio.on(f'start_chess_game_chess_flet_app_response', namespace=self.chess_game_namespace)
        async def on_start_chess_game_chess_flet_app_response(response):
            print(f"Received: {response} on `{self.chess_game_namespace}` namespace.")

        @self.sio.on('write_event_and_players_data_chess_game_local_gui_response', namespace=self.chess_game_namespace)
        async def on_write_event_and_players_data_chess_game_chess_flet_app_response(response):
            print(f"Received: {response} on {self.chess_game_namespace} namespace.")

        @self.sio.on('execute_procedure_of_move_chess_flet_app_response', namespace=self.chess_game_namespace)
        async def on_execute_procedure_of_move_chess_flet_app_response(response):
            print(f"Received: {response} on {self.chess_game_namespace} namespace.")

        @self.sio.on('end_chess_game_chess_flet_app_response', namespace=self.chess_game_namespace)
        async def on_end_chess_game_chess_flet_app_response(response):
            print(f"Received: {response} on {self.chess_game_namespace} namespace.")

        self.loop.run_until_complete(self.start_server())

    async def start_server(self):
        print("Starting server...")
        # await self.sio.connect(
        #     "http://127.0.0.1:8080",
        #     namespaces=[self.chess_game_namespace]
        # )

    async def start_chess_game(
            self
    ):
        print(f"Emitting `start_chess_game` on namespace: `{self.chess_game_namespace}`")
        # await self.sio.emit(
        #     "start_chess_game",
        #     namespace=self.chess_game_namespace
        # )
        print("STARTED GAME")

    @staticmethod
    def read_event_and_players_data_chess_game():
        with open("event_and_players_data_chess_game.json", "r") as file:
            data = json.load(file)
        return data

    async def write_event_and_players_data_chess_game(
            self
    ):
        data = self.read_event_and_players_data_chess_game()
        data_to_send = {
            "event": data["event"],
            "white_player": data["white"],
            "black_player": data["black"]
        }
        print(f"Emitting `write_event_and_players_data_chess_game` on namespace: `{self.chess_game_namespace}`")
        await self.sio.emit(
            "write_event_and_players_data_chess_game",
            data=data_to_send,
            namespace=self.chess_game_namespace
        )

    async def execute_procedure_of_move_white(
            self
    ):
        data_to_send = {
            "color": "white"
        }
        print(f"Emitting `execute_procedure_of_move` on namespace: `{self.chess_game_namespace}`")
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
        await self.sio.emit(
            "execute_procedure_of_move",
            data=data_to_send,
            namespace=self.chess_game_namespace
        )

    async def pause_game(
            self,
            state_of_timers
    ):
        with open("state_of_timers.json", 'w') as json_file:
            json.dump(state_of_timers, json_file)

    async def end_chess_game(
            self,
            result
    ):
        data_to_send = {
            "result_of_game": result
        }
        print(f"Emitting `end_chess_game` on namespace: `{self.chess_game_namespace}`")
        # await self.sio.emit(
        #     "end_chess_game",
        #     data=data_to_send,
        #     namespace=self.chess_game_namespace
        # )
        print(f"SEND {data_to_send}")

    async def main(self, page: ft.Page):
        page.window_width = 450
        page.window_height = 770

        async def route_change(route):
            print(type(page.route))

            page.views.clear()
            page.views.append(
                view_handler(
                    page=page,
                    loop=self.loop,
                    start_game_process=self.start_chess_game,
                    pause_process=self.pause_game,
                    end_game_process=self.end_chess_game
                )[page.route]
            )
        page.on_route_change = route_change
        await page.go_async("/view1")


if __name__ == "__main__":
    flt_app = ChessFletApp()
    ft.app(target=flt_app.main)