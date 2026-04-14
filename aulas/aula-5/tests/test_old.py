import unittest

from conteudo.puzzle_game import PuzzleGame, InvalidPositionException
from tests.shufflers_for_testing_puzzles import *


# Needed paths:
# All_c_uses/Some_p_uses
# - 1 - 2(T) - 4(F) - 6
# All_p_uses
# - 1 - 2(T) - 4(T) - 5
# - 1 - 2(F) - 3

class ClasseTestes(unittest.TestCase):
  # 1 - 2(T) - 4(F) - 6
  def test_get_valid_tile(self):
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
    tile = game.get_tile(1, 1)
    self.assertIsNotNone(tile)
    self.assertEqual(tile, 1)

  # 1 - 2(F) - 3
  def test_get_tile_outside_board(self):
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1234X5786().shuffle(game)
    with self.assertRaises(InvalidPositionException):
      game.get_tile(-1, -1)
  
  # 1 - 2(T) - 4(T) - 5
  def test_get_empty_position(self):
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1X3425786().shuffle(game)
    tile = game.get_tile(1, 2)
    self.assertEqual(tile, " ")