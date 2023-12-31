########################
#  EXTERNAL LIBRARIES  #
########################
import asyncio
import customtkinter
import socketio


class GUIClient:

    def __init__(
            self
    ):
        print("Initializing GUI client...")

        self.sio = socketio.AsyncClient()
        self.chess_game_namespace = "/chess_game"

        @self.sio.on('connect', namespace=self.chess_game_namespace)
        async def on_chess_game_namespace_connect():
            print(f"Connected to chess server `{self.chess_game_namespace}` namespace")

        @self.sio.on(f'start_chess_game_local_gui_response', namespace=self.chess_game_namespace)
        async def on_start_chess_game_local_gui_response(response):
            print(f"Received: {response} on `{self.chess_game_namespace}` namespace.")

        @self.sio.on('write_event_and_players_data_chess_game_local_gui_response', namespace=self.chess_game_namespace)
        async def on_write_event_and_players_data_chess_game_local_gui_response(response):
            print(f"Received: {response} on {self.chess_game_namespace} namespace.")

        @self.sio.on('execute_procedure_of_move_local_gui_response', namespace=self.chess_game_namespace)
        async def on_execute_procedure_of_move_local_gui_response(response):
            print(f"Received: {response} on {self.chess_game_namespace} namespace.")

        @self.sio.on('end_chess_game_local_gui_response', namespace=self.chess_game_namespace)
        async def on_end_chess_game_local_gui_response(response):
            print(f"Received: {response} on {self.chess_game_namespace} namespace.")

        self.loop = asyncio.get_event_loop()
        self.window = self.GUIWindow(
            event_loop=self.loop,
            on_start_chess_game=self.start_chess_game,
            on_write_event_and_players_data_chess_game=self.write_event_and_players_data_chess_game,
            on_execute_procedure_of_move_white=self.execute_procedure_of_move_white,
            on_execute_procedure_of_move_black=self.execute_procedure_of_move_black,
            on_end_chess_game=self.end_chess_game
        )

        self.loop.run_until_complete(self.start_server())

    async def start_server(self):
        print("Starting server...")
        await self.sio.connect(
            "http://127.0.0.1:8080",
            namespaces=[self.chess_game_namespace]
        )
        await self.window.show()

    async def start_chess_game(
            self
    ):
        print(f"Emitting `start_chess_game` on namespace: `{self.chess_game_namespace}`")
        await self.sio.emit(
            "start_chess_game",
            namespace=self.chess_game_namespace
        )

    async def write_event_and_players_data_chess_game(
            self
    ):
        data_to_send = {
            "event": "Friendly",
            "white_player": "Player 1",
            "black_player": "Player 2"
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

    async def end_chess_game(
            self
    ):
        data_to_send = {
            "result_of_game": "1-0"
        }
        print(f"Emitting `end_chess_game` on namespace: `{self.chess_game_namespace}`")
        await self.sio.emit(
            "end_chess_game",
            data=data_to_send,
            namespace=self.chess_game_namespace
        )

    class GUIWindow(customtkinter.CTk):

        def __init__(
                self,
                event_loop: asyncio.AbstractEventLoop,
                on_start_chess_game,
                on_write_event_and_players_data_chess_game,
                on_execute_procedure_of_move_white,
                on_execute_procedure_of_move_black,
                on_end_chess_game
        ):
            super(GUIClient.GUIWindow, self).__init__()
            self.geometry("500x500")
            self.setup_config_colors()
            self.setup_config_texts()
            self.set_default_appearance_of_layout()
            self.set_init_all_labels_buttons()

            self._event_loop = event_loop
            self._on_start_chess_game = on_start_chess_game
            self._on_write_event_and_players_data_chess_game = on_write_event_and_players_data_chess_game
            self._on_execute_procedure_of_move_white = on_execute_procedure_of_move_white
            self._on_execute_procedure_of_move_black = on_execute_procedure_of_move_black
            self._on_end_chess_game = on_end_chess_game

        def setup_config_colors(
                self
        ):
            self.default_apperance_color_mode = "dark"
            self.default_apperance_color_theme = "dark-blue"
            self.default_button_color = "#1f538d"  # what means button is enabled

        def setup_config_texts(
                self
        ):
            self.default_label_text = "GUI CHESS APP"
            self.default_button_start_chess_game = "\n START CHESS GAME \n"
            self.default_button_write_event_and_players_data_chess_game = "\n WRITE CHESS GAME DATA \n"
            self.default_button_execute_procedure_of_move_white = "\n PLAY MOVE WHITE \n"
            self.default_button_execute_procedure_of_move_black = "\n PLAY MOVE BLACK \n"
            self.default_button_end_chess_game = "\n END GAME \n"

        def set_default_appearance_of_layout(
                self
        ):
            customtkinter.set_appearance_mode(
                self.default_apperance_color_mode
            )
            customtkinter.set_default_color_theme(
                self.default_apperance_color_theme
            )

        async def show(
                self
        ):
            while True:
                self.update()
                await asyncio.sleep(0.05)

        def set_init_all_labels_buttons(self):

            print("Setting buttons and labels")

            self.frame = customtkinter.CTkFrame(
                master=self
            )
            self.frame.pack(pady=0, padx=0, fill="both", expand=True)

            self.label = customtkinter.CTkLabel(
                master=self.frame,
                text=self.default_label_text,
                font=("Helvetica", 24, "bold"),
                anchor="e")
            self.label.place(relx=0.3, y=50)

            config_buttons_width = 200

            self.button_start_chess_game = customtkinter.CTkButton(
                master=self.frame,
                text=self.default_button_start_chess_game,
                width=config_buttons_width,
                font=("Helvetica", 12, "bold"),
                command=lambda: self._event_loop.create_task(self._on_start_chess_game())
            )
            self.button_start_chess_game.place(x=150, y=100)

            self.button_write_event_and_players_data_chess_game = customtkinter.CTkButton(
                master=self.frame,
                text=self.default_button_write_event_and_players_data_chess_game,
                width=config_buttons_width,
                font=("Helvetica", 12, "bold"),
                command=lambda: self._event_loop.create_task(self._on_write_event_and_players_data_chess_game())
            )
            self.button_write_event_and_players_data_chess_game.place(x=150, y=170)

            self.button_execute_procedure_of_move_white = customtkinter.CTkButton(
                master=self.frame,
                text=self.default_button_execute_procedure_of_move_white,
                width=config_buttons_width,
                font=("Helvetica", 12, "bold"),
                command=lambda: self._event_loop.create_task(self._on_execute_procedure_of_move_white())
            )
            self.button_execute_procedure_of_move_white.place(x=150, y=240)

            self.button_execute_procedure_of_move_black = customtkinter.CTkButton(
                master=self.frame,
                text=self.default_button_execute_procedure_of_move_black,
                width=config_buttons_width,
                font=("Helvetica", 12, "bold"),
                command=lambda: self._event_loop.create_task(self._on_execute_procedure_of_move_black())
            )
            self.button_execute_procedure_of_move_black.place(x=150, y=310)

            self.button_end_chess_game = customtkinter.CTkButton(
                master=self.frame,
                text=self.default_button_end_chess_game,
                width=config_buttons_width,
                font=("Helvetica", 12, "bold"),
                command=lambda: self._event_loop.create_task(self._on_end_chess_game())
            )
            self.button_end_chess_game.place(x=150, y=380)


if __name__ == '__main__':
    gui_client = GUIClient()