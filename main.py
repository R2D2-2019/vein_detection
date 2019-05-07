import cv2

def quit(cap):
    cap.release()
    cv2.destroyAllWindows()

def choose_camera(camera):
    cap = cv2.VideoCapture(camera)
    if not capture.isOpened():
        raise RuntimeError('Error opening camera.')
    return cap

def capture(cap):
    while(True):
        (ret, frame) = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            quit(cap)
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            snapshot = frame.copy()
            cv2.imshow('Snapshot', snapshot)


def main():
    camera = choose_camera(1)
    capture(camera)

main()
