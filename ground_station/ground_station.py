from yaml import safe_load

from sys import exit
import os

from .frontend import Dashboard
from .comms import Comms

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def start_ground_station():
    try:
        with open(os.path.join(BASE_DIR, "config/config.yml")) as f:
            config = safe_load(f)
    except:
        print("Please copy config/template.yml to config/config.yml")
        exit(0)

    comms = Comms(config)
    dashboard = Dashboard(comms)
    comms.set_dashboard(dashboard)

    dashboard.start()


if __name__ == "__main__":
    start_ground_station()
