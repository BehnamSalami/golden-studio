```python
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

from engine.controller import EngineController


class DataScreen(MDScreen):
    """
    صفحه ورود اطلاعات تابع
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.controller = EngineController()

        self.form = None

        self.layout = MDBoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        self.fields = {}

        self.run_button = MDRaisedButton(
            text="اجرای تابع"
        )

        self.run_button.bind(
            on_release=self.run_function
        )

        self.add_widget(self.layout)

    def load_form(self, form, code=""):

        self.layout.clear_widgets()

        self.fields = {}

        self.form = form

        for field in form["fields"]:

            widget = MDTextField(
                hint_text=field["label"]
            )

            self.fields[field["label"]] = widget

            self.layout.add_widget(widget)

        self.layout.add_widget(self.run_button)

    def run_function(self, instance):

        values = {}

        for name, widget in self.fields.items():

            values[name] = widget.text

        try:

            result = self.controller.run(values)

            result_screen = self.manager.get_screen(
                "result"
            )

            result_screen.show_result(
                result.result
            )

            self.manager.current = "result"

        except Exception as error:

            result_screen = self.manager.get_screen(
                "result"
            )

            result_screen.show_error(
                str(error)
            )

            self.manager.current = "result"
```
