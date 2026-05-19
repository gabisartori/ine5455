from enum import Enum
class TaskStatus(Enum):
  OPEN = 0
  CLOSED = 1

class Task:
  def __init__(self, title: str):
    self.title: str = title
    self.status: TaskStatus = TaskStatus.OPEN
    self.owner = None
    self.project = None

  def assign_to(self, employee):
    if employee not in self.project.get_employees():
      raise ValueError
    employee.add_task(self)
    self.owner = employee

  def get_title(self) -> str:
    return self.title
  
  def get_status(self) -> TaskStatus:
    return self.status
  
  def get_owner(self):
    return self.owner