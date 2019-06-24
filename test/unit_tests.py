"""Provides a class to do unit tests on all functions"""
import unittest
import cv2
from module import vein_detection
from module import hsv
import numpy as np

""" How to do unit tests:
https://docs.python.org/3.7/library/unittest.html
"""

class UnitTest(unittest.TestCase):
    vd_class = vein_detection.VeinDetection(0)
    base_image = cv2.imread('../module/img/test_image.png')

    def test_hsv(self):
        """" When this function is called a default image (test_image.png)
        and a already processed image (test_image_hsv.png)
        gets loaded. The default image is processed by the threshold_frame function.
        The length and values of the histograms of both images get compared.
        If they are all equal then the test is a success
        """
        # Call the constructor with pre-defined ranges.
        # Note: Changing these ranges will result in a failed test, you will then need to create a new
        # pre-processed image for this test to pass.
        hsv_class = hsv.HSV(low_hsv=np.array([0, 0, 36]), high_hsv=np.array([255, 82, 255]))

        # Load the pre-proccessed hsv image
        test_image_hsv = cv2.imread('../module/img/test_image_hsv.png')

        # Call the threshold frame function to create a ranged hsv image
        image_hsv = hsv_class.threshold_frame(self.base_image)

        # Create histogram for both images
        histo_test_hsv = cv2.calcHist([test_image_hsv], [0], None, [256], [0, 256])
        histo_hsv = cv2.calcHist([image_hsv], [0], None, [256], [0, 256])

        # Check if the length of both histograms are equal to eachother
        self.assertEqual(len(histo_hsv), len(histo_test_hsv))

        # Check if the values of both histograms are equal to eachother
        for gray_value in range(len(histo_hsv)):
            self.assertEqual(histo_hsv[gray_value], histo_test_hsv[gray_value])

    def test_image_denoising(self):
        """" When this function is called a default image (test_image.png)
        and a already processed image (test_image_clahe_denoised.png)
        get loaded. The default image is processed by using clahe and denoising with default values.
        The length and values of the histograms of both images get compared.
        """

        # Load pre-processed denoised clahe image
        test_image_clahe_denoised = cv2.imread('../module/img/test_image_clahe_denoised.png')

        # Apply clahe to base image
        image_clahe = self.vd_class.clahe(self.base_image)
        # Denoise the clahe image
        image_clahe_denoised = self.vd_class.image_denoising(image_clahe)

        # Create histogram from denoised image
        histo_clahe_denoised = cv2.calcHist([image_clahe_denoised], [0], None, [256], [0, 256])
        # Create histogram from the loaded pre-processed denoised image
        histo_test_clahe_denoised = cv2.calcHist([test_image_clahe_denoised], [0], None, [256], [0, 256])

        # Check if the length of both histograms are the same
        self.assertEqual(len(histo_clahe_denoised), len(histo_test_clahe_denoised))

        # For each histogram value check if they are the same
        for gray_value in range(len(histo_clahe_denoised)):
            self.assertEqual(histo_clahe_denoised[gray_value], histo_test_clahe_denoised[gray_value])

    def test_adaptive_thresholding(self):
        pass

    def test_canny_edge(self):
        pass

    def test_clahe(self):
        """" When this function is called a default image (test_image.png)
        and a already processed image (test_image_clahe.png)
        get loaded. The default image is processed by using clahe with default values.
        The length and values of the histograms of both images get compared.
        """
        # Load pre-processed clahe test image
        test_image_clahe = cv2.imread('../module/img/test_image_clahe.png')

        # Apply clahe to base image
        image_clahe = self.vd_class.clahe(self.base_image)

        # Create histogram from clahe image
        histo_clahe = cv2.calcHist([image_clahe], [0], None, [256], [0, 256])
        # Create histogram from pre-processed clahe image
        histo_test_clahe = cv2.calcHist([test_image_clahe], [0], None, [256], [0, 256])

        # Check if the length of both histograms are the same
        self.assertEqual(len(histo_clahe), len(histo_test_clahe))

        # For each histogram value check if they are the same
        for gray_value in range(len(histo_clahe)):
            self.assertEqual(histo_clahe[gray_value], histo_test_clahe[gray_value])

if __name__ == '__main__':
    unittest.main()