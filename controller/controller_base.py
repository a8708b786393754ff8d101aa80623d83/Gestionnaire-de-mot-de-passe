class ControllerBase:
    def __init__(self, view):
        self.view = view()
