from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel


class ProjectCard(MDCard):
    """
    کارت نمایش پروژه
    """

    def __init__(
        self,
        project_id,
        project_name,
        callback=None,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.project_id = project_id
        self.project_name = project_name
        self.callback = callback

        self.orientation = "vertical"

        self.padding = 15

        self.spacing = 10

        self.radius = [12]

        self.size_hint_y = None

        self.height = 70

        self.ripple_behavior = True

        self.focus_behavior = True

        self.label = MDLabel(
            text=project_name,
            halign="center"
        )

        self.add_widget(self.label)

        self.bind(
            on_release=self.open_project
        )

    def open_project(self, *args):
        """
        باز کردن پروژه
        """

        if self.callback:

            self.callback(self.project_id)