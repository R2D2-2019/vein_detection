import display
import time
import threading
from PIL import Image

def swapper(display):
    imageIndex = False
    image1 = Image.open("D:\\Images\\testImage.png")
    image2 = Image.open("D:\\Images\\testImage2.png")
    display.changeImageRight(image1)

    while (True):
        if (imageIndex):
            display.changeImageLeft(image1)
            imageIndex = False
        else:
            display.changeImageLeft(image2)
            imageIndex = True
        time.sleep(1)



window = display.Display(300, 291)

#Create workers that work from separate thread
worker1 = threading.Thread(target=swapper, kwargs=dict(display=window))
worker1.start()

window.startWindowLoop()