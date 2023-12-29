############################
###  EXTERNAL LIBRARIES  ###
############################
from enum import Enum
import ezodf
from typing import Literal, Optional

############################
###  INTERNAL LIBRARIES  ###
############################
from chessTools.chessConfig import get_chess_current_game_table_config, \
    get_chess_init_game_table_config, get_chess_config


class ChessPath(str, Enum):
    PATH_TO_CURRENT_GAME: str = get_chess_current_game_table_config()
    PATH_TO_INIT_GAME: str = get_chess_init_game_table_config()


class ChessBoard(str, Enum):
    LETTERS: str = get_chess_config()['board']['letters']
    NUMBERS: str = get_chess_config()['board']['numbers']


class ChessOdsDataReaderWriter:

    def __init__(
            self
    ):
        self.doc = None
        self.sheet_data = None

        self.figure_positions = {}
        for letter in ChessBoard.LETTERS:
            for number in ChessBoard.NUMBERS:
                self.figure_positions.update({
                        letter+number: None
                    }
                )
        # self.reset_chess_table_to_starting_position()

    def reset_chess_table_to_starting_position(self):
        init_positions = self.read_all_chess_table_figures_positions(
            game="init"
        )
        self.read_all_data(
            path=ChessPath.PATH_TO_CURRENT_GAME
        )
        for addr_place, figure in init_positions.items():
            self.__write_chosen_figure_to_given_place(
                addr_place=addr_place,
                figure=figure
            )

        self.read_all_chess_table_figures_positions()

    def read_all_data(
            self,
            path
    ):
        self.doc = ezodf.opendoc(path)
        sheet_name = self.doc.sheets[0].name
        self.sheet_data = self.doc.sheets[sheet_name]
        return self.sheet_data

    def read_all_chess_table_figures_positions(
            self,
            game: Optional[Literal["current", "init"]] = "current"
    ):
        if game == "current":
            self.sheet_data = self.read_all_data(ChessPath.PATH_TO_CURRENT_GAME)
        if game == "init":
            self.sheet_data = self.read_all_data(ChessPath.PATH_TO_INIT_GAME)
        self.figure_positions = {
            addr_place: self.sheet_data[addr_place].value for addr_place, figure in self.figure_positions.items()
        }
        return self.figure_positions

    def get_chosen_figure_from_given_place(
            self,
            addr_place
    ):
        return self.figure_positions[addr_place]

    def move_chosen_figure_to_another_place(
            self,
            addr_place_start,
            addr_place_end
    ):
        figure = self.get_chosen_figure_from_given_place(
            addr_place=addr_place_start
        )
        self.__write_chosen_figure_to_given_place(
            addr_place=addr_place_end,
            figure=figure
        )
        self.__clean_given_place(
            addr_place=addr_place_start
        )
        self.read_all_chess_table_figures_positions()

    def __clean_given_place(self, addr_place):
        self.__write_chosen_figure_to_given_place(
            addr_place=addr_place,
            figure=None
        )

    def __write_chosen_figure_to_given_place(
            self,
            addr_place,
            figure
    ):
        cell = self.sheet_data[addr_place]
        if figure is not None:
            cell.set_value(figure)
        else:
            cell.clear()
        self.doc.save()


if __name__ == "__main__":
    obj = ChessOdsDataReaderWriter()
    obj.reset_chess_table_to_starting_position()
    # obj.read_all_chess_table_figures_positions()
    # obj.move_chosen_figure_to_another_place("E2", "E4")
    # obj.move_chosen_figure_to_another_place("C7", "C5")
    # obj.move_chosen_figure_to_another_place("G1", "F3")
    # obj.move_chosen_figure_to_another_place("D7", "D6")
    # obj.move_chosen_figure_to_another_place("D2", "D4")

