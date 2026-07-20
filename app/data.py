from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

from engine.validator import Validator
from engine.runner import PythonRunner


class DataScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.validator = Validator()
        self.runner = PythonRunner()

        self.function = None
        self.code = ""

        self.layout = MDBoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        self.fields = {}

        self.button = MDRaisedButton(
            text="اجرای تابع"
        )

        self.button.bind(on_release=self.run_function)

        self.add_widget(self.layout)

    def load_form(self, form, code=""):

        self.layout.clear_widgets()

        self.fields = {}

        self.function = form

        self.code = code

        for field in form["fields"]:

            text = MDTextField(
                hint_text=field["label"]
            )

            self.fields[field["label"]] = (
                text,
                field["type"]
            )

            self.layout.add_widget(text)

        self.layout.add_widget(self.button)

    def run_function(self, instance):

        values = {}

        for name, item in self.fields.items():

            widget, value_type = item

            values[name] = self.validator.validate(
                widget.text,
                value_type
            )

        result = self.runner.execute(
            self.code,
            self.function["title"],
            values
        )

        result_screen = self.manager.get_screen("result")

        result_screen.show_result(result)

        self.manager.current = "result"