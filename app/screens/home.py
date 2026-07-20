from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=15
        )

        title = Label(
            text="Golden Studio",
            font_size=28,
            size_hint=(1, 0.15)
        )

        new_project = Button(
            text="➕ پروژه جدید",
            size_hint=(1, 0.12)
        )

        layout.add_widget(title)
        layout.add_widget(new_project)

        self.add_widget(layout)