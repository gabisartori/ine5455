class Employee:
  def __init__(self, name: str):
    self.name: str = name
  
  def get_name(self) -> str:
    return self.name
