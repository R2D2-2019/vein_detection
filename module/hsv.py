"""Provides a class to return a frame in a specified hsv color range"""
import cv2
import numpy as np


class HSV:
    def __init__(self, trackbar_name="HSV slider", low_hsv = np.array([0, 0, 0]), high_hsv = np.array([255, 255, 255])):
        """ The constructor.
        :param trackbar_name: Renames the trackbar window name, can be left blank
        """
        self.__trackbar_name = trackbar_name
        self.__low_hsv = low_hsv
        self.__max_hsv = high_hsv
        self.__low_hsv_names = ["H-Min", "S-Min", "V-Min"]
        self.__max_hsv_names = ["H-Max", "S-Max", "V-Max"]
        self.__is_trackbar_enabled = False

    @staticmethod
    def __convert_to_hsv(frame):
        """ Convert to hsv, convert a specified frame to the HSV color space
        :param frame: frame obtained from the camera
        :return: frame that is converted to the HSV color space
        """
        return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    def __callback(self, x):
        """ Callback, necessary for cv2.createTrackbar, does nothing
        :param x: Can be anything
        """
        pass

    def __create_trackbar(self):
        """ Create trackbar, creates a trackbar in which you can modify the HSV values in real-time """
        cv2.namedWindow(self.__trackbar_name)
        # Trackbar sliders for low threshold
        for name in self.__low_hsv_names:
            cv2.createTrackbar(name, self.__trackbar_name, 0, 255, self.__callback)

        # Trackbar sliders for max threshold
        for name in self.__max_hsv_names:
            cv2.createTrackbar(name, self.__trackbar_name, 255, 255, self.__callback)

    def __get_trackbar_values(self):
        """ Get trackbar values, gets the values from the trackbar and stores them in low_hsv an max_hsv"""
        # Low HSV values
        for i in range(0, len(self.__low_hsv_names)):
            self.__low_hsv[i] = cv2.getTrackbarPos(self.__low_hsv_names[i], self.__trackbar_name)

        # MAX HSV values
        for i in range(0, len(self.__max_hsv_names)):
            self.__max_hsv[i] = cv2.getTrackbarPos(self.__max_hsv_names[i], self.__trackbar_name)

    # The trackbar will be spawned if this function is called, it can only be called once
    # Since calling it again will cause another trackbar to spawn and will result in undefined behaviour
    # This is countered by the if not statement
    def enable_trackbar(self):
        """ Enable trackbar, Calls the create trackbar function and makes sure it doesn't spawn multiple """
        if not self.__is_trackbar_enabled:
            self.__is_trackbar_enabled = True
            self.__create_trackbar()

    def threshold_frame(self, frame):
        """ Treshold frame, applies image thresholding on the given frame
        :param frame: frame obtained from the camera
        :return: Returns the frame which holds only the colors in the low and max hsv range
        """
        if self.__is_trackbar_enabled:
            self.__get_trackbar_values()
        hsv_frame = self.__convert_to_hsv(frame)
        mask = cv2.inRange(hsv_frame, self.__low_hsv, self.__max_hsv)
        return cv2.bitwise_and(frame, frame, mask=mask)
