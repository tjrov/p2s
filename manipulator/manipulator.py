# DX
import math
from threading import Thread
import pygame


class Manipulator(Thread):
    def __init__(self):
        Thread.__init__(self)

        pygame.init()
        pygame.display.set_mode((100, 100))  # big display not needed, no display = no inputs
        pygame.display.set_caption("Testing X-BOX controller")

        joysticks = []

        for i in range(0, pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
            joysticks[-1].init()
            print("Detected joystick '", joysticks[-1].get_name(), "'")

    def run(self):
        clock = pygame.time.Clock()
        keep_playing = True  # variable made for future use

        while keep_playing:
            clock.tick(60)  # not sure which refresh rate is optimal, it seems that 0 is a bit too sensitive
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:
                        if event.value > 0.0:
                            self.joy_one_right(event.value)
                        else:
                            self.joy_one_left(event.value)
                    elif event.axis == 1:
                        if event.value < 0.0:
                            self.joy_one_up(event.value)
                        else:
                            self.joy_one_down(event.value)
                    elif event.axis == 4:
                        if event.value < 0.0:
                            self.joy_two_left(event.value)
                        else:
                            self.joy_two_right(event.value)
                    elif event.axis == 3:
                        if event.value < 0.0:
                            self.joy_two_up(event.value)
                        else:
                            self.joy_two_down(event.value)
                    else:
                        if event.value > 0.0:
                            self.trigger_left(event.value)
                        else:
                            self.trigger_right(event.value)
                if event.type == pygame.JOYBUTTONDOWN:
                    self.button(event.button, False)
                if event.type == pygame.JOYBUTTONUP:
                    self.button(event.button, True)
                if event.type == pygame.JOYHATMOTION:
                    if event.value[0] == 1:
                        self.d_pad_right()
                    elif event.value[0] == -1:
                        self.d_pad_left()
                    elif event.value[1] == 1:
                        self.d_pad_up()
                    elif event.value[1] == -1:
                        self.d_pad_down()
                    else:
                        self.d_pad_center()

        pygame.quit()

    def joy_one_up(self, value):  # returns value (pos value of joystick) is [-1, 0) -1 being the farthest up
        print("joystick one: up ", value)

    def joy_one_down(self, value):  # returns value is (0, 1] 1 being the farthest down
        print("joystick one: down ", value)

    def joy_one_left(self, value):  # returns value is [-1, 0) -1 being the farthest left
        print("joystick one: left ", value)

    def joy_one_right(self, value):  # returns value is [-1, 0) -1 being the farthest right
        print("joystick one: right ", value)

    def joy_two_up(self, value):  # returns value (pos value of joystick) is [-1, 0) -1 being the farthest up
        print("joystick two: up ", value)

    def joy_two_down(self, value):  # returns value is (0, 1] 1 being the farthest down
        print("joystick two: down ", value)

    def joy_two_left(self, value):  # returns value is [-1, 0) -1 being the farthest left
        print("joystick two: left ", value)

    def joy_two_right(self, value):  # returns value is [-1, 0) -1 being the farthest right
        print("joystick two: right ", value)

    def trigger_left(self, value):  # returns value is (0, 1] 1 being the trigger pushed down farthest
        print("trigger left: ", value)

    def trigger_right(self, value):  # returns value is [-1, 0) -1 being the trigger pushed down farthest
        print("trigger right: ", value)

    def d_pad_up(self):
        print("d-pad up")

    def d_pad_down(self):
        print("d-pad down")

    def d_pad_left(self):
        print("d-pad left")

    def d_pad_right(self):
        print("d-pad right")

    def d_pad_center(self):  # d-pad returned to resting state
        print("d-pad centered")

    def button(self, id, state):  # s tate is boolean -- True means button is now up, False means button is now down
        if state:  # id refers to which button is being pressed
            print("button ", id, " up")
        else:  # here are what ids are which button so i can save u some testing
            print("button ", id, " down")  # 0 is A  1 is B   2 is X   3 is Y
            # LB is 4   RB is 5  (these are the ones above the triggers)
            # the one with the two overlapping squares is 6
            # the one to the right of that with the three stripes is 7
            # can't tell if the power button has an id, it opens windows game bar when i press it
