import cv2
from chessTools.chessTool import get_right_camera_index, Result, is_button_pressed


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
                self.__camera = cv2.VideoCapture(temp)
            else:
                self.__camera = cv2.VideoCapture(index)

            if not self.__camera.isOpened():
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
        if self.__camera.isOpened():
            ret, img = self.__camera.read()
            if ret:
                return Result.success(img)
            else:
                return Result.error(
                    error="Image error"
                )
        else:
            return Result.error(
                error="Image error"
            )

    @staticmethod
    def show_got_img(
            image
    ):
        cv2.imshow("Got image", image)

    def show_current_img(
            self,
    ):
        try:
            result_image = self.get_image()
            if result_image.success:
                cv2.imshow("Got image", result_image.value)
                return Result.success()
            else:
                return Result.error(result_image.error)
        except Exception as err:
            message = f"Not camera detected {err}"
            print(message)
            return Result.error(message)


if __name__ == "__main__":
    camera = ChessCameraRecorder()
    if camera.error is not None:
        print(camera.error)
    else:
        while not is_button_pressed():
            camera.show_current_img()