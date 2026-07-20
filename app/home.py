from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

from engine.project import ProjectManager
from app.widgets.project_card import ProjectCard


class HomeScreen(MDScreen):
    """
    صفحه اصلی Golden Studio
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.manager_engine = ProjectManager()

        self.layout = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

        self.title = MDLabel(
            text="Golden Studio",
            halign="center",
            font_style="H4"
        )

        self.new_button = MDRaisedButton(
            text="پروژه جدید"
        )

        self.new_button.bind(
            on_release=self.new_project
        )

        self.project_list = MDBoxLayout(
            orientation="vertical",
            spacing=8,
            size_hint_y=None
        )

        self.layout.add_widget(self.title)
        self.layout.add_widget(self.new_button)
        self.layout.add_widget(self.project_list)

        self.add_widget(self.layout)

        self.refresh_projects()

    def refresh_projects(self):

        self.project_list.clear_widgets()

        projects = self.manager_engine.get_projects()

        for project in projects:

            project_id = project[0]
            project_name = project[1]

            card = ProjectCard(
                project_id,
                project_name
            )

            self.project_list.add_widget(card)

    def new_project(self, instance):

        self.manager.current = "editor"

    def on_pre_enter(self):

        self.refresh_projects()