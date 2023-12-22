import json
import unittest
from chessTools.chessConfig import get_chess_path_to_corners, get_chess_board_letters, get_chess_board_numbers
from chessImageProcessing.chessSquareIdentifier import ChessboardIdentifier


class TestChessboardIdentifier(unittest.TestCase):

    def setUp(self):
        with open(get_chess_path_to_corners(), 'r') as file:
            corners = json.load(file)
        self.corners = corners
        self.letters = get_chess_board_letters()[:-1]
        self.numbers = get_chess_board_numbers()[:-1]

    def test_simple_check_all_squares(self):
        # TEST ALL BOARD
        default_x = 150
        default_y = 423

        const_x = 0
        const_y = 0

        it_l = 0
        it_n = 0

        for _ in range(8):
            for _ in range(8):
                self.assertEqual(
                    self.letters[it_l] + self.numbers[it_n],
                    ChessboardIdentifier.check_square_on_chess_board(
                        center={"x": default_x + const_x, "y": default_y - const_y},
                        corners=self.corners
                    ))
                it_n += 1
                const_y += 50
            it_n = 0
            it_l += 1
            const_y = 0
            const_x += 50


if __name__ == '__main__':
    unittest.main()
