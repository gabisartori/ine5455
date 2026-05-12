class Project:
  def __init__(self, title: str):
    self.title: str = title
    self.company: str = None
  
  def get_title(self) -> str:
    return self.title

  def get_company(self) -> str:
    return self.company