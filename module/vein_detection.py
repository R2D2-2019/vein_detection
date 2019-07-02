"""Provides a class to detect veins in an image"""
import cv2
import numpy as np
from modules.vein_detection.module.camera_handler import CameraHandler
from modules.vein_detection.module.hsv import HSV

class VeinDetection:
    """ This class is used to give a good as possible representation
    of the veins on a body part, using the input from an IR-camera device."""
    def __init__(self, camera_id):
        """ The constructor.
        :param camera_id: the id of the camera device 0=default, 1=connected device
        """
        self.__camera = CameraHandler(camera_id)
        self.__clahe_amount = 2
        self.__hsv = HSV()

    def canny_edge_detection(self, frame):
        """ Canny Edge Detection, find the edges of objects in an image
        Canny Edge Detection step, finds the edges of the body parts and veins
        inside the supplied frame and returns the resulted frame
        Threshold values are the minimum and maximum values that are compared in the canny edge algorithm.
        The difference between the two is how mow sensitive your result will be.
        A lower gap means less edges might be detected. Vice versa.
        :param frame: frame obtained from the camera
        :return: frame with canny edge detection applied
        """
        return cv2.Canny(frame, threshold1=100, threshold2=200)

    def clahe(self, frame, amount=1):
        """ Contrast Limited Adaptive Histogram Equalization, enhance the contrast in an image
        CLAHE (Contrast Limited Adaptive Histogram Equalization)
        creates a better constrast between veins and the skin on supplied frame
        returns the resulted frame
        The frame (image) is devided into small blocks 8x8 pixels by default
        Each of these blocks are then histogram equalized as usual
        Contrast limiting is applied to avoid noise amplification
        The result of this function is a side-by-side comparison between
        a grayscaled version of the original frame (left) and one with clahe applied (right)
        :param frame: frame obtained from the camera
        :param amount: amount of times you want to apply clahe to the frame
        :return: frame with clahe applied
        """
        input_frame_grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # create a CLAHE object
        clahe_object = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

        output_frame = input_frame_grayscaled
        for __ in range(amount):
            output_frame = clahe_object.apply(output_frame)
            output_frame = self.image_denoising(output_frame)

        return output_frame


    def image_denoising(self, frame, kernel_size=5):
        """ Image denoising is used to remove noise from supplied frame
        This implementation is primarily used to remove salt and pepper noise after CLAHE is used on a image
        The parameter kernel_size is used to determine the amount of pixels used for the kernel in the median blur
        A larger kernel means more pixels are used in the calculation but the image could become more blurry
        Returns frame with less noise
        :param frame: frame obtained from the camera
        :param kernel_size: the amount of pixels used for the kernel in the median blur
        :return: frame with median blur applied
        """
        return cv2.medianBlur(frame, kernel_size)


    def adaptive_thresholding(self, frame):
        """ Adaptive thresholding is used to create a black/white image in which the veins can be clearly distinguished
        from the skin.
        Our implementation of adaptive thresholding uses Otsu's binarization.
        With Otsu's binarization the threshold in an image gets calculated so that the thresholding works on every image.
        Instead of getting the best threshold by trial and error Otsu's method can calculate the best threshold.
        The parameter 0 is the threshold value. This value is left at 0 because Otsu is used to calculate the threshold.
        The parameter 255 is the gray value the parts of the image get when they are above the threshold.
        THRESH_BINARY makes everything under the threshold black (0)
        and everything above the threshold the parameter color in this case 255.
        THRESH_OTSU is used to calculate the best threshold value.
        :param frame: frame obtained from the camera
        :return: frame in black/white
        """
        return cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]


    def commands(self, frame, display):
        """ this function provides the user with keyboard commands / actions
        These commands can be helpful for debugging
        press 's' to call show_current_frame(frame), shows current camera output frame
        press 'q' to call exit_camera()
        press 'v' to show a snapshot of the current display
        press ']' to increase clahe_amount
        press '[' to decrease clahe_amount
        press 'h' to spawn the HSV slider
        :param frame: frame obtained from the camera
        :param display: camera stream
        :return: void
        """
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.__camera.exit_camera()
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            self.__camera.get_frame(frame)
        elif cv2.waitKey(1) & 0xFF == ord('v'):
            cv2.imshow('Screenshot', display)
        elif cv2.waitKey(1) & 0xFF == ord('['):
            if self.__clahe_amount > 1:
                self.__clahe_amount -= 1
        elif cv2.waitKey(1) & 0xFF == ord(']'):
            self.__clahe_amount += 1
        elif cv2.waitKey(1) & 0xff == ord('h'):
            self.__hsv.enable_trackbar()

    # This is the main loop for vein detection.
    # Run this after calling the constructor
    def run(self):
        """ When this function is called, the main loop for vein detection will be executed
        :return: void
        """
        while True:
            (ret, frame) = self.__camera.camera.read()
            frame = self.__hsv.threshold_frame(frame)
            input_frame_grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            output_frame_clahe = self.clahe(frame, self.__clahe_amount)
            output_frame_adpt = self.adaptive_thresholding(output_frame_clahe)
            display = np.hstack((input_frame_grayscaled, output_frame_clahe, output_frame_adpt))
            cv2.imshow('Vein Detection', display)
            self.commands(frame, display)
