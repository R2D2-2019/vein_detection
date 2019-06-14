import hsv as hsv
import cv2

def main():
    img = cv2.imread("img/test_image.png")
    hsv_class = hsv.HSV()
    while True:
        frame = img.copy()
        frame = hsv_class.threshold_frame(frame)
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF is ord('q'):
            break


if __name__ == "__main__":
    main()
