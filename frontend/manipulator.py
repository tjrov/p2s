from enum import Enum
from comms import Comms


class Bindings(Enum):
    FORWARD = "<w>"
    STRAFE_LEFT = "<a>"
    BACKWARDS = "<s>"
    STRAFE_RIGHT = "<d>"
    MOVE_UP = "<q>"
    MOVE_DOWN = "<e>"


class Manipulator:
    def __init__(self, root, comms: Comms):
        root.bind(Bindings.FORWARD.value, self.forward)
        root.bind(Bindings.STRAFE_LEFT.value, self.strafe_left)
        root.bind(Bindings.BACKWARDS.value, self.backwards)
        root.bind(Bindings.STRAFE_RIGHT.value, self.strafe_right)
        root.bind(Bindings.MOVE_UP.value, self.move_up)
        root.bind(Bindings.MOVE_DOWN.value, self.move_down)
        self.comms: Comms = comms

    def forward(self, *args):
        self.comms.write("W clicked")

    def backwards(self, *args):
        self.comms.write("S clicked")

    def strafe_left(self, *args):
        self.comms.write("A clicked")

    def strafe_right(self, *args):
        self.comms.write("D clicked")

    def move_up(self, *args):
        self.comms.write("Q clicked")

    def move_down(self, *args):
        self.comms.write("E clicked")
