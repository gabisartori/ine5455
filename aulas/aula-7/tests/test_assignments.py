import unittest
from src.company import Company
from src.employee import Employee
from src.project import Project
from src.task import Task, TaskPriority

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

    task = Task("Corrigir bug na tela inicial", TaskPriority.MEDIAN)
    project.add_task(task)

    self.assertEqual(task, project.get_tasks()[0])

  def test_assign_task_to_employee(self):
    company = Company("W")
    employee = Employee("João")
    project = Project("Site")
    company.add_project(project)
    company.add_employee(employee)
    task = Task("Bug na tela inicial", TaskPriority.MEDIAN)
    project.add_employee(employee)
    project.add_task(task)

    task.assign_to(employee)
    self.assertEqual(employee, task.get_owner())
    self.assertEqual(task, employee.get_tasks()[0])
  
  def test_assign_task_to_employee_not_in_tasks_project(self):
    company = Company("W")
    employee = Employee("João")
    project = Project("Site")
    company.add_project(project)
    company.add_employee(employee)
    task = Task("Bug na tela inicial", TaskPriority.MEDIAN)
    project.add_task(task)

    with self.assertRaises(ValueError):
      task.assign_to(employee)
  
  def test_change_task_owner(self):
    w = Company("W")
    john = Employee("João")
    maria = Employee("Maria")
    website = Project("Site de alunos")
    refactoring = Task("Refatorar codebase", TaskPriority.LOW)
    
    w.add_employee(john)
    w.add_employee(maria)
    w.add_project(website)
    website.add_employee(john)
    website.add_employee(maria)
    website.add_task(refactoring)
    
    refactoring.assign_to(john)
    refactoring.assign_to(maria)

    self.assertEqual(maria, refactoring.owner)
    self.assertEqual(refactoring, maria.get_tasks()[0])

  def test_change_owner_of_closed_task(self):
    w = Company("W")
    john = Employee("João")
    maria = Employee("Maria")
    website = Project("Site de alunos")
    refactoring = Task("Refatorar codebase", TaskPriority.LOW)
    
    w.add_employee(john)
    w.add_employee(maria)
    w.add_project(website)
    website.add_employee(john)
    website.add_employee(maria)
    website.add_task(refactoring)
    
    refactoring.assign_to(john)
    refactoring.close()
    with self.assertRaises(ValueError):
      refactoring.assign_to(maria)

  def test_add_task_to_project(self):
    w = Company("W")
    john = Employee("João")
    w.add_employee(john)
    website = Project("Site legal")
    w.add_project(website)
    website.add_employee(john)

    bug_home_screen = Task("Corrigir bug na tela inicial", TaskPriority.MEDIAN)
    refactor_code_base = Task("Refatorar codebase", TaskPriority.LOW)
    create_security_system = Task("Implementar método de segurança", TaskPriority.HIGH)
    create_login_page = Task("Criar página de login", TaskPriority.HIGH)

    website.add_task(bug_home_screen)
    website.add_task(refactor_code_base)
    website.add_task(create_security_system)
    website.add_task(create_login_page)

    self.assertEqual(bug_home_screen, website.get_tasks()[0])
    self.assertEqual(refactor_code_base, website.get_tasks()[1])
    self.assertEqual(create_security_system, website.get_tasks()[2])
    self.assertEqual(create_login_page, website.get_tasks()[3])
    self.assertEqual(4, len(website.get_tasks()))

  def test_task_id(self):
    w = Company("W")
    john = Employee("João")
    w.add_employee(john)
    website = Project("Site legal")
    w.add_project(website)
    website.add_employee(john)

    bug_home_screen = Task("Corrigir bug na tela inicial", TaskPriority.MEDIAN)
    refactor_code_base = Task("Refatorar codebase", TaskPriority.LOW)
    create_security_system = Task("Implementar método de segurança", TaskPriority.HIGH)
    create_login_page = Task("Criar página de login", TaskPriority.HIGH)

    website.add_task(bug_home_screen)
    website.add_task(refactor_code_base)
    website.add_task(create_security_system)
    website.add_task(create_login_page)

    self.assertEqual(1, bug_home_screen.id)
    self.assertEqual(2, refactor_code_base.id)
    self.assertEqual(3, create_security_system.id)
    self.assertEqual(4, create_login_page.id)
    self.assertEqual(4, w.get_task_id_counter())