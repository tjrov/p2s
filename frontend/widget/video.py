from .widget import Widget


class VideoWidget(Widget):

    WIDTH = 600
    HEIGHT = 450

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

        self.text_label = self.canvas.create_text(
            self.left_x + self.WIDTH / 2,
            self.left_y + self.HEIGHT / 2,
            fill="white",
            font="Courier 18",
            text=f"Camera feed not available.",
        )

    def update(self, data: dict):
        raise NotImplementedError
