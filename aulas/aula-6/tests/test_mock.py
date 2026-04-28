import unittest
from unittest.mock import patch, Mock
from src.puzzle_game import PuzzleGame
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To1234X5786
from src.puzzle_game_with_mock import PuzzleGameWithPlayer


class TestGetTile(unittest.TestCase):
  def setUp(self):
    self.game = PuzzleGame(3)
    shuffler = TestingShufflerPuzzleGame3x3To1234X5786()
    shuffler.shuffle(self.game)

  def test_get_empty_tile(self):
    value = self.game.get_tile(2, 2)
    self.assertEqual(value, " ")

  def test_get_first_tile(self):
    value = self.game.get_tile(1, 1)
    self.assertEqual(value, 1)

  @patch("src.puzzle_game.PuzzleGame.get_tile")
  def test_get_empty_tile_mocked(self, mock_puzzle_game_get_tile: Mock):
    mock_puzzle_game_get_tile.return_value = " "
    value = self.game.get_tile(2, 2)
    self.assertEqual(value, " ")

  @patch("src.puzzle_game.PuzzleGame.get_tile")
  def test_get_first_tile_mocked(self, mock_puzzle_game_get_tile: Mock):
    mock_puzzle_game_get_tile.return_value = 1
    value = self.game.get_tile(1, 1)
    self.assertEqual(value, 1)

class TestGameWithMock(unittest.TestCase):
  def setUp(self):
    self.game = PuzzleGameWithPlayer(3, "Sartori")
    shuffler = TestingShufflerPuzzleGame3x3To1234X5786()
    shuffler.shuffle(self.game)

  def test_game_not_finished(self):
    value = self.game.end_of_the_game()
    self.assertEqual(value, "Game not finished")

  def test_game_finished(self):
    self.game.move_empty_tile("RIGHT")
    self.game.move_empty_tile("DOWN")
    value = self.game.end_of_the_game()
    self.assertEqual(value, "Saved")

  @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
  def test_game_not_finished_mocked(self, puzzle_game_with_player_save_game_to_file_mock: Mock):
    puzzle_game_with_player_save_game_to_file_mock.return_value = "Saved"
    value = self.game.end_of_the_game()
    self.assertEqual(value, "Game not finished")

  @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
  def test_game_finished_mocked(self, puzzle_game_with_player_save_game_to_file_mock: Mock):
    puzzle_game_with_player_save_game_to_file_mock.return_value = "Saved"
    
    self.game.move_empty_tile("RIGHT")
    self.game.move_empty_tile("DOWN")
    value = self.game.end_of_the_game()
    self.assertEqual(value, "Saved")

if __name__ == '__main__':
  unittest.main()
