import cv2
import numpy as np


def exit_cam(cap):
    cap.release()
    cv2.destroyAllWindows()


def choose_camera(camera):
    cap = cv2.VideoCapture(camera)
    if not cap.isOpened():
        raise RuntimeError('Error opening camera.')
    return cap


def snap(cap):
    (ret, frame) = cap.read()
    snapshot = np.zeros(frame.shape, dtype=np.uint8)
    cv2.imshow('Snapshot', snapshot)

    color_array = np.zeros((80, 250, 3), dtype=np.uint8)
    cv2.imshow('Color', color_array)


def commands(cap, frame):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit_cam(cap)
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        snapshot = frame.copy()
        cv2.imshow('Snapshot', snapshot)


def main():
    camera = choose_camera(1)
    while(True):
        (ret, frame) = camera.read()
        cv2.imshow('Frame', frame)
        commands(camera, frame)


main()
