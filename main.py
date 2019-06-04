import display
import image_preprocessor as preprocessor

import threading
from PIL import Image
import time

import ir_camera as camera
import cv2


def millis():
    return int(round(time.time() * 1000))


def image_transformer(disp: display):
    original_image = Image.open("D:\\Images\\vein_test_image2.jpg")
    disp.change_image_left(original_image)
    disp.change_image_right(original_image)

    original_image = original_image.convert('RGB')

    time_before_gray = millis()
    gray_image = preprocessor.image_rgb_2_gray(original_image)
    time_after_gray = millis()

    time_step_to_gray = time_after_gray - time_before_gray
    print("time it took to step to gray is: {} ms".format(time_step_to_gray))

    disp.change_image_right(gray_image)

    time_before_edge = millis()
    edge_image = preprocessor.image_edge_detection(gray_image)
    time_after_edge = millis()

    time_edge_detection = time_after_edge - time_before_edge
    print("time it took to detect edges is: {} ms".format(time_edge_detection))

    disp.change_image_right(edge_image)


def camera_loop():
    cam_class = camera.Camera()
    ir_cam = cam_class.choose_camera(1)
    while True:
        (ret, frame) = ir_cam.read()
        cv2.imshow('Frame', frame)
        cam_class.commands(ir_cam, frame)


if __name__ == "__main__":
    window = display.Display(640, 480)
    worker_camera = threading.Thread(target=camera_loop)
    worker = threading.Thread(target=image_transformer, kwargs=dict(disp=window))
    worker.start()
    worker_camera.start()
