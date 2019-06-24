import unittest
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
        pass

    def test_adaptive_thresholding(self):
        pass

    def test_canny_edge(self):
        pass

    def test_clahe(self):
        pass

if __name__ == '__main__':
    unittest.main()