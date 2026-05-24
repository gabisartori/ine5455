import unittest

from src.task import Task, TaskPriority

class TestTaks(unittest.TestCase):
  def test_task_priority(self):
    minor_task = Task("Refatorar página inicial", TaskPriority.LOW)
    major_task = Task("Criar módulo de segurança", TaskPriority.HIGH)

    self.assertTrue(major_task > minor_task)

  def test_change_open_task_priority(self):
    minor_to_major_task = Task("Coisa que eu não dei muita bola de cara", TaskPriority.LOW)
    minor_to_major_task.set_priority(TaskPriority.MEDIAN)
    self.assertEqual(TaskPriority.MEDIAN, minor_to_major_task.priority)

  def test_change_closed_task_priority(self):
    minor_to_major_task = Task("Coisa que eu terminei antes de perceber que era mais importante", TaskPriority.LOW)
    minor_to_major_task.close()
    with self.assertRaises(ValueError):
      minor_to_major_task.set_priority(TaskPriority.HIGH)
