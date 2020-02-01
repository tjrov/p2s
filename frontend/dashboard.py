from frontend.widget import (
    ActuatorWidget,
    VideoWidget,
    DepthWidget,
    GyroscopeWidget,
    HeadingWidget,
    RovPiLogWidget,
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
        background_color = "#081035"

        root = Tk()
        root.attributes("-topmost", True)
        root.configure(background=background_color)

        self.root = root

        canvas = Canvas(width=self.WIDTH, height=self.HEIGHT, bg=background_color, bd=0,highlightbackground=background_color)
        canvas.pack()

        # self.widgets = {
        #     "ActuatorWidget": ActuatorWidget((0, 500), canvas),
        #     "CameraWidget": CameraWidget((0, 700), canvas),
        #     "DepthWidget": DepthWidget((0, 150), canvas),
        #     "GyroscopeWidget": GyroscopeWidget((0, 0), canvas),
        #     "HeadingWidget": HeadingWidget((250, 150), canvas),
        #     ,
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
        temperature_widget = TemperatureWidget((40, 40), canvas)

        canvas.create_rectangle(
            30,
            275,
            340,
            490,
            fill=accent_color,
            outline=accent_color,
        )
        heading = HeadingWidget((40, 285), canvas)

        canvas.create_rectangle(
            30,
            520,
            340,
            735,
            fill=accent_color,
            outline=accent_color,
        )
        gyro_widget = GyroscopeWidget((40, 530), canvas)

        canvas.create_rectangle(
            380,
            30,
            980,
            128,
            fill=accent_color,
            outline=accent_color
        )

        video_widget = VideoWidget((380, 158), canvas)

        log_widget = RovPiLogWidget((380, 638), canvas)

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
