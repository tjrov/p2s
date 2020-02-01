from threading import Thread


class Reader(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
        self.dashboard = None

    def run(self):
        while True:
            data, address = self.socket.recvfrom(1024)
            if self.dashboard is None:
                print("Waiting for dashboard object.")
                continue
            self.dashboard.update_widget(
                "PiConsoleWidget", {"log": f"Received: {data} from {address}"}
            )
