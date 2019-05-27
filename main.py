import display
import image_preprocessor as preprocessor

import threading
from PIL import Image
import time

millis = lambda: int(round(time.time() * 1000))

def imageTransformer(display: display):
    originalImage = Image.open("D:\\Images\\vein_test_image2.jpg")
    display.changeImageLeft(originalImage)
    display.changeImageRight(originalImage)

    originalImage = originalImage.convert('RGB')

    timeBeforeGray = millis()
    grayImage = preprocessor.image_rgb_2_gray(originalImage)
    timeAfterGray = millis()

    timeStepToGray = timeAfterGray - timeBeforeGray
    print("time it took to step to gray is: {} ms".format(timeStepToGray))

    display.changeImageRight(grayImage)

    timeBeforeEdge = millis()
    edgeImage = preprocessor.image_edge_detection(grayImage)
    timeAfterEdge = millis()

    timeEdgeDetection = timeAfterEdge - timeBeforeEdge
    print("time it took to detect edges is: {} ms".format(timeEdgeDetection))


    display.changeImageRight(edgeImage)

window = display.Display(640, 480)

worker = threading.Thread(target=imageTransformer, kwargs=dict(display=window))
worker.start()

window.startWindowLoop()