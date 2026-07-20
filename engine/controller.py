from engine.parser import FunctionParser
from engine.form_engine import FormEngine
from engine.runner import PythonRunner
from engine.validator import Validator
from engine.result import Result


class EngineController:

    def __init__(self):

        self.runner = PythonRunner()

        self.form = None

        self.code = ""

    def load_code(self, source_code):

        self.code = source_code

        self.runner.load(source_code)

        engine = FormEngine(source_code)

        self.form = engine.build()

        return self.form

    def execute(self, values):

        if self.form is None:

            return Result(
                False,
                None,
                "No form loaded"
            )

        arguments = {}

        for field in self.form["fields"]:

            name = field["label"]

            value = values.get(name, "")

            arguments[name] = Validator.convert(
                value,
                field["type"]
            )

        output = self.runner.execute(
            self.form["title"],
            arguments
        )

        return Result(
            output["success"],
            output["result"],
            output["error"]
        )