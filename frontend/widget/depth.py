from .widget import Widget

from tkinter import PhotoImage

class DepthWidget(Widget):

    WIDTH = 250
    HEIGHT = 350

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas
        self.graph = myGraph = PhotoImage(
            file="frontend/resources/DepthGIF.gif"
        )
        canvas.create_rectangle(
            self.left_x,
            self.left_y,
            self.left_x + self.WIDTH,
            self.left_y + self.HEIGHT,
            fill="green",
            outline="yellow",
        )
        self.graph_id = canvas.create_image(
            self.left_x + self.WIDTH / 2, self.left_y + self.HEIGHT / 2, image=myGraph
        )

    def update(self, data: dict):
        raise NotImplementedError
