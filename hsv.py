import cv2
import numpy as np


class HSV:
    def __init__(self, trackbar_name="HSV slider"):
        self.__trackbar_name = trackbar_name
        self.__low_hsv = np.array([0, 0, 0])
        self.__max_hsv = np.array([255, 255, 255])
        self.__low_hsv_names = ["H-Min", "S-Min", "V-Min"]
        self.__max_hsv_names = ["H-Max", "S-Max", "V-Max"]
        self.__create_trackbar()

    # This function converts a given frame to the HSV color space
    # Returns the frame converted to HSV
    @staticmethod
    def __convert_to_hsv(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # This function is necessary to use the cv2.createTrackbar function
    # It does nothing in this case
    def __callback(self, x):
        pass

    # Creates the "trackbar" in which you can modify the HSV values in real-time
    def __create_trackbar(self):
        cv2.namedWindow(self.__trackbar_name)
        # Trackbar sliders for low threshold
        for name in self.__low_hsv_names:
            cv2.createTrackbar(name, self.__trackbar_name, 0, 255, self.__callback)

        # Trackbar sliders for max threshold
        for name in self.__max_hsv_names:
            cv2.createTrackbar(name, self.__trackbar_name, 255, 255, self.__callback)

    # Get the trackbar values and store them in low_hsv and max_hsv
    def __get_trackbar_values(self):
        # Low HSV values
        for i in range(0, len(self.__low_hsv_names)):
            self.__low_hsv[i] = cv2.getTrackbarPos(self.__low_hsv_names[i], self.__trackbar_name)

        # MAX HSV values
        for i in range(0, len(self.__max_hsv_names)):
            self.__max_hsv[i] = cv2.getTrackbarPos(self.__max_hsv_names[i], self.__trackbar_name)

    # Applies HSV thresholding to given frame
    # Returns the resulting frame
    def threshold_frame(self, frame):
        self.__get_trackbar_values()
        hsv_frame = self.__convert_to_hsv(frame)
        mask = cv2.inRange(hsv_frame, self.__low_hsv, self.__max_hsv)
        return cv2.bitwise_and(frame, frame, mask=mask)
