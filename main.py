from frontend import Frontend
from manipulator import Manipulator

if __name__ == '__main__':
    # TODO: XInput doesn't work with *nix devices, so we need to look into a different module

    frontend = Frontend()
    manipulator = Manipulator()

    manipulator.start()
    frontend.start()
