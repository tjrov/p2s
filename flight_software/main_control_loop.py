from .comms import Comms


class MainControlLoop:

    def __init__(self, config):
        self.comms = Comms(config)

    def execute(self):
        message = self.comms.read()

