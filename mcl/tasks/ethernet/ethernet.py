from socket import socket, AF_INET, SOCK_DGRAM


class ethernet_task:
    UDP_PORT = 5005

    def __init__(self, config):
        """ Communicates with a device via serial on at a given buadrate"""
        self.host_ip = config["udp"]["ip"]["rov"]
        self.target_ip = config["udp"]["ip"]["ground_station"]

        self.sending_socket, self.receiving_socket = self.comms_config()

    def comms_config(self):
        sending_socket = socket(AF_INET, SOCK_DGRAM)
        receiving_socket = socket(AF_INET, SOCK_DGRAM)

        receiving_socket.bind((self.host_ip, self.UDP_PORT))
        receiving_socket.settimeout(1)

        print("----------- CONFIGURATION -----------")
        print(sending_socket)
        print(receiving_socket)
        print((self.target_ip, self.UDP_PORT))
        print("-------------------------------------")

        return sending_socket, receiving_socket

    def read(self):
        try:
            data, address = self.receiving_socket.recvfrom(1024)
            return data.decode('utf-8'), True
        except:
            return '', False

    def write(self, message):
        if not isinstance(message, str):
            return
        encoded_message = message.encode("utf-8")
        self.sending_socket.sendto(encoded_message, (self.target_ip, self.UDP_PORT))

    def __str__(self):
        return f"Target hostname is {self.target_ip} on port {self.UDP_PORT}"
