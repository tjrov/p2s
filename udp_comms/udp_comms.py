from socket import socket, AF_INET, SOCK_DGRAM

from .reader import UDPReader
from .writer import UDPWriter, UDPDebugWriter


class UDPComms:

    UDP_PORT = 5005

    def __init__(self, config):
        """ Communicates with a device via serial on at a given buadrate"""
        self.host_ip = config["udp"]["ip"]["ground_station"]
        self.target_ip = config["udp"]["ip"]["rov"]

        (
            self.sending_socket,
            self.receiving_socket,
            self.reader,
            self.writer,
        ) = self.comms_config()

    def comms_config(self):
        """ Creates a Serial, SerialReader, SerialWriter, DebugWriter based on given preferences """

        sending_socket = socket(AF_INET, SOCK_DGRAM)
        receiving_socket = socket(AF_INET, SOCK_DGRAM)

        receiving_socket.bind((self.host_ip, self.UDP_PORT))

        udp_reader = UDPReader(receiving_socket)
        udp_reader.start()

        udp_writer = UDPWriter(sending_socket, self.target_ip, self.UDP_PORT)
        udp_writer.start()

        return sending_socket, receiving_socket, udp_reader, udp_writer

    def write_packet(self, packet):
        if hasattr(packet, "get_packet"):
            # Ensures the packet has a list of writable bytes
            self.writer.queue.append(packet)
        else:
            raise RuntimeError("Received a non-packet object")

    def __str__(self):
        return f"Target hostname is {self.target_ip} on port {self.UDP_PORT}"
