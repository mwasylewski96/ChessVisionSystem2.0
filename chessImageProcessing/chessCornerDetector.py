import cv2
from chessCameraProcessing.chessCameraRecording import ChessCameraRecorder
from chessTools.chessTool import is_button_pressed, write_corners_to_json_file
from chessTools.chessConfig import get_chess_path_to_corners


class ChessCornerDetector:

    def __init__(self):
        self.window_name = 'Image with Coordinates'
        self.img = None
        self.current_coordinates = {"x": 0, "y": 0}
        self.saved_coordinates = []
        self.setup()

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