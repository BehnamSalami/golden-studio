from engine.parser import PythonParser
from engine.form_engine import FormEngine


class EngineController:
    """
    کنترل‌کننده اصلی موتور برنامه
    """

    def __init__(self):

        self.parser = PythonParser()
        self.form_engine = FormEngine()

    def load_code(self, code: str):

        """
        دریافت کد پایتون
        """

        function = self.parser.parse(code)

        form = self.form_engine.build(function)

        return form