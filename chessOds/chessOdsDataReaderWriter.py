############################
###  EXTERNAL LIBRARIES  ###
############################
from enum import Enum
import ezodf

############################
###  INTERNAL LIBRARIES  ###
############################
from chessTools.chessConfig import get_chess_current_game_table_config, get_chess_config


class ChessPath(str, Enum):
    PATH_TO_GAME: str = get_chess_current_game_table_config()


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

    def read_all_data(
            self
    ):
        self.doc = ezodf.opendoc(ChessPath.PATH_TO_GAME)
        sheet_name = self.doc.sheets[0].name
        self.sheet_data = self.doc.sheets[sheet_name]
        return self.sheet_data

    def read_all_chess_table_figures_positions(
            self
    ):
        self.sheet_data = self.read_all_data()
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
    obj.read_all_chess_table_figures_positions()

    obj.move_chosen_figure_to_another_place("E2", "E4")
    obj.read_all_chess_table_figures_positions()

    obj.move_chosen_figure_to_another_place("C7", "C5")
    obj.read_all_chess_table_figures_positions()

    obj.move_chosen_figure_to_another_place("G1", "F3")
    obj.read_all_chess_table_figures_positions()

    obj.move_chosen_figure_to_another_place("D7", "D6")
    obj.read_all_chess_table_figures_positions()

    obj.move_chosen_figure_to_another_place("D2", "D4")
    obj.read_all_chess_table_figures_positions()
