from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

from app.code_editor import CodeEditor

from engine.controller import EngineController


class EditorScreen(MDScreen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.engine = EngineController()

        root = MDBoxLayout(

            orientation="vertical",

            spacing=10,

            padding=15

        )

        title = MDLabel(

            text="ویرایشگر پایتون",

            halign="center",

            font_style="Headline"

        )

        self.editor = CodeEditor()

        analyze_button = MDRaisedButton(

            text="بررسی کد",

            pos_hint={"center_x": .5}

        )

        analyze_button.bind(

            on_release=self.analyze_code

        )

        root.add_widget(title)

        root.add_widget(self.editor)

        root.add_widget(analyze_button)

        self.add_widget(root)

    def analyze_code(self, *args):

        code = self.editor.get_code()

        try:

            form = self.engine.load_code(code)

            print(form)

        except Exception as error:

            print(error)