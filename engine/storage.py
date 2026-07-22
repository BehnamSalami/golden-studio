```python
import sqlite3
from pathlib import Path


class Storage:
    """
    مدیریت پایگاه داده Golden Studio
    """

    def __init__(self):

        self.db_path = Path("golden.db")

        self.connection = sqlite3.connect(
            self.db_path
        )

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS projects(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                name TEXT NOT NULL,

                code TEXT NOT NULL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        self.connection.commit()

    def save_project(
        self,
        name: str,
        code: str
    ):

        self.cursor.execute(

            """
            INSERT INTO projects
            (
                name,
                code
            )

            VALUES
            (
                ?,
                ?
            )
            """,

            (
                name,
                code
            )
        )

        self.connection.commit()

        return self.cursor.lastrowid

    def get_projects(self):

        self.cursor.execute(

            """
            SELECT

                id,

                name,

                created_at,

                updated_at

            FROM projects

            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()

    def load_project(
        self,
        project_id
    ):

        self.cursor.execute(

            """
            SELECT *

            FROM projects

            WHERE id=?
            """,

            (
                project_id,
            )
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

                code=?,

                updated_at=CURRENT_TIMESTAMP

            WHERE id=?
            """,

            (
                name,
                code,
                project_id
            )
        )

        self.connection.commit()

    def delete_project(
        self,
        project_id
    ):

        self.cursor.execute(

            """
            DELETE

            FROM projects

            WHERE id=?
            """,

            (
                project_id,
            )
        )

        self.connection.commit()

    def close(self):

        self.connection.close()
```
