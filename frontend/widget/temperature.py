from .widget import Widget


class TemperatureWidget(Widget):
    WIDTH = 290
    HEIGHT = 195
    THRESHOLD = 32
    DEGREE_SIGN = "\N{DEGREE SIGN}"

    RED = "#FF5400"
    BLUE = "#2EBBB2"

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas

        self.canvas.create_text(
            self.left_x + 5,
            self.left_y + 10,
            fill='white',
            font="Courier 12",
            text=f"AMBIENT TEMPERATURE",
            anchor='nw'
        )

        fill = self.BLUE
        self.text_label = self.canvas.create_text(
            self.left_x + self.WIDTH / 2,
            self.left_y + self.HEIGHT / 2 + 10,
            fill=fill,
            font=("Verdana", "32"),
            text=f"0{self.DEGREE_SIGN}F",
        )

    def update(self, data: dict):
        temperature = data["temperature"]

        fill = self.RED
        if temperature < self.THRESHOLD:
            fill = self.BLUE

        self.canvas.itemconfig(
            self.text_label, fill=fill, text=f"{temperature}{self.DEGREE_SIGN}F"
        )
