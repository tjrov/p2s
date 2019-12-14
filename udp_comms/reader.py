from threading import Thread


class UDPReader(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket

    def run(self):
        while True:
            data, address = self.socket.recvfrom(1024)
            print(f"Received: {data} from {address}")
