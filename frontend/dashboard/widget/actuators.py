from .widget import Widget


class ActuatorWidget(Widget):

    WIDTH = 100
    HEIGHT = 200

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas

        canvas.create_rectangle(
            self.left_x,
            self.left_y,
            self.left_x + self.WIDTH,
            self.left_y + self.HEIGHT,
            fill="red",
            outline="yellow",
        )

    def update(self, data: dict):
        raise NotImplementedError
