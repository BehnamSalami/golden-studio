from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

from app.widgets.code_editor import CodeEditor
from engine.controller import EngineController


class EditorScreen(MDScreen):
    """
    صفحه ویرایش کد پایتون
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.controller = EngineController()

        self.layout = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

        # ویرایشگر کد
        self.editor = CodeEditor()

        # دکمه بررسی
        self.check_button = MDRaisedButton(
            text="بررسی کد",
            size_hint=(1, None),
            height=50
        )

        self.check_button.bind(
            on_release=self.check_code
        )

        self.layout.add_widget(self.editor)
        self.layout.add_widget(self.check_button)

        self.add_widget(self.layout)

    def check_code(self, instance):

        code = self.editor.get_code()

        try:

            form = self.controller.load_code(code)

            data_screen = self.manager.get_screen("data")

            data_screen.load_form(
                form=form,
                code=code
            )

            self.manager.current = "data"

        except Exception as error:

            print("Parser Error :", error)