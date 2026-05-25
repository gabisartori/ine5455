import unittest

from src.task import Task, TaskPriority, TaskType

class TestTasks(unittest.TestCase):
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

  def test_close_closed_task(self):
    bug_fixing_task = Task("Corrigir Bug na tela inicial", TaskPriority.LOW)
    bug_fixing_task.close()
    with self.assertRaises(ValueError):
      bug_fixing_task.close()

  def test_check_task_type_bug(self):
    bug_fixing_task = Task("Corrigir bug na tela inicial", TaskPriority.MEDIAN, TaskType.BUG)
    self.assertEqual(TaskType.BUG, bug_fixing_task.type)

  def test_check_task_type_refactor(self):
    refactoring_task = Task("Refatorar codebase", TaskPriority.MEDIAN, TaskType.REFACTOR)
    self.assertEqual(TaskType.REFACTOR, refactoring_task.type)

  def test_check_task_type_task(self):
    task_task = Task("Criar sistema de segurança", TaskPriority.MEDIAN, TaskType.TASK)
    self.assertEqual(TaskType.TASK, task_task.type)
