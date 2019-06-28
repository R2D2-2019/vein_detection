from module import vein_detection
import time


def main():
    vd_class = vein_detection.VeinDetection(0)

    # wait for camera to warm up
    time.sleep(1)
    vd_class.run()


if __name__ == "__main__":
    main()
