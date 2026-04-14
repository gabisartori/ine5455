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

  def test_movimento_com_sucesso(self):
    # Path 1: 1 - 2 - 3(T) - 4(T) - 5
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
    success = game.move_tile(5)
    self.assertTrue(success)

  # Path 3: 1 - 2 - 3(T) - 4(F) - 7
  def test_trocar_com_tile_dentro_do_tabuleiro_mas_nao_adjacente(self):
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1234X5786().shuffle(game)
    success = game.move_tile(1)
    self.assertFalse(success)
  
  # Path 2: 1 - 2 - 3(F) - 7
  def test_trocar_com_tile_fora_do_tabuleiro(self):
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1X3425786().shuffle(game)
    game.dic_positions_of_tiles.update({60: (30, 3)})
    success = game.move_tile(60)
    self.assertFalse(success)
