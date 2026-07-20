from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.scrollview import MDScrollView

from app.project_dialog import ProjectDialog
from app.widgets.project_card import ProjectCard


class HomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.projects = []

        root = MDBoxLayout(
            orientation="vertical",
            padding=15,
            spacing=15
        )

        title = MDLabel(
            text="Golden Studio",
            halign="center",
            font_style="Headline"
        )

        root.add_widget(title)

        new_button = MDRaisedButton(
            text="➕ پروژه جدید",
            pos_hint={"center_x": 0.5}
        )

        new_button.bind(
            on_release=self.open_dialog
        )

        root.add_widget(new_button)

        self.scroll = MDScrollView()

        self.project_list = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing=10
        )

        self.scroll.add_widget(self.project_list)

        root.add_widget(self.scroll)

        self.add_widget(root)

    def open_dialog(self, *args):

        dialog = ProjectDialog(
            self.create_project
        )

        dialog.open()

    def create_project(self, project_name):

        self.projects.append(project_name)

        card = ProjectCard(project_name)

        self.project_list.add_widget(card)

        print("Project Created:", project_name)