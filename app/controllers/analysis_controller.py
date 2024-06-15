
class AnalysisController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        return self.view.display(self.model.data)



