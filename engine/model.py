from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass
class Project:
    id: str
    name: str
    project_type: str
    description: str
    created_at: str
    updated_at: str
    version: str = "1.0"
    favorite: bool = False

    @classmethod
    def create(cls, name, project_type, description=""):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return cls(
            id=str(uuid.uuid4()),
            name=name,
            project_type=project_type,
            description=description,
            created_at=now,
            updated_at=now
        )

    def touch(self):
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")