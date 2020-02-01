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
            1020, 48, 1330, 358, fill=accent_color, outline=accent_color
        )

        canvas.create_rectangle(
            1020, 406, 1330, 716, fill=accent_color, outline=accent_color
        )
        thruster_widget = ThrustersWidget((1020, 406), canvas)

        self.myLogo = PhotoImage(file="frontend/resources/logo.gif")
        canvas.create_image(
            680, 80, image=self.myLogo
        )

        canvas.create_text(
            self.WIDTH - 30,
            self.HEIGHT - 20,
            fill="white",
            font="Courier 10",
            text="TJHSST Python Piloting Software",
            anchor="se",
        ),

        self.manipulator = Manipulator(self.root, comms)

        self.widgets = {
            "ThrustersWidget": thruster_widget,
            "TemperatureWidget": temperature_widget,
            "GyroscopeWidget": gyro_widget,
            "PiConsoleWidget": console_widget,
            "VideoWidget": video_widget,
        }

    def update_widget(self, widget_name: str, data: dict):
        if widget_name not in self.widgets:
            return

        self.widgets[widget_name].update(data)

    def update(self):
        self.root.update()

    def start(self):
        self.root.mainloop()
