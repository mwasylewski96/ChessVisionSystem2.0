############################
###  EXTERNAL LIBRARIES  ###
############################
import cv2
import numpy as np

############################
###  INTERNAL LIBRARIES  ###
############################
from chessTools.chessTool import stack_images


class ChessColorDetection:























def empty(a):
    pass




cap = cv2.VideoCapture(0)

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    ret, img = cap.read()

    if not ret:
        print("Błąd odczytu klatki")
        break

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    # Zastosowanie filtru medianowego
    mask = cv2.medianBlur(mask, 21)

    imgResult = cv2.bitwise_and(img, img, mask=mask)

    imgStack = stackImages(1, [img, mask])
    cv2.imshow("Stacked Images", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zwalnianie zasobów
cap.release()
cv2.destroyAllWindows()

