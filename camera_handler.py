"""Provides a class to use the basic functionality of a camera"""
import cv2
import sys


class CameraHandler:
    """ This class is to make the use of the camera easier."""
    def __init__(self, camera):
        """ The constructor.
        :param camera: the id of the camera device 0=default, 1=connected device
        """
        self.camera = cv2.VideoCapture(camera)
        self.__width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.__height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.__frame_rate = self.camera.get(cv2.CAP_PROP_FPS)
        if not self.camera.isOpened():
            print('Error opening camera.')
            sys.exit(1)

    def resize_window(self, frame, width=None, height=None):
        """ This function provides the user with keyboard commands / actions
        :param frame: frame obtained from the camera
        :param width: the width you want your output frame to be
        :param height: the height you want your output frame to be
        :return: frame with dimension width x height
        """
        (current_height, current_width) = frame.shape[:2]

        # If specified width and height are set to None, return current frame
        if width is None and height is None:
            return frame

        if width is None:
            ratio = height / float(current_height)
            dimension = (int(current_width * ratio), height)
        else:
            ratio = width / float(current_width)
            dimension = (width, int(current_height * ratio))

        resize_image = cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)
        self.__width = dimension[0]
        self.__height = dimension[1]

        return resize_image

    def exit_camera(self):
        """ When this function is called the camera will be released, and shut down
        :return: void
        """
        self.camera.release()
        cv2.destroyAllWindows()

    # this function displays the frame given as a parameter
    def get_frame(self, frame):
        """ This function will display the frame obtained from the camera when it is called
        :param frame: frame obtained from the camera
        :return: frame obtained from the camera
        """
        cv2.imshow('frame', frame)
