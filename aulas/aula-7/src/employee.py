class Employee:
  def __init__(self, name: str):
    self.name: str = name
    self.projects: list = []

  def add_project(self, project):
    self.projects.append(project)

  def get_name(self) -> str:
    return self.name

  def get_projects(self) -> list:
    return self.projects