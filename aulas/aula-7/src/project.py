class Project:
  def __init__(self, title: str):
    self.title: str = title
  
  def get_title(self) -> str:
    return self.title
