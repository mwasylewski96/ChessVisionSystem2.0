import unittest
from unittest.mock import patch
from chessOds.chessOdsDataReaderWriter import ChessOdsDataReaderWriter


class TestChessOdsDataReaderWriter(unittest.TestCase):

    def setUp(self):
        self.chess_ods_data_reader_writer = ChessOdsDataReaderWriter()
        self.figure_positions = self.chess_ods_data_reader_writer.read_all_chess_table_figures_positions()

    def tearDown(self) -> None:
        self.chess_ods_data_reader_writer.reset_chess_table_to_starting_position()

    def test_get_chosen_figure_from_given_place(self):
        self.assertEqual(
            "wB",
            self.chess_ods_data_reader_writer.get_chosen_figure_from_given_place(
                addr_place="C1")
        )

    def test_move_chosen_figure_to_another_place_vefication(self):
        self.chess_ods_data_reader_writer.move_chosen_figure_to_another_place("E2", "E4")
        self.chess_ods_data_reader_writer.move_chosen_figure_to_another_place("A7", "A5")
        self.chess_ods_data_reader_writer.move_chosen_figure_to_another_place("G1", "F3")
        self.chess_ods_data_reader_writer.move_chosen_figure_to_another_place("G8", "F6")

        check_places = {
            "E2": None,
            "E4": "wp",
            "A7": None,
            "A5": "bp",
            "G1": None,
            "F3": "wN",
            "G8": None,
            "F6": "bN"
        }

        for addr_place, figure in check_places.items():
            self.assertEqual(
               figure,
               self.chess_ods_data_reader_writer.get_chosen_figure_from_given_place(
                   addr_place=addr_place)
            )

    def test_reset_chess_table_to_starting_position(self):
        self.chess_ods_data_reader_writer.move_chosen_figure_to_another_place("D2", "D4")  # example move
        self.chess_ods_data_reader_writer.reset_chess_table_to_starting_position()

        self.chess_ods_data_reader_writer_init = ChessOdsDataReaderWriter()
        self.figure_positions_init = self.chess_ods_data_reader_writer_init.read_all_chess_table_figures_positions(
            game="init"
        )

        self.assertEqual(
            self.chess_ods_data_reader_writer_init.figure_positions,
            self.chess_ods_data_reader_writer.figure_positions
        )