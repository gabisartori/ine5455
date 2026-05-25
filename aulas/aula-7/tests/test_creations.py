import unittest
from src.company import Company
from src.employee import Employee
from src.project import Project
from src.task import Task, TaskStatus, TaskPriority

class TestCreation(unittest.TestCase):
  def test_create_company(self):
    company = Company("W")
    self.assertEqual("W", company.get_name())

  def test_create_employee(self):
    employee = Employee("João")
    self.assertEqual("João", employee.get_name())

  def test_create_project(self):
    project = Project("Site de inscrição de alunos")
    self.assertEqual("Site de inscrição de alunos", project.get_title())

  def test_create_task(self):
    task = Task("Corrigir bug na página inicial", TaskPriority.MEDIAN)
    self.assertEqual("Corrigir bug na página inicial", task.get_title())
  
  def test_task_starts_with_open_status(self):
    task = Task("Corrigir bug na página incial", TaskPriority.MEDIAN)
    self.assertEqual(TaskStatus.OPEN, task.get_status())
