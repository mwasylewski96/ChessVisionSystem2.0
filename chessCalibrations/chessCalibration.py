# import cv2
# import numpy as np
#
# from chessCameraProcessing.chessCameraRecording import ChessCameraRecorder
# from chessTools.chessTool import stack_images, is_button_pressed
#
# def draw_calibrate_rect(img):
#     cv2.rectangle(img, (640, 360), (715, 435), (255, 0, 0), 2)
#     cv2.putText(img, "e4", (640, 420), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0))
#
#
# def detect_corners(img):
#     grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     mycorners = cv2.goodFeaturesToTrack(grayimg, 250, 0.2, 20)
#     mycorners = np.int0(mycorners)
#     return mycorners
#
#
# def is_on_board(x,y):
#     return x < 900 and x > 320 and y > 70 and y < 680
#
#
# def draw_corner_marks(corners,img):
#     for corner in corners:
#         x, y = corner.ravel()
#         if is_on_board(x,y):
#             # coordinates.append([x, y])
#             img = cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
#
#     return img
#
# def is_calibration_button_pressed():
#     a = cv2.waitKey(1) & 0xFF == ord('r')
#     return a
#
# def calibration(img):
#     if is_calibration_button_pressed():
#         draw_calibrate_rect(img)
#
# if __name__ == "__main__":
#     camera = ChessCameraRecorder()
#     if camera.error is not None:
#         print(camera.error)
#     else:
#         while not is_button_pressed():
#             result_current_image = camera.get_image()
#             if result_current_image.success:
#                 img = result_current_image.value
#                 corners = detect_corners(img)
#                 img_with_detected_corners = draw_corner_marks(corners, img)
#
#                 all_images = stack_images(1, [img_with_detected_corners])
#
#                 cv2.imshow("Stacked Images", all_images)
