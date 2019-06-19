import vein_detection as vd
import time


def main():
    vd_class = vd.VeinDetection(1)

    # wait for camera to warm up
    time.sleep(1)
    vd_class.run()


if __name__ == "__main__":
    main()