from .widget import Widget

from tkinter import PhotoImage


class ThrustersWidget(Widget):
    WIDTH = 310
    HEIGHT = 310

    def __init__(self, left_corner, canvas):
        self.photo = myImage = PhotoImage(
            file="frontend/resources/rov.gif"
        )
        self.left_x, self.left_y = left_corner
        self.canvas = canvas
        self.image_id = canvas.create_image(
            self.left_x + self.WIDTH / 2, self.left_y + self.HEIGHT / 2, image=myImage
        )
        self.front_left = canvas.create_text(
            self.left_x + 75,
            self.left_y + 50,
            font=("Verdana", "16"),
            text="Front Left",
            fill="red",
        )
        self.top_left = canvas.create_text(
            self.left_x + 75,
            self.left_y + 150,
            font=("Verdana", "16"),
            text="Top Left",
            fill="red",
        )
        self.back_left = canvas.create_text(
            self.left_x + 75,
            self.left_y + 250,
            font=("Verdana", "16"),
            text="Back Left",
            fill="red",
        )
        self.front_right = canvas.create_text(
            self.left_x + 225,
            self.left_y + 50,
            font=("Verdana", "16"),
            text="Front Right",
            fill="red",
        )
        self.top_right = canvas.create_text(
            self.left_x + 225,
            self.left_y + 150,
            font=("Verdana", "16"),
            text="Top Right",
            fill="red",
        )
        self.back_right = canvas.create_text(
            self.left_x + 225,
            self.left_y + 250,
            font=("Verdana", "16"),
            text="Back Right",
            fill="red",
        )

    def update(self, data: dict):
        if "front-left" in data:
            self.canvas.itemconfig(self.front_left, text=str(data["front-left"]))
        if "top-left" in data:
            self.canvas.itemconfig(self.top_left, text=str(data["top-left"]))
        if "back-left" in data:
            self.canvas.itemconfig(self.back_left, text=str(data["back-left"]))
        if "front-right" in data:
            self.canvas.itemconfig(self.front_right, text=str(data["front-right"]))
        if "top-right" in data:
            self.canvas.itemconfig(self.top_right, text=str(data["top-right"]))
        if "back-right" in data:
            self.canvas.itemconfig(self.back_right, text=str(data["back-right"]))
