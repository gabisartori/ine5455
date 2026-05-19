from enum import Enum
class TaskStatus(Enum):
  OPEN = 0
  CLOSED = 1

class Task:
  def __init__(self, title: str):
    self.title: str = title
    self.status: TaskStatus = TaskStatus.OPEN
    self.owner = None

  def assign_to(self, employee):
    employee.add_task(self)
    self.owner = employee

  def get_title(self) -> str:
    return self.title
  
  def get_status(self) -> TaskStatus:
    return self.status
  
  def get_owner(self):
    return self.owner