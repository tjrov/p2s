from .widget import Widget


class GyroscopeWidget(Widget):

    WIDTH = 290
    HEIGHT = 133

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas

        self.canvas.create_text(
            self.left_x + 5,
            self.left_y + 10,
            fill="white",
            font="Courier 12",
            text=f"GYROSCOPE READING +X",
            anchor="nw",
        )

        self.canvas.create_text(
            self.left_x + 5,
            self.left_y + 30 + self.HEIGHT + 10,
            fill="white",
            font="Courier 12",
            text=f"GYROSCOPE READING +Y",
            anchor="nw",
        )

        self.canvas.create_text(
            self.left_x + 5,
            self.left_y + 60 + 2 * self.HEIGHT + 10,
            fill="white",
            font="Courier 12",
            text=f"GYROSCOPE READING +Z",
            anchor="nw",
        )

        self.text_id_x = canvas.create_text(
            self.left_x + self.WIDTH / 2,
            self.left_y + self.HEIGHT / 2 + 10,
            font=("Verdana", "32"),
            fill="#9D8AFE",
        )
        self.text_id_y = canvas.create_text(
            self.left_x + self.WIDTH / 2,
            self.left_y + self.HEIGHT / 2 + 30 + self.HEIGHT + 10,
            font=("Verdana", "32"),
            fill="#5FC794",
        )
        self.text_id_z = canvas.create_text(
            self.left_x + self.WIDTH / 2,
            self.left_y + self.HEIGHT / 2 + 60 + 2 * self.HEIGHT + 10,
            font=("Verdana", "32"),
            fill="#F3D067",
        )
        self.update({"gyro-x": 0})
        self.update({"gyro-y": 0})
        self.update({"gyro-z": 0})

    def update(self, data: dict):
        if "gyro-x" in data:
            self.canvas.itemconfig(self.text_id_x, text=str(data["gyro-x"]) + "°")
        if "gyro-y" in data:
            self.canvas.itemconfig(self.text_id_y, text=str(data["gyro-y"]) + "°")
        if "gyro-z" in data:
            self.canvas.itemconfig(self.text_id_z, text=str(data["gyro-z"]) + "°")
