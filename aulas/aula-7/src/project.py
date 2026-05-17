class Project:
  def __init__(self, title: str):
    self.title: str = title
    self.company: str = None
    self.employees: list = []

  def add_employee(self, employee):
    self.employees.append(employee)
    employee.add_project(self)

  def get_title(self) -> str:
    return self.title

  def get_company(self) -> str:
    return self.company
  
  def get_employees(self) -> list:
    return self.employees