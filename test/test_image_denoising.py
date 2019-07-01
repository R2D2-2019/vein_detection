"""this module tests the image denoising class"""
from modules.vein_detection.module.vein_detection import VeinDetection
import cv2

# WARNING: Any big changes in the algorithm will result in a failed test
# in this case you will need to create a new pre-processed image in order for the test to pass
# Load the pre-processed  image
test_image_denoised = cv2.imread('test/img/test_image_denoised.png')

# The base image on which the tests will run on
base_image = cv2.imread('test/img/test_image.png')

# Call the constructor
vein_detection_class = VeinDetection(0)

# Call the image denoising function to create a denoised image
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
