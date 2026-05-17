class Project:
  def __init__(self, title: str):
    self.title: str = title
    self.company = None
    self.employees: list = []

  def add_employee(self, employee):
    if employee in self.company.get_employees():
      self.employees.append(employee)
      employee.add_project(self)
    else:
      raise ValueError

  def get_title(self) -> str:
    return self.title

  def get_company(self):
    return self.company
  
  def get_employees(self) -> list:
    return self.employees