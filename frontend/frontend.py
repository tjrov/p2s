class Frontend:
    dashboard = Dashboard()
    viewfinder = ViewFinder()
    while True:
        dashboard.update()
        viewfinder.update()