from .x_input import XInputJoystick
import sys
from operator import attrgetter
from tkinter import *
from threading import Thread


class Manipulator(Thread):

   def __init__(self):
      Thread.__init__(self)
      # Joystick Setup
      joysticks = XInputJoystick.enumerate_devices()
      device_numbers = list(map(attrgetter('device_number'), joysticks))
      print('found %d devices: %s' % (len(joysticks), device_numbers))
      if not joysticks:
         print("no joysticks available")
         return
      self.joystick = joysticks[0]
      print('using %d' % self.joystick.device_number)
      battery = self.joystick.get_battery_information()
      print(battery)

   def run(self):

      if not self.joystick:
         return

      @self.joystick.event
      def on_button(button, pressed):
         print('button', button, pressed)
         pass

      @self.joystick.event
      def on_axis(axis, value):
         left_speed = 0
         right_speed = 0
         print('axis', axis, value)
         if axis == "left_trigger":
            left_speed = value
         elif axis == "right_trigger":
            right_speed = value
         self.joystick.set_vibration(left_speed, right_speed)

      while 1:
         self.joystick.dispatch_events()
