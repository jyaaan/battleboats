import unittest

from main import Board

BOARD_SIZE = 5

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Board(BOARD_SIZE)

    def test_board_size(self):
        self.assertEqual(len(self.game.board[0]), BOARD_SIZE, "Board width does not match expected.")
        self.assertEqual(len(self.game.board), BOARD_SIZE, "Board height does not match expected.")

    def test_board_set_pos(self):
        self.game.clear_board()
        pos = (2, 1)
        symbol = 'S'
        self.game.set_board_pos(pos, symbol)
        self.assertEqual(self.game.board[pos[1]][pos[0]], symbol, "Expected symbol not found")

    def test_board_clear(self):
        self.game.clear_board()
        pos = (2, 1)
        symbol = 'S'
        self.game.set_board_pos(pos, symbol)
        self.assertEqual(self.game.board[pos[1]][pos[0]], symbol, "Expected symbol not found")
        self.game.clear_board()
        self.assertTrue(all(cell == '•' for row in self.game.board for cell in row), "Board is not clear")

if __name__ == '__main__':
    unittest.main()