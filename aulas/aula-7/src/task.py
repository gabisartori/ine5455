from enum import Enum
class TaskStatus(Enum):
  OPEN = 0
  CLOSED = 1

class TaskPriority(Enum):
  LOW = 0
  MEDIAN = 1
  HIGH = 2

class TaskType(Enum):
  BUG = 0
  TASK = 1
  REFACTOR = 2

class Task:
  def __init__(self, title: str, priority: TaskPriority, type = TaskType.TASK):
    self.title: str = title
    self.status: TaskStatus = TaskStatus.OPEN
    self.owner = None
    self.project = None
    self.priority = priority
    self.type = type
    self.id = None

  def assign_to(self, employee):
    if employee not in self.project.get_employees():
      raise ValueError
    if self.status != TaskStatus.OPEN:
      raise ValueError
    employee.add_task(self)
    self.owner = employee

  def get_title(self) -> str:
    return self.title
  
  def get_status(self) -> TaskStatus:
    return self.status
  
  def get_owner(self):
    return self.owner
  
  def __gt__(self, other):
    return self.priority.value > other.priority.value
  
  def set_priority(self, priority):
    if self.status != TaskStatus.OPEN:
      raise ValueError
    self.priority = priority
  
  def close(self):
    if self.status == TaskStatus.CLOSED:
      raise ValueError
    
    self.status = TaskStatus.CLOSED
