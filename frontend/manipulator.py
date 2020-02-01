from enum import Enum


class Bindings(Enum):
    FORWARD = "<w>"
    STRAFE_LEFT = "<a>"
    BACKWARDS = "<s>"
    STRAFE_RIGHT = "<d>"
    MOVE_UP = "<q>"
    MOVE_DOWN = "<e>"


class Manipulator:

    def __init__(self, root):
        root.bind(Bindings.FORWARD.value, self.forward)
        root.bind(Bindings.STRAFE_LEFT.value, self.strafe_left)
        root.bind(Bindings.BACKWARDS.value, self.backwards)
        root.bind(Bindings.STRAFE_RIGHT.value, self.strafe_right)
        root.bind(Bindings.MOVE_UP.value, self.move_up)
        root.bind(Bindings.MOVE_DOWN.value, self.move_down)

    def forward(self, *args):
        print("W clicked")

    def backwards(self, *args):
        print("S clicked")

    def strafe_left(self, *args):
        print("A clicked")

    def strafe_right(self, *args):
        print("D clicked")

    def move_up(self, *args):
        print("Q clicked")

    def move_down(self, *args):
        print("E clicked")
