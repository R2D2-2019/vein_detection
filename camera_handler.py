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

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def resize_window(self, image, width=None, height=None):
        (current_height, current_width) = image.shape[:2]

        # If specified width and height is set to none, return current image
        if width is None and height is None:
            return image

        if width is None:
            ratio = height / float(current_height)
            dimension = (int(current_width * ratio), height)
        else:
            ratio = width / float(current_width)
            dimension = (width, int(current_height * ratio))

        resize_image = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
        self.__width = dimension[0]
        self.__height = dimension[1]

        return resize_image

    def exit_cam(self):
        self.camera.release()
        cv2.destroyAllWindows()
        sys.exit(0)

    def snap_shot(self, frame):
        snapshot = frame.copy()
        cv2.imshow('Snapshot', snapshot)

    def commands(self, frame):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.exit_cam()
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            self.snap_shot(frame)
