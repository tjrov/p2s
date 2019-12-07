from .widget import Widget


class GyroscopeWidget(Widget):

    WIDTH = 250
    HEIGHT = 150

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas
        self.text_id = canvas.create_text(125, 75, font=("Serif", "25"))
        self.update({"gyro" : 2048})

    def update(self, data: dict):
        self.canvas.itemconfig(self.text_id, text=str(data["gyro"])+"°/s")
