from comms import Comms
from frontend.widget import (
    ActuatorWidget,
    VideoWidget,
    DepthWidget,
    GyroscopeWidget,
    PiConsoleWidget,
    TemperatureWidget,
    ThrustersWidget,
    ControllerWidget,
)
from frontend.manipulator import Manipulator

from tkinter import Tk, Canvas, PhotoImage


class Dashboard:
    WIDTH = 1360
    HEIGHT = 765

    def __init__(self, comms: Comms):
        background_color = "#081035"

        root = Tk()
        root.attributes("-topmost", True)
        root.configure(background=background_color)

        self.root = root

        canvas = Canvas(
            width=self.WIDTH,
            height=self.HEIGHT,
            bg=background_color,
            bd=0,
            highlightbackground=background_color,
        )
        canvas.pack()

        accent_color = "#1C326A"

        canvas.create_rectangle(
            30, 30, 340, 245, fill=accent_color, outline=accent_color,
        )
        temperature_widget = TemperatureWidget((40, 40), canvas)

        canvas.create_rectangle(
            30, 275, 340, 408, fill=accent_color, outline=accent_color,
        )

        canvas.create_rectangle(
            30, 438, 340, 571, fill=accent_color, outline=accent_color,
        )

        canvas.create_rectangle(
            30, 601, 340, 734, fill=accent_color, outline=accent_color,
        )
        gyro_widget = GyroscopeWidget((40, 285), canvas)

        canvas.create_rectangle(
            380, 30, 980, 128, fill=accent_color, outline=accent_color
        )

        video_widget = VideoWidget((380, 158), canvas)

        console_widget = PiConsoleWidget((380, 638), canvas)

        canvas.create_rectangle(
            1020, 68, 1330, 378, fill=accent_color, outline=accent_color
        )

        depth_widget = DepthWidget((1030, 78), canvas)

        thruster_widget = ThrustersWidget((1020, 406), canvas)

        self.logo = PhotoImage(file="frontend/resources/logo.gif")
        canvas.create_image(
            self.WIDTH - 30, 10, image=self.logo, anchor="ne"
        )

        canvas.create_text(
            1020,
            25,
            fill="white",
            font="Courier 14",
            text="Python Piloting Software",
            anchor="nw",
        ),

        self.manipulator = Manipulator(self.root, comms)

        self.widgets = {
            "ThrustersWidget": thruster_widget,
            "TemperatureWidget": temperature_widget,
            "GyroscopeWidget": gyro_widget,
            "PiConsoleWidget": console_widget,
            "VideoWidget": video_widget,
            "DepthWidget": depth_widget
        }

    def update_widget(self, widget_name: str, data: dict):
        if widget_name not in self.widgets:
            return

        self.widgets[widget_name].update(data)

    def update(self):
        self.root.update()

    def start(self):
        self.root.mainloop()
