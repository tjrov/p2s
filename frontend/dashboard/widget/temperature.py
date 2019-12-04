from .widget import Widget
from tkinter import Tk, Canvas
from tkinter.font import Font

class TemperatureWidget(Widget):
    WIDTH = 250
    HEIGHT = 150
    THRESHOLD = 100

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas
        canvas.create_rectangle(
            self.left_x,
            self.left_y,
            self.left_x + self.WIDTH,
            self.left_y + self.HEIGHT,
            fill="black",
            outline="yellow",
        )
        fill = "red"
        font = Font(family="Times", size=20, weight="bold")
        (w, h) = (font.measure("100"), font.metrics("linespace"))

        self.textLabel = self.canvas.create_text(self.left_x + self.WIDTH/2 - w/2, self.left_y + self.HEIGHT/2 - h/2, fill=fill, font="Times 20 italic bold",
                                text="100")

    def update(self, data: dict):
        temperature = data["temperature"]
        if temperature > self.THRESHOLD:
            fill = "red"
        else:
            fill = "blue"

        # self.textLabel = dict["temperature"]

