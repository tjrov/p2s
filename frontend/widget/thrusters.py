from .widget import Widget

from tkinter import PhotoImage


class ThrustersWidget(Widget):

    WIDTH = 310
    HEIGHT = 310

    def __init__(self, left_corner, canvas):
        self.photo = myImage = PhotoImage(
            file="frontend/resources/rov-thrusters_image.gif"
        )
        self.left_x, self.left_y = left_corner
        self.canvas = canvas
        self.image_id = canvas.create_image(
            self.left_x + self.WIDTH / 2, self.left_y + self.HEIGHT / 2, image=myImage
        )
        self.top_left = canvas.create_text(
            self.left_x + 75,
            self.left_y + 50,
            font=("Serif", "20"),
            text="top-left",
            fill="red",
        )
        self.mid_left = canvas.create_text(
            self.left_x + 75,
            self.left_y + 150,
            font=("Serif", "20"),
            text="mid-left",
            fill="red",
        )
        self.bottom_left = canvas.create_text(
            self.left_x + 75,
            self.left_y + 250,
            font=("Serif", "20"),
            text="bottom-left",
            fill="red",
        )
        self.top_right = canvas.create_text(
            self.left_x + 225,
            self.left_y + 50,
            font=("Serif", "20"),
            text="top-right",
            fill="red",
        )
        self.mid_right = canvas.create_text(
            self.left_x + 225,
            self.left_y + 150,
            font=("Serif", "20"),
            text="mid-right",
            fill="red",
        )
        self.bottom_right = canvas.create_text(
            self.left_x + 225,
            self.left_y + 250,
            font=("Serif", "20"),
            text="bottom-right",
            fill="red",
        )

    def update(self, data: dict):
        if "top-left" in data:
            self.canvas.itemconfig(self.top_left, text=str(data["top-left"]))
        if "mid-left" in data:
            self.canvas.itemconfig(self.mid_left, text=str(data["mid-left"]))
        if "bottom-left" in data:
            self.canvas.itemconfig(self.bottom_left, text=str(data["bottom-left"]))
        if "top-right" in data:
            self.canvas.itemconfig(self.top_right, text=str(data["top-right"]))
        if "mid-right" in data:
            self.canvas.itemconfig(self.mid_right, text=str(data["mid-right"]))
        if "bottom-right" in data:
            self.canvas.itemconfig(self.bottom_right, text=str(data["bottom-right"]))
