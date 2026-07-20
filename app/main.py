from kivy.app import App
from kivy.uix.label import Label


class GoldenStudio(App):

    def build(self):
        return Label(
            text="Golden Studio",
            font_size=30
        )


GoldenStudio().run()
