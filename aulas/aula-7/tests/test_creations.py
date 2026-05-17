import unittest
from src.company import Company
from src.employee import Employee
from src.project import Project

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

  def test_add_employee_to_company(self):
    company = Company("W")
    employee = Employee("João")
    company.add_employee(employee)
    self.assertEqual("João", company.get_employees()[0].get_name())

  def test_create_project_and_verify_attribution_to_company(self):
    company = Company("W")
    project = Project("Site de alunos")
    company.add_project(project)
    self.assertEqual("W", project.get_company().get_name())

  def test_assign_employee_to_project(self):
    company = Company("W")
    project = Project("Site de alunos")
    employee = Employee("João")
    company.add_employee(employee)
    company.add_project(project)

    project.add_employee(employee)
    self.assertEqual("Site de alunos", employee.get_projects()[0].get_title())
    self.assertEqual("João", project.get_employees()[0].get_name())

  def test_assign_inexistent_employee_to_project(self):
    """This test should fail since the created employee has not been registred as one of the company's employees"""
    company = Company("W")
    project = Project("Site de alunos")
    employee = Employee("João")
    company.add_project(project)
    with self.assertRaises(ValueError):
      project.add_employee(employee)
