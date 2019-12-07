from .widget import Widget


class TemperatureWidget(Widget):
    WIDTH = 250
    HEIGHT = 150
    THRESHOLD = 32
    DEGREE_SIGN = u'\N{DEGREE SIGN}'

    def __init__(self, left_corner, canvas):
        self.left_x, self.left_y = left_corner
        self.canvas = canvas

        fill = "red"
        self.text_label = self.canvas.create_text(self.left_x + self.WIDTH / 2, self.left_y + self.HEIGHT / 2,
                                                  fill=fill, font="Serif 25",
                                                  text="old")

    def update(self, data: dict):
        temperature = data["temperature"]

        fill = "red"
        if temperature < self.THRESHOLD:
            fill = "blue"

        self.canvas.itemconfig(self.text_label, fill=fill, text=f"{temperature}{self.DEGREE_SIGN}F")
