import camera_handler as camera
import cv2
import time


def main():
    cam_class = camera.CameraHandler(0)
    # wait for camera to warm up
    time.sleep(1)
    while True:
        (ret, frame) = cam_class.camera.read()
        cv2.imshow('Frame', frame)
        cam_class.commands(frame)


if __name__ == "__main__":
    main()
