from time import sleep
from threading import Thread


class DebugWriter(Thread):

    def __init__(self, serial):
        Thread.__init__(self)
        self.serial = serial

    def run(self):
        while True:
            type = input("int or str? ") == "int"
            if type == "int":
                num = input("number? ")
                byte = bytes([num])
                self.serial.write(byte)
            else:
                byte = input("write? ").encode('utf-8')
                self.serial.write(byte)


class SerialWriter(Thread):

    def __init__(self, serial):
        Thread.__init__(self)
        self.serial = serial
        self.queue = []

    def run(self):
        while True:
            if len(self.queue) > 0:
                packet = self.queue.pop(0)
                for byte in packet.bytes:
                    self.serial.write(byte)
                sleep(1)
