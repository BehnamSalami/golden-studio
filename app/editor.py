from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout

from app.widgets.code_editor import CodeEditor
from engine.controller import EngineController


class EditorScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.controller = EngineController()

        layout = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

        self.editor = CodeEditor()

        button = MDRaisedButton(
            text="بررسی کد"
        )

        button.bind(on_release=self.parse_code)

        layout.add_widget(self.editor)
        layout.add_widget(button)

        self.add_widget(layout)

    def parse_code(self, instance):

        code = self.editor.get_code()

        try:

            form = self.controller.load_code(code)

            self.manager.get_screen("data").load_form(form)

            self.manager.current = "data"

        except Exception as error:

            print(error)