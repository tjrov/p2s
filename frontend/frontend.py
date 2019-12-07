from .dashboard import Dashboard
from .viewfinder import Viewfinder
class Frontend:
    def __init__(self):
        self.dashboard = Dashboard()
        self.viewfinder = Viewfinder()

    def start(self):
        while True:
            self.dashboard.update()
            self.viewfinder.update()
