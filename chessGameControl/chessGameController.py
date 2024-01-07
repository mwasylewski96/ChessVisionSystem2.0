import cv2
import imutils
import numpy as np
import multiprocessing
import threading
import time
from screeninfo import get_monitors
# from chessCalibrations.chessCalibration import ChessCalibrator
from chessCameraProcessing.chessCameraRecording import ChessCameraRecorder
from chessGameWriting.chessGameWriter import ChessGameWriter
from chessImageProcessing.chessColorDetection import ChessColorDetector
from chessImageProcessing.chessCornerDetector import ChessCornerDetector, \
    get_white_corners_on_black_screen, load_chess_corners, get_point_or_points_board
from chessImageProcessing.chessSquareIdentifier import ChessboardIdentifier
from chessOds.chessOdsDataReaderWriter import ChessOdsDataReaderWriter

from chessTools.chessConfig import get_chess_config
from chessTools.chessTool import is_button_pressed, stack_images, Result

from typing import Callable, Literal, Optional


class ChessGameController:

    def __init__(
            self
    ):
        self.chess_game_writer = ChessGameWriter(
            game_name="game"
        )
        self.chess_color_detector = ChessColorDetector()
        self.chess_ods_data_r_w = ChessOdsDataReaderWriter()

        self.window_name = None
        self.black_screen = None
        self.screen_width = None
        self.screen_height = None
        self.temp_img = None
        self.saved_image = None

        self.current_before_move_img = None
        self.current_after_move_img = None

        manager = multiprocessing.Manager()
        stacked_image_init_dict = {
            "temp_image": None,
            "white_and_black_detected_image": None,
            "detected_move": None,
            "white_corners_on_black_screen": None
        }
        self.stacked_image = manager.dict(stacked_image_init_dict)
        self.stacked_image_lock = multiprocessing.Lock()

        self.__camera_get_frame_process = None
        self.__camera_display_stacked_images_process = None

        self.__camera_get_frame_process_event = multiprocessing.Event()
        self.__camera_display_stacked_images_process_event = multiprocessing.Event()

        self.corners_from_json = load_chess_corners()

        self.__setup_camera_get_frame_process()
        self.__start_camera_get_frame_process()

        self.__setup_camera_display_stacked_images_process()
        self.__start_camera_display_stacked_images_process()

        self.activated_color = None

        print("Initialised")

    def activate_color(
            self,
            color: Literal["white", "black"]
    ):
        self.activated_color = color

    def reset_chess_table_to_starting_position(
            self
    ):
        self.chess_ods_data_r_w.reset_chess_table_to_starting_position()

    def start_chess_game(
            self
    ):
        try:
            self.__set_current_before_move_img(
                color="white"
            )
        except Exception as err:
            return Result.error(
                error=f"{err}"
            )

        try:
            self.reset_chess_table_to_starting_position()
        except Exception as err:
            return Result.error(
                error=f"{err}"
            )

        try:
            self.chess_game_writer.reset_to_new_game(
                game_name="game"
            )
        except Exception as err:
            return Result.error(
                error=f"{err}"
            )

        self.activate_color(
            color="white"
        )

        return Result.success()

    def execute_procedure_of_move(
            self,
            color: Literal['white', 'black']
    ):
        if color == "white":
            assert self.activated_color == "white", "[FAILURE] It is not white move!"
            self.__set_current_after_move_img(
                color="white"
            )
        if color == "black":
            assert self.activated_color == "black", "[FAILURE] It is not black move!"
            self.__set_current_after_move_img(
                color="black"
            )

        position_figure_after = self.__get_img_after_move()
        position_figure_before = self.__get_img_before_move()

        self.__set_detected_move(
            img_before=position_figure_before,
            img_after=position_figure_after
        )

        center_of_after_move = self.__find_center_of_change(
            img=position_figure_after
        )
        center_of_before_move = self.__find_center_of_change(
            img=position_figure_before
        )

        center_of_after_move = get_point_or_points_board(
            center_elements=center_of_after_move
        )

        center_of_before_move = get_point_or_points_board(
            center_elements=center_of_before_move
        )
        print(f"FOUND: {center_of_after_move}")
        print(f"FOUND: {center_of_before_move}")

        castle_strong_move = len(center_of_before_move) == len(center_of_after_move) == 2
        castle_not_strong_1 = len(center_of_before_move) == 2 and len(center_of_after_move) == 1
        castle_not_strong_2 = len(center_of_before_move) == 1 and len(center_of_after_move) == 2
        if castle_not_strong_1 or castle_not_strong_2:
            print("WARNING! It is probably castle but check move!")

        if castle_strong_move or castle_not_strong_1 or castle_not_strong_2:
            identify_squares = []
            for center_element in center_of_before_move:
                identified_square_before_move = ChessboardIdentifier.check_square_on_chess_board(
                    center=center_element,
                    corners=self.corners_from_json
                )
                identify_squares.append(identified_square_before_move)
            self.identified_square_before_move = identify_squares

            identify_squares = []
            for center_element in center_of_after_move:
                identified_square_after_move = ChessboardIdentifier.check_square_on_chess_board(
                    center=center_element,
                    corners=self.corners_from_json
                )
                identify_squares.append(identified_square_after_move)
            self.identified_square_after_move = identify_squares

            ods_read_before_move_list = []
            for addr_place_identified in self.identified_square_before_move:
                try:
                    ods_read_before_move = self.chess_ods_data_r_w.get_chosen_figure_from_given_place(
                        addr_place=addr_place_identified
                    )
                except Exception as err:
                    return Result.error(
                        error=f"{err}"
                    )

                ods_read_before_move_list.append(ods_read_before_move)
            ods_read_before_move = ods_read_before_move_list

            ods_read_after_move_list = []
            for addr_place_identified in self.identified_square_after_move:
                try:
                    ods_read_after_move = self.chess_ods_data_r_w.get_chosen_figure_from_given_place(
                        addr_place=addr_place_identified
                    )
                except Exception as err:
                    return Result.error(
                        error=f"{err}"
                    )
                ods_read_after_move_list.append(ods_read_after_move)
            ods_read_after_move = ods_read_after_move_list

            castle_list = []
            for figure in ods_read_before_move:
                try:
                    figure_read_before_move = figure[-1]
                except TypeError:
                    figure_read_before_move = None
                castle_list.append(figure_read_before_move)
            self.figure_read_before_move = castle_list

            castle_list = []
            for figure in ods_read_after_move:
                try:
                    figure_read_after_move = figure[-1]
                except TypeError:
                    figure_read_after_move = None
                castle_list.append(figure_read_after_move)
            self.figure_read_after_move = castle_list

            print(f"Before castle {self.figure_read_before_move}")
            print(f"After castle {self.figure_read_after_move}")

            castle = None
            if color == "white":
                if "a1" in self.identified_square_before_move and \
                    "e1" in self.identified_square_before_move and \
                    "c1" in self.identified_square_after_move and \
                    "d1" in self.identified_square_after_move:

                    try:
                        self.chess_ods_data_r_w.move_chosen_figure_to_another_place(
                            addr_place_start="a1",
                            addr_place_end="d1"
                        )
                    except Exception as err:
                        return Result.error(
                            error=f"{err}"
                        )

                    try:
                        self.chess_ods_data_r_w.move_chosen_figure_to_another_place(
                            addr_place_start="e1",
                            addr_place_end="c1"
                        )
                    except Exception as err:
                        return Result.error(
                            error=f"{err}"
                        )

                    castle = "0-0-0"

                if "h1" in self.identified_square_before_move and \
                        "e1" in self.identified_square_before_move and \
                        "g1" in self.identified_square_after_move and \
                        "f1" in self.identified_square_after_move:

                    try:
                        self.chess_ods_data_r_w.move_chosen_figure_to_another_place(
                            addr_place_start="e1",
                            addr_place_end="g1"
                        )
                    except Exception as err:
                        return Result.error(
                            error=f"{err}"
                        )

                    try:
                        self.chess_ods_data_r_w.move_chosen_figure_to_another_place(
                            addr_place_start="h1",
                            addr_place_end="f1"
                        )
                    except Exception as err:
                        return Result.error(
                            error=f"{err}"
                        )

                    castle = "0-0"

            if color == "black":
                if "a8" in self.identified_square_before_move and \
                        "e8" in self.identified_square_before_move and \
                        "c8" in self.identified_square_after_move and \
                        "d8" in self.identified_square_after_move:
                    try:
                        self.chess_ods_data_r_w.move_chosen_figure_to_another_place(
                            addr_place_start="a8",
                            addr_place_end="d8"
                        )
                    except Exception as err:
                        return Result.error(
                            error=f"{err}"
                        )

                    try:
                        self.chess_ods_data_r_w.move_chosen_figure_to_another_place(
                            addr_place_start="e8",
                            addr_place_end="c8"
                        )
                    except Exception as err:
                        return Result.error(
                            error=f"{err}"
                        )

                    castle = "0-0-0"

                if "h8" in self.identified_square_before_move and \
                        "e8" in self.identified_square_before_move and \
                        "g8" in self.identified_square_after_move and \
                        "f8" in self.identified_square_after_move:
                    try:
                        self.chess_ods_data_r_w.move_chosen_figure_to_another_place(
                            addr_place_start="e8",
                            addr_place_end="g8"
                        )
                    except Exception as err:
                        return Result.error(
                            error=f"{err}"
                        )

                    try:
                        self.chess_ods_data_r_w.move_chosen_figure_to_another_place(
                            addr_place_start="h8",
                            addr_place_end="f8"
                        )
                    except Exception as err:
                        return Result.error(
                            error=f"{err}"
                        )

                    castle = "0-0"

            try:
                self.__write_identified_move_to_txt(
                    color=color,
                    castle=castle
                )
            except Exception as err:
                return Result.error(
                    error=f"{err}"
                )
        else:
            self.identified_square_after_move = ChessboardIdentifier.check_square_on_chess_board(
                center=center_of_after_move[0],
                corners=self.corners_from_json
            )

            self.identified_square_before_move = ChessboardIdentifier.check_square_on_chess_board(
                center=center_of_before_move[0],
                corners=self.corners_from_json
            )

            try:
                ods_read_after_move = self.chess_ods_data_r_w.get_chosen_figure_from_given_place(
                    addr_place=self.identified_square_after_move
                )
            except Exception as err:
                return Result.error(
                    error=f"{err}"
                )

            try:
                ods_read_before_move = self.chess_ods_data_r_w.get_chosen_figure_from_given_place(
                    addr_place=self.identified_square_before_move
                )
            except Exception as err:
                return Result.error(
                    error=f"{err}"
                )

            print(f"--> {ods_read_before_move}, {ods_read_after_move}")

            try:
                self.figure_read_after_move = ods_read_after_move[-1]
            except TypeError:
                self.figure_read_after_move = None

            try:
                self.figure_read_before_move = ods_read_before_move[-1]
            except TypeError:
                self.figure_read_before_move = None


            try:
                self.chess_ods_data_r_w.move_chosen_figure_to_another_place(
                    addr_place_start=self.identified_square_before_move,
                    addr_place_end=self.identified_square_after_move
                )
            except Exception as err:
                return Result.error(
                    error=f"{err}"
                )

            try:
                self.__write_identified_move_to_txt(
                    color=color
                )
            except Exception as err:
                return Result.error(
                    error=f"{err}"
                )

        if color == "white":
            self.__set_current_before_move_img(
                color="black"
            )
            self.activate_color(
                color="black"
            )
        if color == "black":
            self.__set_current_before_move_img(
                color="white"
            )
            self.activate_color(
                color="white"
            )

        return Result.success()

    def end_chess_game(
            self,
            result_of_game: Literal['1-0', '0-1', '1/2-1/2']
    ):
        try:
            self.chess_game_writer.set_result_game(
                value=result_of_game
            )
        except Exception as err:
            return Result.error(
                error=f"{err}"
            )

        return Result.success()

    def write_event_and_players_data_chess_game(
            self,
            event,
            white_player,
            black_player
    ):
        try:
            self.chess_game_writer.set_event_game(
                value=event
            )
        except Exception as err:
            return Result.error(
                error=f"{err}"
            )

        try:
            self.chess_game_writer.set_white_game(
                value=white_player
            )
        except Exception as err:
            return Result.error(
                error=f"{err}"
            )

        try:
            self.chess_game_writer.set_black_game(
                value=black_player
            )
        except Exception as err:
            return Result.error(
                error=f"{err}"
            )

        return Result.success()

    def __write_identified_move_to_txt(
            self,
            color: Literal['white', 'black'],
            castle: Optional[Literal['0-0-0', '0-0']] = None
    ):
        if color == "white":
            if castle is None:
                if self.figure_read_before_move == "p":
                    if self.figure_read_after_move is not None:
                        self.chess_game_writer.write_white_move(
                            move=f"{self.identified_square_before_move[0]}x{self.identified_square_after_move}"
                        )
                    else:
                        self.chess_game_writer.write_white_move(
                            move=f"{self.identified_square_after_move}"
                        )
                else:
                    if self.figure_read_after_move is not None:
                        self.chess_game_writer.write_white_move(
                            move=f"{self.figure_read_before_move}x{self.identified_square_after_move}"
                        )
                    else:
                        self.chess_game_writer.write_white_move(
                            move=f"{self.figure_read_before_move}{self.identified_square_after_move}"
                        )
            else:
                self.chess_game_writer.write_white_move(
                    move=f"{castle}"
                )
        if color == "black":
            if castle is None:
                if self.figure_read_before_move == "p":
                    if self.figure_read_after_move is not None:
                        self.chess_game_writer.write_black_move(
                            move=f"{self.identified_square_before_move[0]}x{self.identified_square_after_move}"
                        )
                    else:
                        self.chess_game_writer.write_black_move(
                            move=f"{self.identified_square_after_move}"
                        )
                else:
                    if self.figure_read_after_move is not None:
                        self.chess_game_writer.write_black_move(
                            move=f"{self.figure_read_before_move}x{self.identified_square_after_move}"
                        )
                    else:
                        self.chess_game_writer.write_black_move(
                            move=f"{self.figure_read_before_move}{self.identified_square_after_move}"
                        )
            else:
                self.chess_game_writer.write_black_move(
                    move=f"{castle}"
                )

    def __get_img_after_move(self):
        position_figure_after = cv2.subtract(
            self.current_after_move_img.copy(),
            self.current_before_move_img.copy()
        )
        position_figure_after = self.chess_color_detector.get_corrected_img_using_median_filter(position_figure_after)

        return position_figure_after

    def __get_img_before_move(self):
        position_figure_before = cv2.subtract(
            self.current_before_move_img.copy(),
            self.current_after_move_img.copy(),
        )
        position_figure_before = self.chess_color_detector.get_corrected_img_using_median_filter(position_figure_before)

        return position_figure_before

    def __set_detected_move(
            self,
            img_before,
            img_after
    ):
        img_with_detected_move = cv2.add(img_before.copy(),img_after.copy())

        with self.stacked_image_lock:
            img_with_detected_move = cv2.add(img_with_detected_move, self.stacked_image["white_corners_on_black_screen"])
            self.stacked_image["detected_move"] = img_with_detected_move

    def __set_current_before_move_img(
            self,
            color: Literal['white', 'black']
    ):

        with self.stacked_image_lock:
            img_before_move_direct_from_camera = self.stacked_image["temp_image"]

        self.current_before_move_img = self.chess_color_detector.get_img_with_chosen_mask(
                figure_mask=color,
                current_recorded_image=img_before_move_direct_from_camera
            )

    def __set_current_after_move_img(
            self,
            color: Literal['white', 'black']
    ):

        with self.stacked_image_lock:
            img_after_move_direct_from_camera = self.stacked_image["temp_image"]

        self.current_after_move_img = self.chess_color_detector.get_img_with_chosen_mask(
            figure_mask=color,
            current_recorded_image=img_after_move_direct_from_camera
        )

    def setup_window_for_images(self):
        self.window_name = get_chess_config()['main_window_name']

        monitors = get_monitors()

        if monitors:
            # main_monitor = max(monitors, key=lambda monitor: monitor.width * monitor.height)
            main_monitor = monitors[1]
            self.screen_width, self.screen_height = main_monitor.width, main_monitor.height
            cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
            cv2.setWindowProperty(self.window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            self.black_screen = np.zeros((self.screen_height, self.screen_width, 3), dtype=np.uint8)
        else:
            raise Exception("None screen")

    @staticmethod
    def __find_center_of_change(
            img
    ):
        center_elements = []
        contours = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        for found_contour in contours:
            if cv2.contourArea(found_contour) > 10:
                M = cv2.moments(found_contour)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                center_elements.append(
                    {"x": cX, "y": cY}
                )
        return center_elements

    def stack_image_on_main_window(
            self,
            image
    ):

        height, width, _ = image.shape

        start_x = (self.screen_width - width) // 2
        start_y = (self.screen_height - height) // 2

        self.black_screen[start_y:start_y + height, start_x:start_x + width] = image[:, :, :]

    def show_main_window(
            self
    ):
        cv2.imshow(self.window_name, self.black_screen)

    def set_white_and_black_detected_image(
            self,
            img_white,
            img_black
    ):
        img_mixed = img_white + img_black

        with self.stacked_image_lock:
            self.stacked_image["white_and_black_detected_image"] = img_mixed

    def __setup_camera_get_frame_process(
            self
    ):
        self.__camera_get_frame_process = multiprocessing.Process(
            target=self._run_camera_get_frame_process,
            daemon=True,
            args=(
                self.__camera_get_frame_process_event,
                self.stacked_image_lock,
            )
        )

    def __start_camera_get_frame_process(self):
        self.__camera_get_frame_process.start()
        self.__camera_get_frame_process = None  # TODO Why I must do this?

    def _run_camera_get_frame_process(
            self,
            event_frame: multiprocessing.Event(),
            lock: multiprocessing.Lock(),
    ):
        chess_camera = ChessCameraRecorder()
        init_img = chess_camera.get_image().value

        with lock:
            self.stacked_image["white_corners_on_black_screen"] = get_white_corners_on_black_screen(init_img)

        while not event_frame.is_set():

            temp_img = chess_camera.get_image().value
            with lock:
                self.stacked_image["temp_image"] = temp_img
            cv2.waitKey(1)

    def __setup_camera_display_stacked_images_process(
            self
    ):
        self.__camera_display_stacked_images_process = multiprocessing.Process(
            target=self._run_camera_display_stacked_images_process,
            daemon=True,
            args=(
                self.__camera_display_stacked_images_process_event,
                self.stacked_image_lock,
            )
        )

    def __start_camera_display_stacked_images_process(
            self
    ):
        self.__camera_display_stacked_images_process.start()
        self.__camera_display_stacked_images_process = None

    def _run_camera_display_stacked_images_process(
            self,
            event: multiprocessing.Event(),
            lock: multiprocessing.Lock(),
    ):
        self.setup_window_for_images()
        time.sleep(20)  # TODO use some multiprocessing event to wait until it wll be set
        while not event.is_set():

            with lock:
                temp_dict = self.stacked_image

            if temp_dict["temp_image"] is not None:
                if temp_dict["detected_move"] is not None:
                    stacked_images_to_show = stack_images(
                            1,
                            [temp_dict["temp_image"],
                             temp_dict["detected_move"]
                             ]
                        )
                else:
                    stacked_images_to_show = stack_images(
                            1,
                            [temp_dict["temp_image"]
                             ]
                        )

                self.stack_image_on_main_window(stacked_images_to_show)

            self.show_main_window()
            cv2.waitKey(1)


# Below code is only example to test.
# Main idea is chessFletApp client sending messages to chessServer
if __name__ == "__main__":
    game_controller = ChessGameController()
    game_controller.chess_ods_data_r_w.reset_chess_table_to_starting_position()
    time.sleep(1)
    a = input("Prepare chessboard and press enter to start game")
    game_controller.start_chess_game()
    event = input("Enter name of Event")
    white_player = input("Enter name of white player")
    black_player = input("Enter name of black player")
    game_controller.chess_game_writer.set_event_game(
        value=event
    )
    game_controller.chess_game_writer.set_white_game(
        value=white_player
    )
    game_controller.chess_game_writer.set_black_game(
        value=black_player
    )
    print("Instead of move you can type 'q' and press enter to end game")
    while True:
        move = input("Move white figure and [press enter]")
        if move != "q":
            game_controller.execute_procedure_of_move(
                color="white"
            )
        else:
            break
        move = input("Move black figure and [press enter]")
        if move != "q":
            game_controller.execute_procedure_of_move(
                color="black"
            )
        else:
            break
    result = input("Set result of game: '1-0' or '0-1' or '1/2-1/2' ")
    game_controller.end_chess_game(
        result_of_game=result
    )

