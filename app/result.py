
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton


class ResultScreen(MDScreen):
    """
    صفحه نمایش نتیجه اجرای تابع
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        self.title = MDLabel(
            text="نتیجه اجرا",
            halign="center",
            font_style="H5"
        )

        self.result_label = MDLabel(
            text="",
            halign="center",
            font_style="H4",
            markup=True
        )

        self.back_button = MDRaisedButton(
            text="بازگشت به صفحه اصلی"
        )

        self.back_button.bind(
            on_release=self.go_home
        )

        self.layout.add_widget(self.title)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

    def show_result(self, result):
        """
        نمایش نتیجه موفق
        """

        self.result_label.markup = False
        self.result_label.text = str(result)

    def show_error(self, message):
        """
        نمایش خطا
        """

        self.result_label.markup = True

        self.result_label.text = (
            "[color=#ff4444]"
            + str(message)
            + "[/color]"
        )

    def clear(self):
        """
        پاک کردن نتیجه قبلی
        """

        self.result_label.markup = False
        self.result_label.text = ""

    def go_home(self, instance):

        self.clear()

        self.manager.current = "home"

