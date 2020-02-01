from threading import Thread


class Writer(Thread):
    def __init__(self, socket, target_hostname, udp_port):
        Thread.__init__(self)
        self.socket = socket
        self.target = (target_hostname, udp_port)


    def run(self):
        while True:
            message_type = input("int or str? ") == "int"
            if message_type:
                number = int(input("What number? "))
                self.socket.sendto(bytes([number]), self.target)
            else:
                message = input("What do you want to send? ").encode("utf-8")
                self.socket.sendto(message, self.target)


class UDPWriter(Thread):
    def __init__(self, socket, target_hostname, udp_port):
        Thread.__init__(self)
        self.socket = socket
        self.target = (target_hostname, udp_port)
        self.queue = []
        print("----------- CONFIGURATION -----------")
        print(self.socket)
        print(self.target)
        print("-------------------------------------")

    def run(self):
        while True:
            if len(self.queue) > 0:
                message: bytes = self.queue.pop(0)
                if not isinstance(message, bytes):
                    continue

                self.socket.sendto(message, self.target)
