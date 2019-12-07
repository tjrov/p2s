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
        font = Font(family="SansSerif", size=50, weight="bold")
        degreeSign = u'\N{DEGREE SIGN}'
        (w, h) = (font.measure("100 " + degreeSign + "F"), font.metrics("linespace"))

        self.textLabel = self.canvas.create_text(self.left_x + self.WIDTH/2, self.left_y + self.HEIGHT/2, fill=fill, font="SansSerif 50 bold",
                                text="100 " + degreeSign + "F")


    def update(self, data: dict):
        temperature = data["temperature"]
        if temperature > self.THRESHOLD:
            fill = "red"
        else:
            fill = "blue"

        # self.textLabel = dict["temperature"]

