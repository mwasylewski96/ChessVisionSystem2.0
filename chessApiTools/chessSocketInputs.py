########################
#  EXTERNAL LIBRARIES  #
########################
from pydantic import BaseModel
from typing import Optional, Literal


class SocketInput(BaseModel):
    sid: str
    error: Optional[dict] = None

    def to_payload(
            self
    ):
        data = self.model_dump()
        data = {key: value for key, value in data.items() if key != "sid" and key != "error"}
        return data


class StartChessGameInput(SocketInput):
    pass


class WriteEventAndPlayersDataChessGameInput(SocketInput):
    event: Optional[str] = None
    white_player: Optional[str] = None
    black_player: Optional[str] = None


class ExecuteProcedureOfMoveInput(SocketInput):
    color: Literal['white', 'black']


class EndChessGameInput(SocketInput):
    result_of_game: Optional[Literal['1-0', '0-1', '1/2-1/2']] = None
