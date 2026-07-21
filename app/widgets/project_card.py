from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel


class ProjectCard(MDCard):
    """
    کارت نمایش پروژه
    """

    def __init__(
        self,
        project_id: int,
        project_name: str,
        callback=None,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.project_id = project_id
        self.project_name = project_name
        self.callback = callback

        self.orientation = "vertical"
        self.padding = "12dp"
        self.spacing = "8dp"

        self.size_hint_y = None
        self.height = "70dp"

        self.radius = [12, 12, 12, 12]
        self.elevation = 2
        self.ripple_behavior = True

        self.label = MDLabel(
            text=project_name,
            halign="center",
            valign="middle"
        )

        self.add_widget(self.label)

        self.bind(
            on_release=self._on_card_pressed
        )

    def _on_card_pressed(self, *args):
        """
        هنگام لمس کارت
        """

        if callable(self.callback):
            self.callback(self.project_id)