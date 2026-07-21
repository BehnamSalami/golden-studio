from engine.parser import PythonParser
from engine.form_engine import FormEngine
from engine.validator import InputValidator
from engine.runner import PythonRunner
from engine.session import Session


class EngineController:
    """
    کنترل‌کننده اصلی موتور Golden Studio
    """

    def __init__(self):

        self.parser = PythonParser()
        self.form_engine = FormEngine()
        self.validator = InputValidator()
        self.runner = PythonRunner()
        self.session = Session()

    def load_code(self, code: str):
        """
        تحلیل کد و ساخت فرم
        """

        function = self.parser.parse(code)

        self.session.function = function
        self.session.code = code

        form = self.form_engine.build(function)

        return form

    def run(self, values):
        """
        اجرای تابع
        """

        function = self.session.function

        validated = self.validator.validate(
            function,
            values
        )

        result = self.runner.execute(
            self.session.code,
            function.name,
            validated
        )

        self.session.result = result

        return result

    def get_result(self):
        """
        آخرین نتیجه اجرا
        """

        return self.session.result

    def clear(self):
        """
        پاک کردن وضعیت موتور
        """

        self.session = Session()