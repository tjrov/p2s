from yaml import safe_load

from sys import exit

from frontend import Frontend
from manipulator import Manipulator
from udp_comms import UDPComms

if __name__ == "__main__":
    # TODO: XInput doesn't work with *nix devices, so we need to look into a different module

    try:
        with open("config/config.yml") as f:
            config = safe_load(f)
    except:
        print("Please copy config/template.yml to config/config.yml")
        exit(0)

    comms = UDPComms(config, debug=True)

    frontend = Frontend()
    manipulator = Manipulator()

    manipulator.start()
    frontend.start()
