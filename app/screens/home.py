from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout


class HomeScreen(MDScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = MDBoxLayout(

            orientation="vertical",

            padding=20,

            spacing=20

        )

        title = MDLabel(

            text="Golden Studio",

            halign="center",

            font_style="Headline"

        )

        button = MDRaisedButton(

            text="پروژه جدید",

            pos_hint={"center_x": 0.5}

        )

        layout.add_widget(title)

        layout.add_widget(button)

        self.add_widget(layout)