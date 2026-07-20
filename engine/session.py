from engine.controller import EngineController


class Session:

    def __init__(self):

        self.engine = EngineController()

        self.current_project = None

    def open_project(self, project):

        self.current_project = project

    def load_code(self, code):

        return self.engine.load_code(code)

    def execute(self, values):

        return self.engine.execute(values)

    def close(self):

        self.current_project = None