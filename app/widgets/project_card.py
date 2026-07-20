from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel


class ProjectCard(MDCard):

    def __init__(self, project_name, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        self.padding = 15

        self.radius = [18]

        self.size_hint_y = None

        self.height = 70

        self.ripple_behavior = True

        self.md_bg_color = (0.96, 0.96, 0.96, 1)

        title = MDLabel(

            text="📁 " + project_name,

            font_style="Title",

            halign="left"

        )

        self.add_widget(title)