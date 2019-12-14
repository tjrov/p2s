import glob
import sys

from serial import Serial, SerialException
from serial.tools.list_ports import comports


def list_serial_ports():
    """ Lists serial port names
        :raises EnvironmentError: On unsupported or unknown platforms
        :returns A list of the serial ports available on the system
        :source http://stackoverflow.com/questions/12090503/ddg#14224477
   """

    if sys.platform.startswith("win"):
        ports = ["COM%s" % (i + 1) for i in range(256)]
    elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob("/dev/tty[A-Za-z]*")
    elif sys.platform.startswith("darwin"):
        ports = glob.glob("/dev/tty.*")
    else:
        raise EnvironmentError("Unsupported platform")

    result = []
    for port in ports:
        try:
            s = Serial(port)
            s.close()
            result.append(port)
        except SerialException:
            pass

    if len(result) == 0 and len(comports()) > 0:
        print(
            f"Fix permissions for these devices (sudo chmod 777): {[port.device for port in comports()]}"
        )
        print("Or close the serial port if its already open\n")

    return result


def get_port():
    """ Allows the user to choose the serial device if there are more than one """

    ports = list_serial_ports()

    if len(ports) == 0:
        raise OSError("No serial device connected")

    if len(ports) == 1:
        port_index = 0
    else:
        port_index = int(
            input(f"Choose which serial port to use (0-{len(ports) - 1}): {ports}: ")
        )

    return ports[port_index]
