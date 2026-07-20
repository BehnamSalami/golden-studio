from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton


class DataScreen(MDScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.fields = {}

        root = MDBoxLayout(

            orientation="vertical",

            spacing=10,

            padding=15

        )

        title = MDLabel(

            text="ورود اطلاعات",

            halign="center",

            font_style="Headline"

        )

        root.add_widget(title)

        self.form_layout = MDBoxLayout(

            orientation="vertical",

            spacing=10

        )

        root.add_widget(self.form_layout)

        self.run_button = MDRaisedButton(

            text="محاسبه",

            pos_hint={"center_x":0.5}

        )

        root.add_widget(self.run_button)

        self.add_widget(root)

    def build_form(self, form):

        self.form_layout.clear_widgets()

        self.fields = {}

        for field in form["fields"]:

            widget = MDTextField(

                hint_text=field["label"]

            )

            self.fields[field["label"]] = widget

            self.form_layout.add_widget(widget)

    def get_values(self):

        values = {}

        for name, widget in self.fields.items():

            values[name] = widget.text

        return values