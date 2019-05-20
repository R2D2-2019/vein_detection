import display
import image_preprocessor as preprocessor

import time
import threading
from PIL import Image


window = display.Display(640, 480)

originalImage = Image.open("D:\\Images\\vein_test_image.jpg")
originalImage = originalImage.convert('RGB')
grayImage = preprocessor.image_rgb_2_gray(originalImage)
edgeImage = preprocessor.image_edge_detection(grayImage)

window.changeImageLeft(originalImage)
window.changeImageRight(edgeImage)

window.startWindowLoop()