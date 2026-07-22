```python
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

from engine.controller import EngineController


class DataScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.controller = EngineController()

        self.code = ""

        self.form = None

        self.fields = {}

        self.layout = MDBoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        self.run_button = MDRaisedButton(
            text="اجرای تابع"
        )

        self.run_button.bind(
            on_release=self.run_function
        )

        self.add_widget(self.layout)

    def load_form(self, form, code):

        self.code = code

        self.form = form

        self.fields = {}

        self.layout.clear_widgets()

        for item in form["fields"]:

            widget = MDTextField(
                hint_text=item["label"]
            )

            self.fields[item["label"]] = widget

            self.layout.add_widget(widget)

        self.layout.add_widget(self.run_button)

    def run_function(self, instance):

        values = {}

        for name, widget in self.fields.items():

            values[name] = widget.text

        try:

            self.controller.load_code(
                self.code
            )

            result = self.controller.run(
                values
            )

            screen = self.manager.get_screen(
                "result"
            )

            screen.show_result(
                result.result
            )

            self.manager.current = "result"

        except Exception as error:

            screen = self.manager.get_screen(
                "result"
            )

            screen.show_error(
                str(error)
            )

            self.manager.current = "result"
```
