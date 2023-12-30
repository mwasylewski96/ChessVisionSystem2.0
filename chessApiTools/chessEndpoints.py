########################
#  EXTERNAL LIBRARIES  #
########################
from abc import ABC, abstractmethod
from pydantic import ValidationError
########################
#  INTERNAL LIBRARIES  #
########################
from chessApiTools.chessSocketInputs import *


class Endpoint(ABC):

    @classmethod
    @abstractmethod
    def parse_input(
            cls,
            sid,
            data: Optional[dict] = None
    ):
        raise NotImplementedError


class StartChessGameEndpoint(Endpoint):

    @classmethod
    def parse_input(
            cls,
            sid,
            data=None,
            **kwargs
    ):
        return StartChessGameInput(
            sid=sid
        )


class WriteEventAndPlayersDataChessGameEndpoint(Endpoint):

    @classmethod
    def parse_input(
            cls,
            sid,
            data=None,
            **kwargs
    ):
        try:
            return WriteEventAndPlayersDataChessGameInput(
                sid=sid,
                **data
            )

        except ValidationError as err:
            error = f"{err}"
            return WriteEventAndPlayersDataChessGameInput(
                sid=sid,
                error=error
            )


class ExecuteProcedureOfMoveEndpoint(Endpoint):

    @classmethod
    def parse_input(
            cls,
            sid,
            data=None,
            **kwargs
    ):
        try:
            return ExecuteProcedureOfMoveInput(
                sid=sid,
                color=data['color']
            )

        except ValidationError as err:
            error = f"{err}"
            return ExecuteProcedureOfMoveInput(
                sid=sid,
                error=error,
                color=None
            )


class EndChessGameEndpoint(Endpoint):

    @classmethod
    def parse_input(
            cls,
            sid,
            data=None,
            **kwargs
    ):
        try:
            return EndChessGameInput(
                sid=sid,
                **data
            )

        except ValidationError as err:
            error = f"{err}"
            return EndChessGameInput(
                sid=sid,
                error=error
            )