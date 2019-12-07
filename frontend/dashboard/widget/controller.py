#kevin wu 12/7/2019
from tkinter import *

class ControllerWidget(Widget):

    WIDTH = 250
    HEIGHT = 150

    def __init__(self, left_corner, canvas):
        #Canvas Setup
        self.left_x, self.left_y = left_corner
        self.canvas = canvas
        canvas.create_rectangle(
            self.left_x,
            self.left_y,
            self.left_x + self.WIDTH,
            self.left_y + self.HEIGHT,
            fill="white",
            outline="red",
        )
    def update(self, data: dict):
        raise NotImplementedError