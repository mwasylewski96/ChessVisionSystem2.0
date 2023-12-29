import cv2
import numpy as np
import json
from chessCameraProcessing.chessCameraRecording import ChessCameraRecorder
from chessTools.chessTool import is_button_pressed, write_corners_to_json_file
from chessTools.chessConfig import get_chess_path_to_corners


def load_chess_corners():
    with open(get_chess_path_to_corners(), 'r') as file:
        corners = json.load(file)
    return corners


def get_point_or_points_board(
        center_elements
):
    points_on_board = []
    corners = load_chess_corners()
    for point in center_elements:
        if corners["a1"]["x"] < point["x"] < corners["i1"]["x"] and \
            corners["a1"]["y"] > point["y"] > corners["i9"]["y"]:
            points_on_board.append({
                'x': point["x"],
                "y": point["y"]
            })
    return points_on_board


def get_white_corners_on_black_screen(
        init_img
):
    height, width, _ = init_img.shape
    image = np.zeros((height, width), dtype=np.uint8)
    corners = load_chess_corners()
    for corner, coordinates in corners.items():
        x, y = coordinates["x"], coordinates["y"]
        cv2.circle(image, (x, y), 3, 255, -1)

    corners = load_chess_corners()
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 0.7
    font_thickness = 2
    font_color = 255
    text_letters = "ABCDEFGH"
    small_letters = text_letters.lower() + "i"
    it = 0
    for _ in range(8):
        point1 = [corners[f"{small_letters[it]}1"]["x"], corners[f"{small_letters[it]}1"]["y"]]
        point2 = [corners[f"{small_letters[it+1]}1"]["x"], corners[f"{small_letters[it+1]}1"]["y"]]
        average_point = ((point1[0] + point2[0]) // 2, (point1[1] + point2[1]) // 2)
        cv2.putText(image, text_letters[it], (average_point[0] - 10, average_point[1] + 25), font, font_size, font_color,
                font_thickness)
        it += 1
    it = 0
    for _ in range(8):
        point1 = [corners[f"a{it+1}"]["x"], corners[f"a{it+1}"]["y"]]
        point2 = [corners[f"a{it+2}"]["x"], corners[f"a{it+2}"]["y"]]
        average_point = ((point1[0] + point2[0]) // 2, (point1[1] + point2[1]) // 2)
        cv2.putText(image, str(it+1), (average_point[0] - 30, average_point[1] + 10), font, font_size, font_color,
                font_thickness)
        it += 1

    return image


class ChessCornerDetector:

    def __init__(self):
        self.window_name = 'Image with Coordinates'
        self.img = None
        self.current_coordinates = {"x": 0, "y": 0}
        self.saved_coordinates = []
        # self.setup()

    def setup(self):
        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.on_mouse_event)

    def set_current_image(
            self,
            img
    ):
        self.img = img

    def on_mouse_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            self.current_coordinates["x"] = x
            self.current_coordinates["y"] = y
        if event == cv2.EVENT_LBUTTONDOWN:
            self.current_coordinates["x"] = x
            self.current_coordinates["y"] = y
            if not len(self.saved_coordinates) == 81:
                self.saved_coordinates.append([x,y])
                if len(self.saved_coordinates) == 81:
                    print(self.saved_coordinates)
                    write_corners_to_json_file(
                        corners=self.saved_coordinates,
                        path=get_chess_path_to_corners()
                    )
                    print("All Coordinates saved")

        if event == cv2.EVENT_RBUTTONDOWN:
            self.saved_coordinates = []

    def show_current_coordinates_on_image(self):
        text = f'X: {self.current_coordinates["x"]}, Y: {self.current_coordinates["y"]}'
        cv2.putText(
            self.img,
            text,
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2
        )
        if self.saved_coordinates is not []:
            self.draw_corner_marks()

        cv2.imshow(self.window_name, self.img)

    def draw_corner_marks(self):
        for x, y in self.saved_coordinates:
            cv2.circle(self.img, (x, y), 5, (255, 0, 0), -1)


if __name__ == "__main__":
    camera = ChessCameraRecorder()
    if camera.error is not None:
        print(camera.error)
    else:
        corner_detector = ChessCornerDetector()
        while not is_button_pressed():
            result_current_image = camera.get_image()
            if result_current_image.success:
                img = result_current_image.value
                corner_detector.set_current_image(img)
                corner_detector.show_current_coordinates_on_image()