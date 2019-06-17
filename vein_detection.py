import cv2
import numpy as np
import camera_handler as camera


# Main Vein Detection class
class VeinDetection:
    def __init__(self, camera_id):
        self.__camera = camera.CameraHandler(camera_id)
        self.__clahe_amount = 2

    # Canny Edge Detection step, finds the edges of the body parts and veins
    # inside the supplied frame and returns the resulted frame
    # NOTE: This function should be made private (since these functions are going to get called inside run())
    # it's public for testing purposes now.
    def canny_edge_detection(self, frame):
        return frame

    # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    # creates a better constrast between veins and the skin on supplied frame
    # returns the resulted frame
    # The frame (image) is devided into small blocks 8x8 pixels by default
    # Each of these blocks are then histogram equalized as usual
    # Contrast limiting is applied to avoid noise amplification
    # The result of this function is a side-by-side comparison between
    # a grayscaled version of the original frame (left) and one with clahe applied (right)
    # NOTE: This function should be made private (since these functions are going to get called inside run())
    # it's public for testing purposes now.
    def clahe(self, frame, amount=1):
        input_frame_grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # create a CLAHE object
        clahe_object = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

        output_frame = input_frame_grayscaled
        for __ in range(amount):
            output_frame = clahe_object.apply(output_frame)
            output_frame = self.image_denoising(output_frame)

        return output_frame

    # Image Denoising is used to remove noice from supplied frame
    # returns frame with less noise
    # NOTE: This function should be made private (since these functions are going to get called inside run())
    # it's public for testing purposes now.
    def image_denoising(self, frame):
            return frame

    # Adaptive Thresholding is used to create a black/white image from supplied frame
    # returns a black/white image
    # NOTE: This function should be made private (since these functions are going to get called inside run())
    # it's public for testing purposes now.
    def adaptive_thresholding(self, frame):
        return frame

    # this function provides the user with keyboard commands / actions
    # These commands can be helpful for debugging
    # press 's' to call show_current_frame(frame), shows current camera output frame
    # press 'q' to call exit_camera()
    # press 'v' to show a snapshot of the current display
    # press ']' to increase clahe_amount
    # press '[' to decrease clahe_amount
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

    # This is the main loop for vein detection.
    # Run this after calling the constructor
    def run(self):
        while True:
            (ret, frame) = self.__camera.camera.read()
            input_frame_grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            output_frame = self.clahe(frame, self.__clahe_amount)
            # output_frame = self.adaptive_thresholding(frame)
            # output_frame = self.canny_edge_detection(frame)
            display = np.hstack((input_frame_grayscaled, output_frame))
            cv2.imshow('Vein Detection', display)
            self.commands(frame, display)
