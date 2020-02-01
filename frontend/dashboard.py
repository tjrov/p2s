from frontend.widget import (
    ActuatorWidget,
    CameraWidget,
    DepthWidget,
    GyroscopeWidget,
    HeadingWidget,
    TemperatureWidget,
    ThrustersWidget,
    ControllerWidget,
)

from frontend.manipulator import Manipulator

from tkinter import Tk, Canvas
from enum import Enum


class Dashboard:
    WIDTH = 1360
    HEIGHT = 765

    def __init__(self):
        root = Tk()
        root.attributes("-topmost", True)
        root.configure(background='#081035')

        self.root = root

        canvas = Canvas(width=self.WIDTH, height=self.HEIGHT, bg="#081035")
        canvas.pack()

        # self.widgets = {
        #     "ActuatorWidget": ActuatorWidget((0, 500), canvas),
        #     "CameraWidget": CameraWidget((0, 700), canvas),
        #     "DepthWidget": DepthWidget((0, 150), canvas),
        #     "GyroscopeWidget": GyroscopeWidget((0, 0), canvas),
        #     "HeadingWidget": HeadingWidget((250, 150), canvas),
        #     "TemperatureWidget": TemperatureWidget((250, 0), canvas),
        #     "ThrustersWidget": ThrustersWidget((100, 500), canvas,),
        #     "ControllerWidget": ControllerWidget((0, 900), canvas,),
        # }

        accent_color = "#1C326A"

        canvas.create_rectangle(
            30,
            30,
            340,
            245,
            fill=accent_color,
            outline=accent_color,
        )

        canvas.create_rectangle(
            30,
            275,
            340,
            490,
            fill=accent_color,
            outline=accent_color,
        )

        canvas.create_rectangle(
            30,
            520,
            340,
            735,
            fill=accent_color,
            outline=accent_color,
        )

        canvas.create_rectangle(
            380,
            30,
            980,
            128,
            fill=accent_color,
            outline=accent_color
        )

        canvas.create_rectangle(
            380,
            158,
            980,
            608,
            fill=accent_color,
            outline=accent_color,
        )

        canvas.create_rectangle(
            380,
            638,
            980,
            736,
            fill=accent_color,
            outline=accent_color
        )

        canvas.create_rectangle(
            1020,
            48,
            1330,
            358,
            fill=accent_color,
            outline=accent_color
        )

        canvas.create_rectangle(
            1020,
            406,
            1330,
            716,
            fill=accent_color,
            outline=accent_color
        )

        self.manipulator = Manipulator(self.root)

    def update_widget(self, widget_name: str, data: dict):
        if widget_name not in self.widgets:
            return

        self.widgets[widget_name].update(data)

    def update(self):
        self.root.update()

    def start(self):
        self.root.mainloop()
