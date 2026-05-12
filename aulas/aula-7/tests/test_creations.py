import unittest

class TestCreation(unittest.TestCase):
  def test_create_company(self):
    company = Company("W")
    self.assertEqual("W", company.get_name())

  # def test_create_employee(self):
  # def test_create_project(self):

