#creates class Frontend
class Frontend:
    dashboard = Dashboard()
    viewfinder = ViewFinder()
    while True:
        dashboard.update()
        viewfinder.update()
        #refreshes camera and GUI views
