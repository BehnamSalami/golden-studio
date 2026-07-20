import sqlite3
from pathlib import Path


class Storage:
    """
    مسئول ذخیره اطلاعات پروژه
    """

    def __init__(self):

        self.db_path = Path("golden.db")

        self.connection = sqlite3.connect(self.db_path)

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            code TEXT NOT NULL

        )
        """)

        self.connection.commit()

    def save_project(self, name: str, code: str):

        self.cursor.execute(
            """
            INSERT INTO projects(name,code)
            VALUES(?,?)
            """,
            (name, code)
        )

        self.connection.commit()

    def get_projects(self):

        self.cursor.execute("""
        SELECT id,name
        FROM projects
        ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    def load_project(self, project_id):

        self.cursor.execute(
            """
            SELECT *
            FROM projects
            WHERE id=?
            """,
            (project_id,)
        )

        return self.cursor.fetchone()

    def update_project(
        self,
        project_id,
        name,
        code
    ):

        self.cursor.execute(
            """
            UPDATE projects

            SET

            name=?,

            code=?

            WHERE id=?
            """,
            (
                name,
                code,
                project_id
            )
        )

        self.connection.commit()

    def delete_project(self, project_id):

        self.cursor.execute(

            """
            DELETE FROM projects

            WHERE id=?
            """,

            (project_id,)
        )

        self.connection.commit()

    def close(self):

        self.connection.close()