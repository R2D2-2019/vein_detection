"""this module tests the image denoising class"""
import sys
import os

ROOT_DIR = os.path.abspath(os.curdir)
sys.path.append(ROOT_DIR)
import module.vein_detection
import cv2

# The base image on which the tests will run on
base_image = cv2.imread('test/img/test_image.png')

# Call the constructor
vein_detection_class = module.vein_detection.VeinDetection(0)

# Load the pre-processed  image
test_image_clahe = cv2.imread('test/img/test_image_clahe.png')

# Call the image clahe function to create an image with CLAHE applied
image_clahe = vein_detection_class.clahe(base_image)

# Create histogram for both images
histo_test_clahe = cv2.calcHist([test_image_clahe], [0], None, [256], [0, 256])
histo_clahe = cv2.calcHist([image_clahe], [0], None, [256], [0, 256])

# Get the height, width and channels of the test image
test_shape = test_image_clahe.shape

# Get the height, width and channels of the image
shape = image_clahe.shape

def test_height():
    """this test asserts that the height of both images are equal"""
    assert test_shape[0] == shape[0]


def test_width():
    """this test asserts that the width of both images are equal"""
    assert test_shape[1] == shape[1]


def test_histogram_length():
    """this test asserts that the histogram sizes of both images are equal"""
    assert len(histo_test_clahe) == len(histo_clahe)


def test_histogram_values():
    """this test asserts that the histogram values of both images are equal"""
    for gray_value in range(len(histo_clahe)):
        assert histo_test_clahe[gray_value] == histo_clahe[gray_value]
