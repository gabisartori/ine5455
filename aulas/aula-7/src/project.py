class Project:
  def __init__(self, title: str):
    self.title: str = title
    self.company = None
    self.employees: list = []

  def add_employee(self, employee):
    if employee not in self.company.get_employees(): raise ValueError
    if employee in self.employees: raise ValueError
    self.employees.append(employee)
    employee.add_project(self)
 
  def get_title(self) -> str:
    return self.title

  def get_company(self):
    return self.company
  
  def get_employees(self) -> list:
    return self.employees