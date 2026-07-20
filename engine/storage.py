import json
from pathlib import Path
from dataclasses import asdict

from engine.model import Project


class ProjectStorage:

    def __init__(self):

        self.base_path = Path("user_projects")

        self.base_path.mkdir(exist_ok=True)

    def save(self, project: Project):

        project_path = self.base_path / project.id

        project_path.mkdir(exist_ok=True)

        with open(project_path / "project.json", "w", encoding="utf-8") as file:

            json.dump(asdict(project), file, ensure_ascii=False, indent=4)

    def load(self, project_id):

        file_path = self.base_path / project_id / "project.json"

        if not file_path.exists():

            return None

        with open(file_path, "r", encoding="utf-8") as file:

            data = json.load(file)

        return Project(**data)

    def list_projects(self):

        projects = []

        for folder in self.base_path.iterdir():

            file_path = folder / "project.json"

            if file_path.exists():

                with open(file_path, "r", encoding="utf-8") as file:

                    projects.append(Project(**json.load(file)))

        return projects