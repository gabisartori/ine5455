import unittest
from src.company import Company
from src.employee import Employee
from src.project import Project
from src.task import Task

class TestAssignments(unittest.TestCase):
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

  def test_company_can_have_multiple_employees(self):
    company = Company("W")
    employee_1 = Employee("João")
    employee_2 = Employee("Maria")

    company.add_employee(employee_1)
    company.add_employee(employee_2)

    self.assertEqual(employee_1, company.get_employees()[0])
    self.assertEqual(employee_2, company.get_employees()[1])

  def test_project_can_have_multiple_employees(self):
    company = Company("W")
    employee_1 = Employee("João")
    employee_2 = Employee("Maria")
    company.add_employee(employee_1)
    company.add_employee(employee_2)
    project = Project("Site legal")
    company.add_project(project)

    project.add_employee(employee_1)
    project.add_employee(employee_2)

    self.assertEqual(employee_1, project.get_employees()[0])
    self.assertEqual(employee_2, project.get_employees()[1])

  def test_assign_employee_to_project_their_already_assigned_to(self):
    company = Company("W")
    employee_1 = Employee("João")
    company.add_employee(employee_1)
    project = Project("Site legal")
    company.add_project(project)

    project.add_employee(employee_1)
    with self.assertRaises(ValueError):
      project.add_employee(employee_1)

  def test_repeat_employee_addition_to_company(self):
    company = Company("W")
    employee_1 = Employee("João")
    company.add_employee(employee_1)
    with self.assertRaises(ValueError):
      company.add_employee(employee_1)

  def test_add_task_to_project(self):
    company = Company("W")
    employee = Employee("João")
    company.add_employee(employee)
    project = Project("Site legal")
    company.add_project(project)
    project.add_employee(employee)

    task = Task("Corrigir bug na tela inicial")
    project.add_task(task)

    self.assertEqual(task, project.get_tasks()[0])

  def test_assign_task_to_employee(self):
    company = Company("W")
    employee = Employee("João")
    project = Project("Site")
    company.add_project(project)
    company.add_employee(employee)
    task = Task("Bug na tela inicial")
    project.add_task(task)

    task.assign_to(employee)
    self.assertEqual(employee, task.get_owner())
    self.assertEqual(task, employee.get_tasks()[0])
