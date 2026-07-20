from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

from app.widgets.code_editor import CodeEditor

from engine.controller import EngineController


class EditorScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.engine = EngineController()

        layout = MDBoxLayout(
            orientation="vertical",
            padding=15,
            spacing=15
        )

        title = MDLabel(
            text="ویرایشگر پایتون",
            halign="center",
            font_style="Headline"
        )

        self.editor = CodeEditor()

        self.analyze_button = MDRaisedButton(
            text="بررسی کد",
            pos_hint={"center_x": 0.5}
        )

        self.analyze_button.bind(
            on_release=self.analyze_code
        )

        layout.add_widget(title)
        layout.add_widget(self.editor)
        layout.add_widget(self.analyze_button)

        self.add_widget(layout)

    def analyze_code(self, *args):

        code = self.editor.get_code()

        if not code.strip():
            print("کدی وارد نشده است.")
            return

        try:

            form = self.engine.load_code(code)

            print("====== فرم ساخته شد ======")
            print(form)

            if self.manager:
                data_screen = self.manager.get_screen("data")
                data_screen.build_form(form)
                self.manager.current = "data"

        except Exception as error:

            print("خطا در تحلیل کد")
            print(error)