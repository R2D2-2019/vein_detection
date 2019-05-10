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


def commands(cap, frame):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit_cam(cap)
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        snapshot = frame.copy()
        cv2.imshow('Snapshot', snapshot)
        get_pixel_values(snapshot)


def get_pixel_values(snap):
    height = snap.shape[0]
    width = snap.shape[1]
    pixel_values = [[[0 for n in range(3)] for row in range(width)] for col in range(height)]
    for y in range(height):
        for x in range(width):
            pixel_values[y][x][0] = snap[y, x, 0]
            pixel_values[y][x][1] = snap[y, x, 1]
            pixel_values[y][x][2] = snap[y, x, 2]
    return pixel_values


def main():
    cam = choose_camera(1)
    while(True):
        (ret, frame) = cam.read()
        cv2.imshow('Frame', frame)
        commands(cam, frame)


main()
