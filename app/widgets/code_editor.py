from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class CodeEditor(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        self.editor = MDTextField(
            hint_text="کد پایتون خود را اینجا بنویسید...",
            multiline=True,
            mode="outlined",
            size_hint_y=1
        )

        self.add_widget(self.editor)

    def get_code(self):
        """دریافت کد نوشته شده"""
        return self.editor.text

    def set_code(self, code):
        """قرار دادن کد داخل ویرایشگر"""
        self.editor.text = code

    def clear(self):
        """پاک کردن ویرایشگر"""
        self.editor.text = ""