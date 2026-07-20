import json
from pathlib import Path
from dataclasses import asdict

from engine.model import Project


class ProjectStorage:

    def __init__(self):

        self.projects_folder = Path("user_projects")

        self.projects_folder.mkdir(exist_ok=True)

    def save(self, project: Project):

        project_folder = self.projects_folder / project.id

        project_folder.mkdir(exist_ok=True)

        project_file = project_folder / "project.json"

        with open(project_file, "w", encoding="utf-8") as file:

            json.dump(
                asdict(project),
                file,
                ensure_ascii=False,
                indent=4
            )

    def load(self, project_id):

        project_file = self.projects_folder / project_id / "project.json"

        if not project_file.exists():

            return None

        with open(project_file, "r", encoding="utf-8") as file:

            data = json.load(file)

        return Project(**data)

    def get_all_projects(self):

        projects = []

        for folder in self.projects_folder.iterdir():

            if folder.is_dir():

                project_file = folder / "project.json"

                if project_file.exists():

                    with open(project_file, "r", encoding="utf-8") as file:

                        data = json.load(file)

                    projects.append(Project(**data))

        return projects

    def delete(self, project_id):

        project_folder = self.projects_folder / project_id

        if not project_folder.exists():

            return False

        for file in project_folder.iterdir():

            file.unlink()

        project_folder.rmdir()

        return True
