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
  def test_get_valid_tile_at_line_of_empty_position(self):
    # Mata Mutante 7
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
    tile = game.get_tile(2, 1)
    self.assertIsNotNone(tile)
    self.assertEqual(tile, 4)

  def test_get_tile_outside_board_with_negative_line_and_valid_column(self):
    # Mata Mutante 1
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1234X5786().shuffle(game)
    with self.assertRaises(InvalidPositionException):
      game.get_tile(-1, 1)
  
  def test_get_tile_at_line_greater_than_0_but_invalid_column(self):
    # Mata mutante 2
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1X3425786().shuffle(game)
    with self.assertRaises(InvalidPositionException):
      tile = game.get_tile(100, -1)

  def test_get_tile_at_line_0_valid_column(self):
    # Mata mutante 2
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1X3425786().shuffle(game)
    with self.assertRaises(InvalidPositionException):
      tile = game.get_tile(0, 1)

  def test_get_tile_at_line_greater_than_0_but_invalid_column(self):
    # Mata mutante 3
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1X3425786().shuffle(game)
    with self.assertRaises(InvalidPositionException):
      tile = game.get_tile(100, -1)

  def test_get_tile_at_last_line(self):
    # Mata mutante 4
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1X3425786().shuffle(game)
    tile = game.get_tile(3, 1)
    self.assertEqual(tile, 7)

  def test_get_tile_at_column_0_valid_line(self):
    # Mata mutante 2
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1X3425786().shuffle(game)
    with self.assertRaises(InvalidPositionException):
      tile = game.get_tile(1, 0)

  def test_get_tile_at_last_column(self):
    # Mata mutante 6
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1X3425786().shuffle(game)
    tile = game.get_tile(1, 3)
    self.assertEqual(tile, 3)

  # Testes da move_tile
  def test_movimento_com_sucesso(self):
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
    success = game.move_tile(5)
    self.assertTrue(success)

  def test_trocar_com_tile_dentro_do_tabuleiro_mas_nao_adjacente(self):
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1234X5786().shuffle(game)
    success = game.move_tile(1)
    self.assertFalse(success)
  
  def test_trocar_com_tile_fora_do_tabuleiro(self):
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1X3425786().shuffle(game)
    game.dic_positions_of_tiles.update({60: (30, 3)})
    success = game.move_tile(60)
    self.assertFalse(success)

  def test_verifica_tile_apos_movimento(self):
    # Mata Mutante 9
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
    success = game.move_tile(5)
    self.assertTrue(success)
    self.assertEqual(game.get_tile(2, 3), 5)

  def test_movimento_com_sucesso_verifica_peça_movida(self):
    # Mata mutante 8
    # Nesse caso, o tile 8 está na posição 3, 2. Mas o mutante irá ler como se estivess na posição 3, 3.
    # A posição vazia nesse tabuleiro é a 2, 2. A posição 3, 2 é adjacente mas a 3, 3 não.
    game = PuzzleGame(3)
    TestingShufflerPuzzleGame3x3To1234X5786().shuffle(game)
    success = game.move_tile(8)
    self.assertTrue(success)
 
