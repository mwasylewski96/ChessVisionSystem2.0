import cv2

cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

while True:
    succes, img = cap.read()
    cv2.imshow("VIDEOKUWRWA", img)
    cv2.waitKey(1)
# import cv2
#
#
# def CameraIndexes():
#     # Cam indexes limit, that you would like to check? .
#     index = 0
#     arr = []
#     iter_idx = 10
#     while iter_idx > 0:
#         cap = cv2.VideoCapture(index)
#         if cap.read()[0]:
#             arr.append(index)
#             cap.release()
#         index += 1
#         iter_idx -= 1
#     return arr


print("\n\nCamera Indexes: ", CameraIndexes())