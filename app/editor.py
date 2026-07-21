from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

from app.widgets.code_editor import CodeEditor

from engine.controller import EngineController
from engine.project import ProjectManager


class EditorScreen(MDScreen):
    """
    صفحه ویرایش کد
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.controller = EngineController()

        self.project_manager = ProjectManager()

        self.project_id = None

        self.project_name = ""

        self.layout = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

        self.editor = CodeEditor()

        self.check_button = MDRaisedButton(
            text="بررسی کد",
            size_hint=(1, None),
            height=50
        )

        self.save_button = MDRaisedButton(
            text="ذخیره پروژه",
            size_hint=(1, None),
            height=50
        )

        self.check_button.bind(
            on_release=self.check_code
        )

        self.save_button.bind(
            on_release=self.save_project
        )

        self.layout.add_widget(self.editor)
        self.layout.add_widget(self.check_button)
        self.layout.add_widget(self.save_button)

        self.add_widget(self.layout)

    def load_project(
        self,
        project_id,
        project_name,
        code
    ):
        """
        بارگذاری پروژه
        """

        self.project_id = project_id

        self.project_name = project_name

        self.editor.set_code(code)

    def save_project(self, *args):
        """
        ذخیره پروژه
        """

        if self.project_id is None:
            return

        code = self.editor.get_code()

        self.project_manager.update_project(
            self.project_id,
            self.project_name,
            code
        )

        print("Project Saved")

    def check_code(self, instance):

        code = self.editor.get_code()

        try:

            form = self.controller.load_code(code)

            data_screen = self.manager.get_screen(
                "data"
            )

            data_screen.load_form(
                form=form,
                code=code
            )

            self.manager.current = "data"

        except Exception as error:

            print(
                "Parser Error:",
                error
            )

    def clear(self):
        """
        پروژه جدید
        """

        self.project_id = None

        self.project_name = ""

        self.editor.clear()