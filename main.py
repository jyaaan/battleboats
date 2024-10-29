"""
1. initialize board of some size using a new class
2. come up with data structure for storing game on board
3. find way to display board to terminal
4. find way to game logic or user input etc.

1.
a. create board class
b. decide on characters to store game state.
c. allow for init of board of given size, resulting in empty board (test)

use grid
board = [[]]

symbols:
'•' = empty square
'S' = ship square
'M' = miss
'H' = hit, ship still afloat
'X' = hit, ship sunk
"""

from enum import StrEnum
import time


class Symbol(StrEnum):
    EMPTY = "•"
    SHIP = "S"
    MISS = "M"
    HIT = "H"
    SUNK = "X"


class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[Symbol.EMPTY.value for _ in range(size)] for _ in range(size)]

    def set_board_pos(self, pos: tuple[int, int], symbol: str) -> None:
        col, row = pos
        if not (0 <= col < self.size and 0 <= row < self.size):
            raise IndexError("Out of bounds!")

        self.board[row][col] = symbol

    def draw_board(self) -> None:
        for row in self.board:
            print(" ".join(row))
        print("\n\n")

    def clear_board(self) -> None:
        self.board = [
            [Symbol.EMPTY.value for _ in range(self.size)] for _ in range(self.size)
        ]


if __name__ == "__main__":
    board = Board(5)
    board.draw_board()
    time.sleep(2)
    board.set_board_pos((14, 2), Symbol.SHIP.value)
    board.draw_board()
