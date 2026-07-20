from engine.model import Project
from engine.storage import ProjectStorage


class ProjectManager:

    def __init__(self):

        self.storage = ProjectStorage()

    def create_project(
        self,
        name,
        project_type="Python",
        description=""
    ):

        project = Project.create(
            name=name,
            project_type=project_type,
            description=description
        )

        self.storage.save(project)

        return project

    def open_project(self, project_id):

        return self.storage.load(project_id)

    def list_projects(self):

        return self.storage.get_all_projects()

    def delete_project(self, project_id):

        return self.storage.delete(project_id)