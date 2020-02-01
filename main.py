from yaml import safe_load

from sys import exit

from frontend import Dashboard
from udp_comms import UDPComms

if __name__ == "__main__":
    try:
        with open("config/config.yml") as f:
            config = safe_load(f)
    except:
        print("Please copy config/template.yml to config/config.yml")
        exit(0)

    comms = UDPComms(config)

    dashboard = Dashboard()
    dashboard.start()
