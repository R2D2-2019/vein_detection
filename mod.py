from client.comm import BaseComm
from common.frame_enum import FrameType


class Module:
    def __init__(self, comm: BaseComm):
        self.comm = comm
        self.comm.listen_for([FrameType.ACTIVITY_LED_STATE])

    def process(self):
        while self.comm.has_data():
            frame = self.comm.get_data()

            if frame.request:
                continue

            values = frame.get_data()

            if values[0]:
                print("The LED is ON")
            else:
                print("The LED is OFF")

    def stop(self):
        self.comm.stop()