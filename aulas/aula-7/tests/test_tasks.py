import unittest

from src.task import Task, TaskPriority

class TestTaks(unittest.TestCase):
  def test_task_priority(self):
    minor_task = Task("Refatorar página inicial", TaskPriority.LOW)
    major_task = Task("Criar módulo de segurança", TaskPriority.HIGH)

    self.assertTrue(major_task > minor_task)
