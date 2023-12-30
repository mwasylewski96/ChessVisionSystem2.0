########################
#  EXTERNAL LIBRARIES  #
########################
from aiohttp import web
import socketio
from typing import Type
##########################
#  INTERNAL LIBRARIES  #
##########################
from chessApiTools.chessEndpoints import *
from chessApiTools.chessSocketOutputs import *
from chessGameModel.chessModel import ChessModel


class ChessServer(web.Application):

    def __init__(
            self,
            chess_client: Literal['chess_local_gui', 'chess_flet_app']
    ):
        super(ChessServer, self).__init__()

        self.chess_model = ChessModel()
        self.socket: socketio.AsyncServer = ChessServer.Socket(
            chess_model=self.chess_model,
            chess_client=chess_client
        )
        self.cleanup_ctx.append(
            self.subprocesses
        )
        self.socket.attach(
            self
        )

    async def subprocesses(
            self,
            app
    ):
        self.chess_model.chess_methods.chess_game_controller.reset_chess_table_to_starting_position()
        print("Server turn on")
        yield
        print("Server turn off")

    class Socket(socketio.AsyncServer):

        def __init__(
                self,
                chess_model: ChessModel,
                chess_client: Literal['chess_local_gui', 'chess_flet_app'],
                async_mode='aiohttp'
        ):
            super(ChessServer.Socket, self).__init__(async_mode=async_mode, cors_allowed_origins='*')

            self.chess_game_namespace = "/chess_game"
            self.register_namespace(socketio.AsyncNamespace(
                namespace=self.chess_game_namespace
            ))

            if chess_client == "chess_local_gui":
                self.client_event_pattern = "_local_gui_response"
            if chess_client == "chess_flet_app":
                self.client_event_pattern = "_chess_flet_app_response"

            def chess_server_socket_decorator(
                    chess_model_method: callable,
                    chess_endpoint: Type[Endpoint],
                    chess_socket_output: Type[SocketOutput],
            ):
                """

                :param chess_model_method:
                :param chess_endpoint:
                :param chess_socket_output:
                :return:
                """

                def inner(
                        wrapped_chess_server_method: callable
                ):
                    """

                    :param wrapped_chess_server_method:
                    :return:
                    """

                    print(f"Setting up `{wrapped_chess_server_method.__name__}` "
                          f"endpoint on namespace: `{self.chess_game_namespace}`.")

                    async def wrapper(
                            sid,
                            data_dict: Optional[dict] = None
                    ) -> None:
                        print(f"{wrapped_chess_server_method.__name__}` process started on namespace:"
                              f" `{self.chess_game_namespace}`... data_dict: `{data_dict}`")
                        parsed_input = chess_endpoint.parse_input(
                            sid=sid,
                            data=data_dict
                        )
                        print(f"Acquiring data with `{parsed_input}`")
                        chess_model_response = await chess_model_method(
                            chess_endpoint_input=parsed_input
                        )
                        if chess_model_response.success:
                            print(f"{wrapped_chess_server_method.__name__} process finished successfully!")
                        print(f"Emitting response to: '{wrapped_chess_server_method.__name__ + '_response'}' on namespace: '{self.chess_game_namespace}'")
                        print(f"Chess model response: {chess_model_response}")
                        await self.emit(
                            f"{wrapped_chess_server_method.__name__ + self.client_event_pattern}",
                            chess_model_response.serialize(),
                            namespace=self.chess_game_namespace,
                            room=sid
                        )

                    self.on(wrapped_chess_server_method.__name__, handler=wrapper, namespace=self.chess_game_namespace)
                return inner

            @chess_server_socket_decorator(
                chess_model_method=chess_model.chess_methods.start_chess_game,
                chess_endpoint=StartChessGameEndpoint,
                chess_socket_output=StartChessGameOutput,
            )
            async def start_chess_game():
                pass

            @chess_server_socket_decorator(
                chess_model_method=chess_model.chess_methods.write_event_and_players_data_chess_game,
                chess_endpoint=WriteEventAndPlayersDataChessGameEndpoint,
                chess_socket_output=WriteEventAndPlayersDataChessGameOutput,
            )
            async def write_event_and_players_data_chess_game():
                pass

            @chess_server_socket_decorator(
                chess_model_method=chess_model.chess_methods.execute_procedure_of_move,
                chess_endpoint=ExecuteProcedureOfMoveEndpoint,
                chess_socket_output=ExecuteProcedureOfMoveOutput,
            )
            async def execute_procedure_of_move():
                pass

            @chess_server_socket_decorator(
                chess_model_method=chess_model.chess_methods.end_chess_game,
                chess_endpoint=EndChessGameEndpoint,
                chess_socket_output=EndChessGameOutput,
            )
            async def end_chess_game():
                pass


def main():
    server = ChessServer(
        chess_client="chess_local_gui"
        # chess_client="chess_flet_app"
    )
    web.run_app(server)


if __name__ == '__main__':
    main()

