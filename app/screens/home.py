from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard


class HomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

        new_project = MDRaisedButton(
            text="➕ پروژه جدید",
            pos_hint={"center_x": .5}
        )

        root.add_widget(new_project)

        subtitle = MDLabel(
            text="پروژه‌های من",
            font_style="Title",
            padding=[0,20,0,10]
        )

        root.add_widget(subtitle)

        projects = [
            "تحلیل شرکت تولیدی",
            "تحلیل شرکت سرمایه گذاری",
            "ساخت سایت فروشگاهی"
        ]

        for project in projects:

            card = MDCard(
                orientation="vertical",
                padding=15,
                radius=[15],
                size_hint_y=None,
                height=70
            )

            label = MDLabel(
                text="📁  " + project
            )

            card.add_widget(label)

            root.add_widget(card)

        self.add_widget(root)