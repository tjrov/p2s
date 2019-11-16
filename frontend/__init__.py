from .dashboard import Dashboard
from .viewfinder import Viewfinder

class Frontend:
    dashboard = Dashboard()
    viewfinder = Viewfinder()
    while True:
        dashboard.update()
        viewfinder.update()
