from .widget import Widget
from PIL import Image, ImageTk
from collections import deque


class DepthWidget(Widget):
    WIDTH = 250
    HEIGHT = 350

    # left corner of graph is approximately (left_x + 10, left_y-5)
    # width of one block is approximately 58
    # height of one meter is approximately 20

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas
        self.graph = myGraph = ImageTk.PhotoImage(Image.open(
            "frontend/resources/DepthGraph.png"
        ))
        self.graph_id = canvas.create_image(
            self.left_x + 145, self.left_y + 150, image=myGraph
        )
        self.q = deque(maxlen=5)
        self.lines = []
        for i in range(5):
            self.lines.append(canvas.create_line(self.left_x + 10, self.left_y - 5, self.left_x + 10, self.left_y - 5,
                                                 fill="red", width=1.5))

    def update(self, data: dict):
        self.q.append(data["depth"])
        if len(self.q) > 1:
            for k in range(len(self.q) - 1):
                self.canvas.coords(self.lines[k], self.left_x + 10 + (58 * k), self.left_y - 5 + (self.q[k] * 20),
                                   self.left_x + 10 + (58 * (k + 1)), self.left_y - 5 + (self.q[k + 1] * 20))
