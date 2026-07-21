from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from app.home import HomeScreen
from app.editor import EditorScreen
from app.data import DataScreen
from app.result import ResultScreen


class GoldenStudio(MDApp):

    def build(self):

        self.title = "Golden Studio"

        self.theme_cls.primary_palette = "Blue"

        manager = ScreenManager()

        manager.add_widget(HomeScreen(name="home"))

        manager.add_widget(EditorScreen(name="editor"))

        manager.add_widget(DataScreen(name="data"))

        manager.add_widget(ResultScreen(name="result"))

        return manager


if __name__ == "__main__":
    GoldenStudio().run()