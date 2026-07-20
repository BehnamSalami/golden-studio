from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


class ResultScreen(MDScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        root = MDBoxLayout(

            orientation="vertical",

            padding=20

        )

        title = MDLabel(

            text="نتیجه",

            halign="center",

            font_style="Headline"

        )

        self.result = MDLabel(

            text="",

            halign="center"

        )

        root.add_widget(title)

        root.add_widget(self.result)

        self.add_widget(root)

    def show_result(self, result):

        self.result.text = str(result)