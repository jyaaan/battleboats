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


def main():
    print("Welcome to Battleboats!")
    size = int(input("Enter the size of the board: "))
    board = Board(size)

    print("Initial Board:")
    board.draw_board()

    while True:
        try:
            # Get user input for ship placement
            row, col = map(int, input(f"Enter the row and column (0-{size-1}) to place a ship, separated by a space: ").split())
            
            # Place the ship
            board.set_board_pos((col, row), Symbol.SHIP.value)
            
            # Display updated board
            print("Updated Board:")
            board.draw_board()
        except IndexError:
            print(f"Invalid position! Please enter values between 0 and {size-1}.")
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")
        except KeyboardInterrupt:
            print("\nExiting game. Goodbye!")
            break


if __name__ == "__main__":
    # board = Board(5)
    # board.draw_board()
    # time.sleep(2)
    # board.set_board_pos((2, 2), Symbol.SHIP.value)
    # board.draw_board()
    main()
