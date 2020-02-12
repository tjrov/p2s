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
        self.graph_id = canvas.create_image(
            self.left_x + 145, self.left_y + 150, image=myGraph
        )

    def update(self, data: dict):
        raise NotImplementedError
