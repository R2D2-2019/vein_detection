import cv2
import sys


class CameraHandler:

    def __init__(self, camera):
        self.__width = None
        self.__height = None
        self.__frame_rate = None
        self.camera = cv2.VideoCapture(camera)
        if not self.camera.isOpened():
            print('Error opening camera.')
            sys.exit(1)

    # This function returns the camera output width (int)
    def get_camera_width(self):
        return self.__width

    # This function returns the camera output height (int)
    def get_camera_height(self):
        return self.__height

    # With this function you can resize the output window
    # frame is the output from the camera
    # width and height (int) can be set and are None by default
    def resize_window(self, frame, width=None, height=None):
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

    # When this function is called the camera will be released, and shut down.
    # Might need to change sys.exit(0) since in the future you might not want
    # to close the entire application when closing the camera.
    def exit_camera(self):
        self.camera.release()
        cv2.destroyAllWindows()
        sys.exit(0)

    # This function returns a frame from the camera at the point this function is called
    def get_current_frame(self, frame):
        return frame.copy()

    # this function displays the frame given as a parameter
    def show_current_frame(self, frame):
        cv2.imshow('frame', self.get_current_frame(frame))
