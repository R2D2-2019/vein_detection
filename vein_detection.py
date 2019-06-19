import cv2
import numpy as np
import camera_handler as camera
import hsv as hsv


# Main Vein Detection class
class VeinDetection:
    def __init__(self, camera_id):
        self.__camera = camera.CameraHandler(camera_id)
        self.__clahe_amount = 2
        self.__hsv = hsv.HSV()

    # Canny Edge Detection step, finds the edges of the body parts and veins
    # inside the supplied frame and returns the resulted frame
    # Threshold values are the minimum and maximum values that are compared in the canny edge algorithm.
    # The difference between the two is how mow sensitive your result will be.
    # A lower gap means less edges might be detected. Vice versa.
    def __canny_edge_detection(self, frame):
        return cv2.Canny(frame, threshold1=100, threshold2=200)

    # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    # creates a better constrast between veins and the skin on supplied frame
    # returns the resulted frame
    # The frame (image) is devided into small blocks 8x8 pixels by default
    # Each of these blocks are then histogram equalized as usual
    # Contrast limiting is applied to avoid noise amplification
    # The result of this function is a side-by-side comparison between
    # a grayscaled version of the original frame (left) and one with clahe applied (right)
    def __clahe(self, frame, amount=1):
        input_frame_grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # create a CLAHE object
        clahe_object = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

        output_frame = input_frame_grayscaled
        for __ in range(amount):
            output_frame = clahe_object.apply(output_frame)
            output_frame = self.__image_denoising(output_frame)

        return output_frame

    # Image denoising is used to remove noise from supplied frame
    # This implementation is primarily used to remove salt and pepper noise after CLAHE is used on a image
    # The parameter kernel_size is used to determine the amount of pixels used for the kernel in the median blur
    # A larger kernel means more pixels are used in the calculation but the image could become more blurry
    # Returns frame with less noise
    def __image_denoising(self, frame, kernel_size=5):
        frame = cv2.medianBlur(frame, kernel_size)

        return frame

    # Adaptive Thresholding is used to create a black/white image from supplied frame
    # returns a black/white image
    def __adaptive_thresholding(self, frame):
        return frame

    # this function provides the user with keyboard commands / actions
    # These commands can be helpful for debugging
    # press 's' to call show_current_frame(frame), shows current camera output frame
    # press 'q' to call exit_camera()
    # press 'v' to show a snapshot of the current display
    # press ']' to increase clahe_amount
    # press '[' to decrease clahe_amount
    # press 'h' to spawn the HSV slider
    def commands(self, frame, display):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.__camera.exit_camera()
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            self.__camera.show_current_frame(frame)
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
        while True:
            (ret, frame) = self.__camera.camera.read()
            frame = self.__hsv.threshold_frame(frame)
            input_frame_grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            output_frame = self.__clahe(frame, self.__clahe_amount)
            display = np.hstack((input_frame_grayscaled, output_frame))
            cv2.imshow('Vein Detection', display)
            self.commands(frame, display)
