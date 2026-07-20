from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from app.screens.home import HomeScreen


class GoldenStudio(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(
            HomeScreen(name="home")
        )

        return manager


GoldenStudio().run()