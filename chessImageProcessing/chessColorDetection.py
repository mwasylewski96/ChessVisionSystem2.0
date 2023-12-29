############################
###  EXTERNAL LIBRARIES  ###
############################
import cv2
import numpy as np
from typing import Literal
############################
###  INTERNAL LIBRARIES  ###
############################
from chessTools.chessTool import stack_images, is_button_pressed
from chessTools.chessConfig import get_chess_calibration_config
from chessCameraProcessing.chessCameraRecording import ChessCameraRecorder
from chessImageProcessing.chessCornerDetector import load_chess_corners


class ChessColorDetector:

    def __init__(self):
        self.img_hsv = None
        chess_figures_config = get_chess_calibration_config()
        self.white_config = chess_figures_config["green"]
        self.black_config = chess_figures_config["blue"]

    def get_images_on_one_frame(
            self,
            current_recorded_image
    ):
        self.img_hsv = cv2.cvtColor(current_recorded_image, cv2.COLOR_BGR2HSV)

        white_img_result = self.get_img_with_chosen_mask(
            figure_mask="white"
        )

        black_img_result = self.get_img_with_chosen_mask(
            figure_mask="black"
        )

        both_white_blacks = white_img_result + black_img_result

        all_images_on_frame = stack_images(
            1,
            [current_recorded_image,both_white_blacks],
        )

        return all_images_on_frame

    def get_img_with_chosen_mask(
            self,
            figure_mask: Literal['white', 'black'],
            current_recorded_image=None
    ):
        if figure_mask == "white":
            config_to_process = self.white_config
        elif figure_mask == "black":
            config_to_process = self.black_config
        else:
            return None

        lower = np.array([
            config_to_process['hue_min'],
            config_to_process['sat_min'],
            config_to_process['val_min']
        ])

        upper = np.array([
            config_to_process['hue_max'],
            config_to_process['sat_max'],
            config_to_process['val_max']
        ])

        if current_recorded_image is not None:
            current_image_hsv = cv2.cvtColor(current_recorded_image, cv2.COLOR_BGR2HSV)
        else:
            current_image_hsv = self.img_hsv

        mask = cv2.inRange(current_image_hsv, lower, upper)
        # Median filter
        mask = cv2.medianBlur(mask, 21)
        cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        return mask

    @staticmethod
    def get_corrected_img_using_median_filter(
            img
    ):
        ret_img = cv2.medianBlur(img, 21)
        return ret_img


if __name__ == "__main__":
    camera = ChessCameraRecorder()
    if camera.error is not None:
        print(camera.error)
    else:
        color_frame_detector = ChessColorDetector()
        while not is_button_pressed():
            result_current_image = camera.get_image()
            if result_current_image.success:
                all_images = color_frame_detector.get_images_on_one_frame(
                    result_current_image.value
                )
                # white_image = color_frame_detector.get_img_with_chosen_mask(
                #     figure_mask="white",
                #     current_recorded_image=result_current_image.value
                # )
                cv2.imshow("Stacked Images", all_images)


# def empty(a):
#     pass
#
#
#
#
# cap = cv2.VideoCapture(0)
#
# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars", 640, 240)
# cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
# cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
# cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
# cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
# cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
# cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
#
# while True:
#     ret, img = cap.read()
#
#     if not ret:
#         print("Błąd odczytu klatki")
#         break
#
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
#
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(imgHSV, lower, upper)
#
#     # Zastosowanie filtru medianowego
#     mask = cv2.medianBlur(mask, 21)
#
#     imgResult = cv2.bitwise_and(img, img, mask=mask)
#
#     imgStack = stackImages(1, [img, mask])
#     cv2.imshow("Stacked Images", imgStack)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Zwalnianie zasobów
# cap.release()
# cv2.destroyAllWindows()