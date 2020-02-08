from .widget import Widget


class PiConsoleWidget(Widget):
    WIDTH = 600
    HEIGHT = 98

    MAX_LEN = 53

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
            "Console",
            "Logs from the pi will be printed to the console,",
            "along with unidentifiable messages.",
        ]

        self.text_items = [
            self.canvas.create_text(
                self.left_x + 10,
                self.left_y + 20,
                fill="white",
                font="Courier 14",
                text=self.logs[0],
                anchor="w",
                width=self.WIDTH - 10,
            ),
            self.canvas.create_text(
                self.left_x + 10,
                self.left_y + 50,
                fill="white",
                font="Courier 14",
                text=self.logs[1],
                anchor="w",
                width=self.WIDTH - 10,
            ),
            self.canvas.create_text(
                self.left_x + 10,
                self.left_y + 80,
                fill="white",
                font="Courier 14",
                text=self.logs[2],
                anchor="w",
                width=self.WIDTH - 10,
            ),
        ]

    def update(self, data: dict):
        if "log" in data:
            self.logs.pop(0)
            self.logs.append(data["log"])
            for index, item in enumerate(self.text_items):
                self.canvas.itemconfig(
                    item, fill="white", text=self.logs[index][: self.MAX_LEN + 1]
                )
