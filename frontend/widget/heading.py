from .widget import Widget


class HeadingWidget(Widget):

    WIDTH = 250
    HEIGHT = 350

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas
        canvas.create_rectangle(
            self.left_x,
            self.left_y,
            self.left_x + self.WIDTH,
            self.left_y + self.HEIGHT,
            fill="yellow",
            outline="yellow",
        )

    def update(self, data: dict):
        raise NotImplementedError
