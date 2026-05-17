class Company:
  def __init__(self, name: str):
    self.name: str = name
    self.employees: list = []
  
  def get_name(self) -> str:
    return self.name

  def add_project(self, project):
    project.company = self
  
  def add_employee(self, employee):
    self.employees.append(employee)
    employee.company = self

  def get_employees(self) -> list:
    return self.employees