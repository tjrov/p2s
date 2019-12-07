from .widget import Widget


class GyroscopeWidget(Widget):

    WIDTH = 250
    HEIGHT = 150

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas
        canvas.create_rectangle(
            self.left_x,
            self.left_y,
            self.left_x + self.WIDTH,
            self.left_y + self.HEIGHT,
            fill="magenta",
            outline="yellow",
        )

    def update(self, data: dict):
        raise NotImplementedError
