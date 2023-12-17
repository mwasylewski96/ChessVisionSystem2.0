import cv2
from chessTools.chessTool import get_right_camera_index


class ChessCameraRecorder:

    def __init__(
            self
    ):
        self.error = None
        try:
            print("Initialising camera ...")
            index = get_right_camera_index()
            if index is None:
                raise cv2.error(f"Camera not found! index = {index}")
            if index == 2:
                temp = 0
                self.camera = cv2.VideoCapture(temp)
            else:
                self.camera = cv2.VideoCapture(index)

            if not self.camera.isOpened():
                if index == 2:
                    error_message = "Camera not found! Probably on Linux system"
                    raise cv2.error(error_message)

        except cv2.error as cv_err:
            self.error = f"Error with initialising camera ! {cv_err}"

        except Exception as err:
            self.error = f"Other error with camera! {err}"

    def get_image(
            self
    ):
        if self.camera.isOpened():
            ret, img = self.camera.read()
            if ret:
                return img
            else:
                return None
        else:
            return None

    @staticmethod
    def show_got_img(
            image
    ):
        cv2.imshow("Got image", image)

    def show_current_img(
            self,
    ):
        cv2.imshow("Got image", self.get_image())


if __name__ == "__main__":
    camera = ChessCameraRecorder()
    if camera.error is not None:
        print(camera.error)
    else:
        for _ in range(10000):
            camera.show_current_img()
            cv2.waitKey(1)
