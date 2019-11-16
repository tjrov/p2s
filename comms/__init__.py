from serial import Serial

from .helper import get_port
from .reader import SerialReader
from .writer import SerialWriter, DebugWriter


class Comms:

    def __init__(self, baudrate, debug=False):
        """ Communicates with a device via serial on at a given buadrate"""

        self.baudrate = baudrate
        self.serial_port = get_port()
        self.serial, self.reader, self.writer = self.serial_config(debug)

    def serial_config(self, debug):
        """ Creates a Serial, SerialReader, SerialWriter, DebugWriter based on given preferences """

        serial = Serial(port=self.serial_port, baudrate=self.baudrate, write_timeout=0)

        serial_reader = SerialReader(serial)
        serial_reader.start()

        serial_writer = SerialWriter(serial)
        serial_writer.start()

        if debug:
            debug_writer = DebugWriter(serial)
            debug_writer.start()

        return serial, serial_reader, serial_writer

    def __str__(self):
        return f"On port {self.serial_port} at a baudrate of {self.baudrate}"
