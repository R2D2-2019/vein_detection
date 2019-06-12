import cv2
import numpy as np
import camera_handler as camera


# Main Vein Detection class
class VeinDetection:
    def __init__(self, camera_id):
        self.__camera = camera.CameraHandler(camera_id)

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
    # NOTE: This function should be made private (since these functions are going to get called inside run())
    # it's public for testing purposes now.
    def clahe(self, frame):
        input_frame_grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # create a CLAHE object
        clahe_object = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        output_frame = clahe_object.apply(input_frame_grayscaled)
        result = np.hstack((input_frame_grayscaled, output_frame))
        return result

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
    # press 's' to call show_current_frame(frame)
    # press 'q' to call exit_camera()
    def commands(self, frame):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.__camera.exit_camera()
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            self.__camera.show_current_frame(frame)
        elif cv2.waitKey(1) & 0xFF == ord('v'):
            cv2.imshow('Vein Detection', self.clahe(frame))

    # This is the main loop for vein detection.
    # Run this after calling the constructor
    def run(self):
        return
