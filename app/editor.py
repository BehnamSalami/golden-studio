from engine.storage import Storage


class ProjectManager:
    """
    مدیریت پروژه‌های Golden Studio
    """

    def __init__(self):

        self.storage = Storage()

    def create_project(
        self,
        name: str,
        code: str = ""
    ):
        """
        ایجاد پروژه جدید
        """

        return self.storage.save_project(
            name,
            code
        )

    def get_projects(self):
        """
        دریافت لیست پروژه‌ها
        """

        return self.storage.get_projects()

    def open_project(
        self,
        project_id: int
    ):
        """
        باز کردن پروژه
        """

        return self.storage.load_project(
            project_id
        )

    def update_project(
        self,
        project_id: int,
        name: str,
        code: str
    ):
        """
        بروزرسانی پروژه
        """

        return self.storage.update_project(
            project_id,
            name,
            code
        )

    def save_project(
        self,
        project_id: int,
        name: str,
        code: str
    ):
        """
        سازگاری با نسخه‌های قبلی
        """

        return self.update_project(
            project_id,
            name,
            code
        )

    def delete_project(
        self,
        project_id: int
    ):
        """
        حذف پروژه
        """

        return self.storage.delete_project(
            project_id
        )

    def close(self):
        """
        بستن اتصال دیتابیس
        """

        self.storage.close()