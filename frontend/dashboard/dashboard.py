from .widget import (
    ActuatorWidget,
    CameraWidget,
    DepthWidget,
    GyroscopeWidget,
    HeadingWidget,
    TemperatureWidget,
    ThrustersWidget,
    ControllerWidget,
)

from tkinter import Tk, Canvas


class Dashboard:
    WIDTH = 500
    HEIGHT = 900

    def __init__(self):
        root = Tk()
        root.attributes("-topmost", True)
        self.root = root

        canvas = Canvas(width=self.WIDTH, height=self.HEIGHT, bg="white")
        canvas.pack()

        self.widgets = {
            "ActuatorWidget": ActuatorWidget((0, 500), canvas),
            "CameraWidget": CameraWidget((0, 700), canvas),
            "DepthWidget": DepthWidget((0, 150), canvas),
            "GyroscopeWidget": GyroscopeWidget((0, 0), canvas),
            "HeadingWidget": HeadingWidget((250, 150), canvas),
            "TemperatureWidget": TemperatureWidget((250, 0), canvas),
            "ThrustersWidget": ThrustersWidget((100, 500), canvas,),
            "ControllerWidget": ControllerWidget((0, 900), canvas,),
        }

        self.root.update()

    def update_widget(self, widget_name: str, data: dict):
        if widget_name not in self.widgets:
            return

        self.widgets[widget_name].update(data)

    def update(self):
        self.root.update()
