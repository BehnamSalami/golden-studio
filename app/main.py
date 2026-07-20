from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from app.screens.home import HomeScreen


class GoldenStudio(MDApp):

    def build(self):

        self.title = "Golden Studio"

        self.theme_cls.primary_palette = "Blue"

        self.theme_cls.theme_style = "Light"

        manager = ScreenManager()

        manager.add_widget(
            HomeScreen(name="home")
        )

        return manager


GoldenStudio().run()