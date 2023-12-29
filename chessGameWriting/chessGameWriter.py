from chessTools.chessConfig import get_chess_directory_path_game
import datetime


class ChessGameWriter:

    def __init__(
            self,
            game_name
    ):
        self.__main_path = get_chess_directory_path_game()
        date = datetime.datetime.now()
        self.__current_game_path = f"{self.__main_path}/{game_name}_{date.strftime('%H-%M-%S')}.txt"
        self.__date = date.strftime('%Y.%m.%d')
        self.__setup_init_config_game_pattern()
        self.__create_init_game()

    def reset_to_new_game(self, game_name):
        self.__main_path = get_chess_directory_path_game()
        date = datetime.datetime.now()
        self.__current_game_path = f"{self.__main_path}/{game_name}_{date.strftime('%H-%M-%S')}.txt"
        self.__date = date.strftime('%Y.%m.%d')
        self.__setup_init_config_game_pattern()
        self.__create_init_game()

    def __setup_init_config_game_pattern(self):
        self.__game_event = "[Event \"\"]"
        self.__game_date = f"[Date \"{self.__date}\"]"
        self.__game_white = f"[White \"\"]"
        self.__game_black = f"[Black \"\"]"
        self.__game_result = f"[Result \"\"]"
        self.__game_init_data = [
            self.__game_event,
            self.__game_date,
            self.__game_white,
            self.__game_black,
            self.__game_result
        ]
        self.__game_move_number = 1

    def __create_init_game(self):
        with open(self.__current_game_path, 'w') as file:
            for line in self.__game_init_data:
                file.write(line+"\n")
            file.seek(0)

    def __game_parameter_decorator(
            this_game_param_value,
            line_number: int
    ):
        def decorator(method):
            def wrapper(
                    self,
                    value
            ):
                this_game_param = this_game_param_value.format(value)
                with open(self.__current_game_path, 'r+') as file:
                    lines = file.readlines()
                    lines[line_number] = this_game_param + '\n'
                    file.seek(0)
                    file.writelines(lines)
                method(self, value)
            return wrapper
        return decorator

    @__game_parameter_decorator(
        this_game_param_value="[Event \"{0}\"]",
        line_number=0
    )
    def set_event_game(
            self,
            event
    ):
        self.__game_event = f"[Event \"{event}\"]"

    @__game_parameter_decorator(
        this_game_param_value="[White \"{0}\"]",
        line_number=2
    )
    def set_white_game(
            self,
            white
    ):
        self.__game_white = f"[White \"{white}\"]"

    @__game_parameter_decorator(
        this_game_param_value="[Black \"{0}\"]",
        line_number=3
    )
    def set_black_game(
            self,
            black
    ):
        self.__game_black = f"[Black \"{black}\"]"

    @__game_parameter_decorator(
        this_game_param_value="[Result \"{0}\"]",
        line_number=4
    )
    def set_result_game(
            self,
            result
    ):
        self.__game_result = f"[Result \"{result}\"]"

    def write_white_move(self, move):
        text = f"{self.__game_move_number}.{move}"
        with open(self.__current_game_path, 'a') as file:
            file.write(text)

    def write_black_move(self, move):
        text = f" {move}\n"
        with open(self.__current_game_path, 'a') as file:
            file.write(text)
        self.__game_move_number += 1


if __name__ == "__main__":
    game_writer = ChessGameWriter(game_name="game_")
    game_writer.set_event_game(value="Friend")
    game_writer.set_white_game(value="Marcin")
    game_writer.set_black_game(value="Jan")
    game_writer.write_white_move(move="e4")
    game_writer.write_black_move(move="c5")
    game_writer.write_white_move(move="Nf3")
    game_writer.write_black_move(move="d6")
    game_writer.write_white_move(move="d4")
    game_writer.write_black_move(move="cxd4")
    game_writer.write_white_move(move="Nxd4")
    game_writer.write_black_move(move="Nf6")
    game_writer.write_white_move(move="Nc3")
    game_writer.write_black_move(move="a6")
    game_writer.write_white_move(move="Bg5")
    game_writer.set_result_game(value="1-0")