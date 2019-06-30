#!/usr/bin/python
import cv2
import numpy as np
from scipy.stats import itemfreq

outputArray = [0]

LEFT_NUM = 1 
RIGHT_NUM = 2 
FORWARD_NUM = 3
FORWARD_AND_RIGHT =4
FORWARD_AND_LEFT = 5
STOP_NUM = 6
index = 0 

# I took this solution from:
# https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv#43111221
def get_dominant_color(image, n_colors):
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    flags, labels, centroids = cv2.kmeans(
        pixels, n_colors, None, criteria, 10, flags)
    palette = np.uint8(centroids)
    return palette[np.argmax(itemfreq(labels)[:, -1])]


clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv2.VideoCapture(0)  # Put here ID of your camera (/dev/videoN)
cv2.namedWindow('camera')
cv2.setMouseCallback('camera', onMouse)

# Read and process frames in loop
success, frame = cameraCapture.read()
while success and not clicked:
    cv2.waitKey(1)
    success, frame = cameraCapture.read()

    # Conversion to gray is required to speed up calculations, we would detect
    # the same circles in BGR and GRAY anyways.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Then we blur the entire frame to prevent accidental false circle
    # detections
    img = cv2.medianBlur(gray, 37)
    # Finally, OpenCV built-in algorithm searching for circles. Arguments are a
    # bit tricky. The most useful are minDist (equals to 50 in this example)
    # and param{1,2}. First one represents distance between centers of detected
    # circles so we never have multiple circles in one place. However,
    # increasing this parameter too much may prevent detection of some circles.
    # Increasing param1 increases count of detected circles. Increasing param2
    # drops more false circles.
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,
                              1, 50, param1=120, param2=40)

    if not circles is None:
        circles = np.uint16(np.around(circles))
        # Filter the biggest circle, we don't want far signs to be detected
        # instead of close ones.
        max_r, max_i = 0, 0
        for i in range(len(circles[:, :, 2][0])):
            if circles[:, :, 2][0][i] > 50 and circles[:, :, 2][0][i] > max_r:
                max_i = i
                max_r = circles[:, :, 2][0][i]
        x, y, r = circles[:, :, :][0][max_i]
        # This check prevents program crash when trying to index list out of
        # its range. We actually cut a square with the whole circle inside.
        if y > r and x > r:
            square = frame[y-r:y+r, x-r:x+r]

            dominant_color = get_dominant_color(square, 2)
            if dominant_color[2] > 100:
                # Stop sign is red, so we check if there is a lot of red color
                # in circle.
                # print("STOP")
                outputArray.pop()
                outputArray.append(STOP_NUM)

            elif dominant_color[0] > 80:
                # Other signs are blue.

                # Here we cut 3 zones from the circle, then count their
                # dominant color and finally compare.
                zone_0 = square[square.shape[0]*3//8:square.shape[0]
                                * 5//8, square.shape[1]*1//8:square.shape[1]*3//8]
                zone_0_color = get_dominant_color(zone_0, 1)

                zone_1 = square[square.shape[0]*1//8:square.shape[0]
                                * 3//8, square.shape[1]*3//8:square.shape[1]*5//8]
                zone_1_color = get_dominant_color(zone_1, 1)

                zone_2 = square[square.shape[0]*3//8:square.shape[0]
                                * 5//8, square.shape[1]*5//8:square.shape[1]*7//8]
                zone_2_color = get_dominant_color(zone_2, 1)

                if zone_1_color[2] < 60:
                    if sum(zone_0_color) > sum(zone_2_color):
                        # print("LEFT")
                        outputArray.pop()
                        outputArray.append(LEFT_NUM)

                    else:
                        # print("RIGHT")
                        outputArray.pop()
                        outputArray.append(RIGHT_NUM)
                else:
                    if sum(zone_1_color) > sum(zone_0_color) and sum(zone_1_color) > sum(zone_2_color):
                        # print("FORWARD")
                        outputArray.pop()
                        outputArray.append(FORWARD_NUM)
                    elif sum(zone_0_color) > sum(zone_2_color):
                        # print("FORWARD AND LEFT")
                        outputArray.pop()
                        outputArray.append(FORWARD_AND_LEFT)
                    else:
                        # print("FORWARD AND RIGHT")
                        outputArray.pop()
                        outputArray.append(FORWARD_AND_RIGHT)

            else:
                print("N/A")

        # Draw all detected circles on the screen
        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
            print (outputArray)
        cv2.imshow('camera', frame)

cv2.destroyAllWindows()
cameraCapture.release()
