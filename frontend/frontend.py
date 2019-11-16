from dashboard import gui
from viewfinder import viewfinder

class Frontend:
    dashboard = Dashboard()
    viewfinder = ViewFinder()
    while True:
        dashboard.update()
        viewfinder.update()
