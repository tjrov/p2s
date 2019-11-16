from .dashboard import *
from .viewfinder import *

class Frontend:
    dashboard = Dashboard()
    viewfinder = Viewfinder()
    while True:
        dashboard.update()
        viewfinder.update()
