"""this module tests the hsv class"""
import sys
import os

ROOT_DIR = os.path.abspath(os.curdir)
sys.path.append(ROOT_DIR)
import module.vein_detection
import cv2
import numpy as np

# The base image on wich the tests will run on
base_image = cv2.imread('test/img/test_image.png')

# Call the constructor.
vein_detection_class = module.vein_detection.VeinDetection(0)

# Load the pre-processed  image
test_image_denoised = cv2.imread('test/img/test_image_denoised.png')

# Call the image denoising frame function to create a denoised image
image_denoised = vein_detection_class.image_denoising(base_image)

# Create histogram for both images
histo_test_denoised = cv2.calcHist([test_image_denoised], [0], None, [256], [0, 256])
histo_denoised = cv2.calcHist([image_denoised], [0], None, [256], [0, 256])


def test_height():
    """this test asserts that the height of both images are equal"""
    test_shape = test_image_denoised.shape
    shape = image_denoised.shape
    assert test_shape[0] == shape[0]


def test_width():
    """this test asserts that the width of both images are equal"""
    test_shape = test_image_denoised.shape
    shape = image_denoised.shape
    assert test_shape[1] == shape[1]


def test_channels():
    """this test asserts that the hsv channels of both images are equal"""
    test_shape = test_image_denoised.shape
    shape = image_denoised.shape
    assert test_shape[2] == shape[2]


def test_histogram_length():
    """this test asserts that the histogram sizes of both images are equal"""
    assert len(histo_test_denoised) == len(histo_denoised)


def test_histogram_values():
    """this test asserts that the histogram values of both images are equal"""
    for gray_value in range(len(histo_denoised)):
        assert histo_test_denoised[gray_value] == histo_denoised[gray_value]
