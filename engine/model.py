from dataclasses import dataclass
from datetime import datetime


@dataclass
class Project:

    id: str

    name: str

    project_type: str

    created_at: str

    updated_at: str

    description: str = ""

    favorite: bool = False

    version: str = "1.0"

    @staticmethod
    def create(name, project_type, description=""):

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return Project(

            id=now.replace("-", "").replace(":", "").replace(" ", ""),

            name=name,

            project_type=project_type,

            created_at=now,

            updated_at=now,

            description=description

        )