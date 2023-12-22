import cv2
import json

from chessCameraProcessing.chessCameraRecording import ChessCameraRecorder
from chessTools.chessTool import stack_images, is_button_pressed
from chessTools.chessConfig import get_chess_path_to_corners


class ChessCalibrator:

    @staticmethod
    def draw_calibrate_rect(img, square, left_up_corner_xy, right_down_corner_xy):
        x = left_up_corner_xy["x"] + (right_down_corner_xy["x"]-left_up_corner_xy["x"])//8
        y = (left_up_corner_xy["y"] + right_down_corner_xy["y"])//2 - (left_up_corner_xy["y"] - right_down_corner_xy["y"])//4
        cv2.rectangle(img, (left_up_corner_xy["x"], left_up_corner_xy["y"]), (right_down_corner_xy["x"], right_down_corner_xy["y"]), (255, 0, 0), 2)
        cv2.putText(img, square, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))


if __name__ == "__main__":
    with open(get_chess_path_to_corners(), 'r') as file:
        corners = json.load(file)
    camera = ChessCameraRecorder()
    if camera.error is not None:
        print(camera.error)
    else:
        chessCalibrator = ChessCalibrator()
        while not is_button_pressed():
            result_current_image = camera.get_image()
            if result_current_image.success:
                square = "c2"
                chessCalibrator.draw_calibrate_rect(
                    img=result_current_image.value,
                    square=square,
                    left_up_corner_xy=corners[square[0]+str(int(square[1])+1)],
                    right_down_corner_xy=corners["d"+square[1]],
                )
                cv2.imshow("Calibration img", result_current_image.value)
