"""this module tests the hsv class"""
import sys
import os
ROOT_DIR = os.path.abspath(os.curdir)
print(str(ROOT_DIR))
sys.path.append(ROOT_DIR)
from module import hsv
import cv2
import numpy as np

# The base image on wich the tests will run on
base_image = cv2.imread('C:/ti-software/vein-detection/vein_detection/test_image.png')

# Call the constructor with pre-defined ranges.
# Note: Changing these ranges will result in a failed test, you will then need to create a new
# pre-processed image for these tests to pass.
hsv_class = hsv.HSV(low_hsv=np.array([0, 0, 36]), high_hsv=np.array([255, 82, 255]))

# Load the pre-proccessed hsv image
print(str(ROOT_DIR) + '\\test_image_hsv.png')
test_image_hsv = cv2.imread('C:/ti-software/vein-detection/vein_detection/test_image_hsv.png')

# Call the threshold frame function to create a ranged hsv image
image_hsv = hsv_class.threshold_frame(base_image)

# Create histogram for both images
histo_test_hsv = cv2.calcHist([test_image_hsv], [0], None, [256], [0, 256])
histo_hsv = cv2.calcHist([image_hsv], [0], None, [256], [0, 256])

def test_height():
    """this test asserts that the height of both images are equal"""
    test_shape = test_image_hsv.shape
    shape = image_hsv.shape
    assert test_shape[0] == shape[0]

def test_width():
    """this test asserts that the width of both images are equal"""
    test_shape = test_image_hsv.shape
    shape = image_hsv.shape
    assert test_shape[1] == shape[1]

def test_channels():
    """this test asserts that the hsv channels of both images are equal"""
    test_shape = test_image_hsv.shape
    shape = image_hsv.shape
    assert test_shape[2] == shape[2]

def test_histogram_length():
    """this test asserts that the histogram sizes of both images are equal"""
    assert len(histo_test_hsv) == len(histo_hsv)

def test_histogram_values():
    """this test asserts that the histogram values of both images are equal"""
    for gray_value in range(len(histo_hsv)):
        assert histo_test_hsv[gray_value] == histo_hsv[gray_value]

