import cv2
import camera_handler as camera

# Main Vein Detection class
class VeinDetection:
    def __init__(self, camera_id):
        self.__camera = camera.CameraHandler(camera_id)

    # Canny Edge Detection step, finds the edges of the body parts and veins
    # inside the supplied frame and returns the resulted frame
    # NOTE: This function should be made private later on
    def canny_edge_detection(self, frame):
        return frame

    # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    # creates a better constrast between veins and the skin on supplied frame
    # returns the resulted frame
    # NOTE: This function should be made private later on
    def clahe(self, frame):
        return frame

    # Image Denoising is used to remove noice from supplied frame
    # returns frame with less noise
    # NOTE: This function should be made private later on
    def image_denoising(self, frame):
        return frame

    # Adaptive Thresholding is used to create a black/white image from supplied frame
    # returns a black/white image
    # NOTE: This function should be made private later on
    def adaptive_thresholding(self, frame):
        return frame

    # This is the main loop for vein detection.
    # Run this after calling the constructor
    def run(self):
        return