from .widget import Widget


class GyroscopeWidget(Widget):

    WIDTH = 290
    HEIGHT = 195

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas

        self.canvas.create_text(
            self.left_x + 5,
            self.left_y + 10,
            fill='white',
            font="Courier 12",
            text=f"GYROSCOPE READING",
            anchor='nw'
        )

        self.text_id = canvas.create_text(self.left_x + self.WIDTH / 2, self.left_y + self.HEIGHT / 2 + 10, font=("Verdana", "32"), fill="#5FC794")
        self.update({"gyro": 2048})

    def update(self, data: dict):
        if "gyro" in data:
            self.canvas.itemconfig(self.text_id, text=str(data["gyro"]) + "°/s")
