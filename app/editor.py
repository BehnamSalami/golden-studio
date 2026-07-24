from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

from app.widgets.code_editor import CodeEditor
from engine.controller import EngineController


class EditorScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.controller = EngineController()
        self.project_id = None
        self.project_name = ""

        self.layout = MDBoxLayout(orientation="vertical", padding=10, spacing=10)

        self.title = MDLabel(text="ویرایشگر کد", font_style="H5", halign="center")
        self.code_editor = CodeEditor()

        self.run_button = MDRaisedButton(text="اجرای کد و نمایش فرم")
        self.run_button.bind(on_release=self.run_code)

        self.layout.add_widget(self.title)
        self.layout.add_widget(self.code_editor)
        self.layout.add_widget(self.run_button)

        self.add_widget(self.layout)

    def load_project(self, project_id, name, code):
        self.project_id = project_id
        self.project_name = name
        self.title.text = f"ویرایش: {name}"
        self.code_editor.set_code(code)

    def run_code(self, instance):
        code = self.code_editor.get_code()
        if not code.strip():
            return

        try:
            form = self.controller.load_code(code)
            data_screen = self.manager.get_screen("data")
            data_screen.load_form(form, code)
            self.manager.current = "data"
        except Exception as e:
            # نمایش خطا
            result_screen = self.manager.get_screen("result")
            result_screen.show_error(str(e))
            self.manager.current = "result"