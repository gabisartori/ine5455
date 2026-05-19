class Employee:
  def __init__(self, name: str):
    self.name: str = name
    self.projects: list = []
    self.company = None
    self.tasks = []

  def add_project(self, project):
    self.projects.append(project)

  def add_task(self, task):
    self.tasks.append(task)

  def get_name(self) -> str:
    return self.name

  def get_projects(self) -> list:
    return self.projects
  
  def get_tasks(self) -> list:
    return self.tasks
