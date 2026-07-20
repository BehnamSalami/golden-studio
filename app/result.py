from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton


class ResultScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        title = MDLabel(
            text="نتیجه محاسبه",
            halign="center",
            font_style="Headline"
        )

        root.add_widget(title)

        self.result_label = MDLabel(
            text="هنوز نتیجه‌ای وجود ندارد.",
            halign="center"
        )

        root.add_widget(self.result_label)

        self.back_button = MDRaisedButton(
            text="بازگشت به صفحه اصلی",
            pos_hint={"center_x": 0.5}
        )

        self.back_button.bind(
            on_release=self.go_home
        )

        root.add_widget(self.back_button)

        self.add_widget(root)

    def show_result(self, result):

        text = ""

        for key, value in result.items():

            text += f"{key} : {value}\n"

        self.result_label.text = text

    def go_home(self, *args):

        if self.manager:

            self.manager.current = "home"