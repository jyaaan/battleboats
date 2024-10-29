"""
1. initialize board of some size using a new class
2. come up with data structure for storing game on board
3. find way to display board to terminal
4. find way to game logic or user input etc.

10/28
a. create players
b. take user input that places things on board. start with ships
c. validate entry

there are phases of the game


use grid
board = [[]]

symbols:
'•' = empty square
'S' = ship square
'M' = miss
'H' = hit, ship still afloat
'X' = hit, ship sunk
"""

import time

from board import Board
from util import Symbol

if __name__ == "__main__":
    board = Board(5)
    board.draw_board()
    time.sleep(2)
    board.set_board_pos((14, 2), Symbol.SHIP.value)
    board.draw_board()
