from yaml import safe_load

from sys import exit
import os

from .main_control_loop import MainControlLoop

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def start_flight_software():
    try:
        with open(os.path.join(BASE_DIR, "config/config.yml")) as f:
            config = safe_load(f)
    except:
        print("Please copy config/template.yml to config/config.yml")
        exit(0)

    mcl = MainControlLoop(config)
    while True:
        mcl.execute()


if __name__ == "__main__":
    start_flight_software()
