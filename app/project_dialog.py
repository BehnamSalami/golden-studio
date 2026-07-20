from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton, MDButtonText


class ProjectDialog:

    def __init__(self, on_create):

        self.on_create = on_create

        self.name_field = MDTextField(
            hint_text="نام پروژه"
        )

        self.dialog = MDDialog(
            headline_text="پروژه جدید",
            supporting_text="نام پروژه را وارد کنید.",
            content=self.name_field,
            buttons=[
                MDButton(
                    MDButtonText(text="انصراف"),
                    on_release=self.close
                ),
                MDButton(
                    MDButtonText(text="ایجاد"),
                    on_release=self.create
                )
            ]
        )

    def open(self):
        self.dialog.open()

    def close(self, *args):
        self.dialog.dismiss()

    def create(self, *args):

        project_name = self.name_field.text.strip()

        if project_name:

            self.on_create(project_name)

        self.dialog.dismiss()