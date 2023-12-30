########################
#  EXTERNAL LIBRARIES  #
########################
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class SocketOutput:
    success: bool
    payload: Optional[dict] = None
    message: Optional[str] = None

    def serialize(
            self
    ):
        return asdict(
            self
        )


@dataclass
class StartChessGameOutput(SocketOutput):
    pass


@dataclass
class WriteEventAndPlayersDataChessGameOutput(SocketOutput):
    pass


@dataclass
class ExecuteProcedureOfMoveOutput(SocketOutput):
    pass


@dataclass
class EndChessGameOutput(SocketOutput):
    pass