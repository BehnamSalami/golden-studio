from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel


class ProjectCard(MDCard):
    """
    کارت نمایش پروژه
    """

    def __init__(self, project_id, project_name, **kwargs):
        super().__init__(**kwargs)

        self.project_id = project_id
        self.project_name = project_name

        self.orientation = "vertical"

        self.padding = 15

        self.spacing = 10

        self.radius = [12]

        self.size_hint_y = None

        self.height = 70

        self.label = MDLabel(
            text=project_name,
            halign="center"
        )

        self.add_widget(self.label)

    def on_release(self):
        """
        در مراحل بعدی پروژه را باز می‌کند.
        """
        print(
            f"Open Project : {self.project_id}"
        )