from threading import Thread


class SerialReader(Thread):
    def __init__(self, serial):
        Thread.__init__(self)
        self.serial = serial

    def run(self):
        while True:
            data = self.serial.read()
            print(f"Received: {data} from ROV")
