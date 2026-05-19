from enum import Enum
class TaskStatus(Enum):
  OPEN = 0
  CLOSED = 1

class Task:
  def __init__(self, title: str):
    self.title: str = title
    self.status: TaskStatus = TaskStatus.OPEN

  def get_title(self) -> str:
    return self.title
  
  def get_status(self) -> TaskStatus.OPEN:
    return self.status