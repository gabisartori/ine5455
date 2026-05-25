class Company:
  def __init__(self, name: str):
    self.name: str = name
    self.employees: list = []
    self.projects: list = []
    self.task_id_counter = 0
  
  def get_name(self) -> str:
    return self.name

  def add_project(self, project):
    project.company = self
    self.projects.append(project)
  
  def add_employee(self, employee):
    if employee in self.employees:
      raise ValueError
    self.employees.append(employee)
    employee.company = self

  def get_employees(self) -> list:
    return self.employees
  
  def assign_task_id(self) -> int:
    self.task_id_counter += 1
    return self.task_id_counter
  
  def get_task_id_counter(self) -> int:
    return self.task_id_counter
  
  def get_task_by_id(self, id):
    for project in self.projects:
      for task in project.tasks:
        if task.id == id:
          return task
    raise ValueError("Ocorrência não encontrada")