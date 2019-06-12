import camera_handler as camera
import vein_detection as vd
import cv2
import time


def main():
    cam_class = camera.CameraHandler(0)
    vd_class = vd.VeinDetection(0)

    # wait for camera to warm up
    time.sleep(1)
    while True:
        (ret, frame) = cam_class.camera.read()
        cv2.imshow('Frame', frame)
        vd_class.commands(frame)


if __name__ == "__main__":
    main()
