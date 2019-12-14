from threading import Thread


class UDPDebugWriter(Thread):
    def __init__(self, socket, target_hostname, udp_port):
        Thread.__init__(self)
        self.socket = socket
        self.target = (target_hostname, udp_port)
        print("CONFIGURATION: ")
        print(self.socket)
        print(self.target)

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

    def run(self):
        while True:
            if len(self.queue) > 0:
                packet = self.queue.pop(0).get_packet()
                for item in packet:
                    self.socket.sendto(item, self.target)
