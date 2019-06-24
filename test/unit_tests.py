import unittest
import cv2
from module import vein_detection
from module import hsv

""" How to do unit tests:
https://docs.python.org/3.7/library/unittest.html
"""

class UnitTest(unittest.TestCase):
    vd_class = vein_detection.VeinDetection(0)
    hsv_class = hsv.HSV()

    def test_hsv(self):
        pass

    def test_image_denoising(self):
        """" When this function is called a default image (test_image.png)
        and a already processed image (test_image_clahe_denoised.png)
        get loaded. The default image is processed by using clahe and denoising with default values.
        The length and values of the histograms of both images get compared.
        """
        image = cv2.imread('../module/img/test_image.png')
        test_image_clahe_denoised = cv2.imread('../module/img/test_image_clahe_denoised.png')

        image_clahe = self.vd_class.clahe(image)
        image_clahe_denoised = self.vd_class.image_denoising(image_clahe)

        histo_clahe_denoised = cv2.calcHist([image_clahe_denoised], [0], None, [256], [0, 256])
        histo_test_clahe_denoised = cv2.calcHist([test_image_clahe_denoised], [0], None, [256], [0, 256])

        self.assertEqual(len(histo_clahe_denoised), len(histo_test_clahe_denoised))

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
        image = cv2.imread('../module/img/test_image.png')
        test_image_clahe = cv2.imread('../module/img/test_image_clahe.png')

        image_clahe = self.vd_class.clahe(image)

        histo_clahe = cv2.calcHist([image_clahe], [0], None, [256], [0, 256])
        histo_test_clahe = cv2.calcHist([test_image_clahe], [0], None, [256], [0, 256])

        self.assertEqual(len(histo_clahe), len(histo_test_clahe))

        for gray_value in range(len(histo_clahe)):
            self.assertEqual(histo_clahe[gray_value], histo_test_clahe[gray_value])

if __name__ == '__main__':
    unittest.main()