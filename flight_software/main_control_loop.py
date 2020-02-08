from .comms import Comms

from time import time
import re


class MainControlLoop:

    def __init__(self, config):
        self.comms = Comms(config)
        self.last_temp = -1
        self.last_gyro = -1
        self.last_depth = -1

    def execute(self):
        # TODO: after we get other sensors we need to add i2c calls to read that data in
        temperature = 0
        gyro_x, gyro_y, gyro_z = 0, 0, 0
        depth = 0
        sys_time = time()
        message, received = self.comms.read()

        t_top_left = 0
        t_top_right = 0
        t_front_left = 0
        t_front_right = 0
        t_back_left = 0
        t_back_left_right = 0

        if received and re.match(r"^GS:T:\d+;\d+;\d+;\d+;\d+;\d+;$", message) is not None:
            values = list(map(lambda x: int(x) if x != '' else 0, message.replace('GS:T:', '').split(';')))
            t_top_left = values[0]
            t_top_right = values[1]
            t_front_left = values[2]
            t_front_right = values[3]
            t_back_left = values[4]
            t_back_left_right = values[5]

        ## COMMUNICATE THESE VALUES TO FLIGHT COMPUTER

        if sys_time - self.last_depth > 5:
            self.comms.write(f"FS:D:{depth}")
            self.last_depth = sys_time

        if sys_time - self.last_temp > 10:
            self.comms.write(f"FS:TE:{temperature}")
            self.last_temp = sys_time

        if sys_time - self.last_gyro > 1:
            self.comms.write(f"FS:G:{gyro_x};{gyro_y};{gyro_z}")
            self.last_gyro = sys_time
