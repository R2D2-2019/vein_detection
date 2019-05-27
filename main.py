import IR_camera_c as cam
import cv2

def main():
    cam_class = cam.camera_c()
    IR_cam = cam_class.choose_camera(1)
    while (True):
        (ret, frame) = IR_cam.read()
        cv2.imshow('Frame', frame)
        cam_class.commands(IR_cam, frame)


main()
