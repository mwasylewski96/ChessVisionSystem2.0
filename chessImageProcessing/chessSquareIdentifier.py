import json
from chessTools.chessConfig import get_chess_path_to_corners, \
    get_chess_board_letters, get_chess_board_numbers
from typing import Dict


class ChessboardIdentifier:

    @staticmethod
    def check_square_on_chess_board(
            center: Dict[str, int],
            corners: Dict[str, Dict[str, int]]
    ):
        letters = get_chess_board_letters()
        numbers = get_chess_board_numbers()
        it_l = 0
        it_n = 0
        for _ in range(8):
            for _ in range(8):
                if corners[letters[it_l] + numbers[it_n]]["x"] < center["x"] < corners[letters[it_l+1] + numbers[it_n]]["x"] and \
                        corners[letters[it_l] + numbers[it_n]]["y"] > center["y"] > corners[letters[it_l] + numbers[it_n+1]]["y"]:
                    return letters[it_l] + numbers[it_n]
                it_l += 1
            it_l = 0
            it_n += 1
        return None


if __name__ == '__main__':
    with open(get_chess_path_to_corners(), 'r') as file:
        corners = json.load(file)

    obj = ChessboardIdentifier()

    # TEST ALL BOARD
    default_x = 150
    default_y = 423

    const_x = 0
    const_y = 0

    for _ in range(8):
        for _ in range(8):
            print(obj.check_square_on_chess_board(
                center={"x": default_x+const_x, "y": default_y-const_y},
                corners=corners
            ))
            const_y += 50
        const_y = 0
        const_x += 50