from .widget import Widget


class RovPiLogWidget(Widget):
    WIDTH = 600
    HEIGHT = 98

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas

        canvas.create_rectangle(
            self.left_x,
            self.left_y,
            self.left_x + self.WIDTH,
            self.left_y + self.HEIGHT,
            fill="black",
            outline="#081035",
        )

        self.logs = [

        ]

    def update(self, data: dict):
        return
