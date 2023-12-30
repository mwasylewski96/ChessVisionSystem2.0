########################
#  INTERNAL LIBRARIES  #
########################
from chessGameControl.chessGameController import ChessGameController
from chessApiTools.chessSocketInputs import *
from chessApiTools.chessSocketOutputs import *


class ChessModel:

    def __init__(self):
        self.chess_methods: ChessModel.ChessGameMethods = ChessModel.ChessGameMethods()

    class ChessGameMethods:

        def __init__(self):
            self.chess_game_controller: ChessGameController = ChessGameController()

        async def start_chess_game(
                self,
                chess_endpoint_input: StartChessGameInput
        ) -> StartChessGameOutput:
            data_to_send = {"error": None}
            try:
                data = self.chess_game_controller.start_chess_game()
            except Exception as err:
                data_to_send['error'] = f"{err}"
                return StartChessGameOutput(
                    success=False,
                    payload=data_to_send,
                    message=f"[FAILURE] Failed with starting a new game"
                )
            if data.success:
                return StartChessGameOutput(
                    success=True,
                    payload=None,
                    message="[SUCCESS] Successfully started a new game"
                )
            else:
                return StartChessGameOutput(
                    success=False,
                    payload=None,
                    message="[FAILURE] Failed with starting a new game"
                )

        async def write_event_and_players_data_chess_game(
                self,
                chess_endpoint_input: WriteEventAndPlayersDataChessGameInput
        ) -> WriteEventAndPlayersDataChessGameOutput:

            data_to_send = {"error": None}

            if chess_endpoint_input.error is not None:
                data_to_send['error'] = chess_endpoint_input.error
                return WriteEventAndPlayersDataChessGameOutput(
                    success=False,
                    payload=data_to_send,
                    message="[FAILURE] Failed with writing event and player data chess game"
                )
            try:
                data = self.chess_game_controller.write_event_and_players_data_chess_game(
                    **chess_endpoint_input.to_payload()
                )
            except Exception as err:
                data_to_send['error'] = f"{err}"
                return WriteEventAndPlayersDataChessGameOutput(
                    success=False,
                    payload=data_to_send,
                    message=f"[FAILURE] Failed with writing event and player data chess game"
                )
            if data.success:
                return WriteEventAndPlayersDataChessGameOutput(
                    success=True,
                    payload=data_to_send,
                    message="[SUCCESS] Successfully written event and player data chess game"
                )
            else:
                data_to_send['error'] = data.error
                return WriteEventAndPlayersDataChessGameOutput(
                    success=False,
                    payload=data_to_send,
                    message="[FAILURE] Failed with writing event and player data chess game"
                )

        async def execute_procedure_of_move(
                self,
                chess_endpoint_input: ExecuteProcedureOfMoveInput
        ) -> ExecuteProcedureOfMoveOutput:

            data_to_send = {"error": None}

            if chess_endpoint_input.error is not None:
                data_to_send['error'] = chess_endpoint_input.error
                return ExecuteProcedureOfMoveOutput(
                    success=False,
                    payload=data_to_send,
                    message="[FAILURE] Failed with executing procedure of move!"
                )
            try:
                data = self.chess_game_controller.execute_procedure_of_move(
                    **chess_endpoint_input.to_payload()
                )
            except AssertionError as err:
                data_to_send['error'] = f"{err}"
                return ExecuteProcedureOfMoveOutput(
                    success=False,
                    payload=data_to_send,
                    message=f"[FAILURE] Failed with executing procedure of move {chess_endpoint_input.color}"
                )
            except Exception as err:
                data_to_send['error'] = f"{err}"
                return ExecuteProcedureOfMoveOutput(
                    success=False,
                    payload=data_to_send,
                    message=f"[FAILURE] Failed with executing procedure of move {chess_endpoint_input.color}"
                )
            if data.success:
                return ExecuteProcedureOfMoveOutput(
                    success=True,
                    payload=data_to_send,
                    message=f"[SUCCESS] Successfully executed procedure of move {chess_endpoint_input.color}"
                )
            else:
                data_to_send['error'] = data.error
                return ExecuteProcedureOfMoveOutput(
                    success=False,
                    payload=data_to_send,
                    message=f"[FAILURE] Failed with executing procedure of move {chess_endpoint_input.color}"
                )

        async def end_chess_game(
                self,
                chess_endpoint_input: EndChessGameInput
        ) -> EndChessGameOutput:

            data_to_send = {"error": None}

            if chess_endpoint_input.error is not None:
                data_to_send['error'] = chess_endpoint_input.error
                return EndChessGameOutput(
                    success=False,
                    payload=data_to_send,
                    message=f"[FAILURE] Failed with ending game with result!"
                )
            try:
                data = self.chess_game_controller.end_chess_game(
                    **chess_endpoint_input.to_payload()
                )
            except Exception as err:
                data_to_send['error'] = f"DUPPPAA {err}"
                return EndChessGameOutput(
                    success=False,
                    payload=data_to_send,
                    message=f"[FAILURE] Failed with ending game with result: {chess_endpoint_input.result_of_game}"
                )
            if data.success:
                return EndChessGameOutput(
                    success=True,
                    payload=data_to_send,
                    message=f"[SUCCESS] Successfully ended game with result: {chess_endpoint_input.result_of_game}"
                )
            else:
                data_to_send['error'] = data.error
                return EndChessGameOutput(
                    success=False,
                    payload=data_to_send,
                    message=f"[FAILURE] Failed with ending game with result: {chess_endpoint_input.result_of_game}"
                )