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
from ship import Ship
from util import Symbol
from player import Player

# def main():
#     print("Welcome to Battleboats!")
#     size = int(input("Enter the size of the board: "))
#     board = Board(size)

#     print("Initial Board:")
#     board.draw_board()

#     while True:
#         try:
#             # Get user input for ship placement
#             row, col = map(int, input(f"Enter the row and column (0-{size-1}) to place a ship, separated by a space: ").split())
            
#             # Place the ship
#             tiny_ship = Ship(size=1)
#             board.set_board_pos((col, row), Symbol.SHIP, tiny_ship)
            
#             # Display updated board
#             print("Updated Board:")
#             board.draw_board()
#         except IndexError:
#             print(f"Invalid position! Please enter values between 0 and {size-1}.")
#         except ValueError:
#             print("Invalid input! Please enter two numbers separated by a space.")
#         except KeyboardInterrupt:
#             print("\nExiting game. Goodbye!")
#             break

# #Still need to add:
#     #message in case user re-enters same coordinates
#     #track which squares belong to which ship (multiple S's in different arrangements could get confusing)

# # board = [[Symbol.EMPTY for _ in range(size)] for _ in range(size)] => size x size grid, each cell contains a Symbol
# # ships = {
# #     'S2': 0,
# # }
# # Enemy cruiser sunk.
# # (1, 2)
# # board = [[{'symbol': Symbol.HIT, 'ship_id': 'S2'} for _ in range(size)] for _ in range(size)] => size x size grid, each cell contains a Symbol
# # (2, 2)
# # also a hit on S2
# # SUNK
# # board = [[{'symbol': Symbol.HIT, 'ship': Ship()} for _ in range(size)] for _ in range(size)] => size x size grid, each cell contains a Symbol
# # Ship(
# #     'name': 'Cruiser',
# #     'hits_remaining': 0,
# #     'positions': [(1, 2), (2, 2)],
# # )
# # board.sink_ship(ship.positions)
# # hits = [(3, 4), (4, 4)]
# # misses = [(1, 3), (5, 6)]


# if __name__ == "__main__":
#     # board = Board(5)
#     # board.draw_board()
#     # time.sleep(2)
#     # board.set_board_pos((2, 2), Symbol.SHIP.value)
#     # board.draw_board()
#     main()



def setup_game():
    print("Welcome to Battleboats!")
    board_size = int(input("Enter the size of the board (e.g., 8): "))
    player1 = Player(1, "Player 1", board_size)
    player2 = Player(2, "Player 2", board_size)

    # Setup Phase: Place Ships
    for player in [player1, player2]:
        print(f"\n{player.name}, place your ships!")
        player.place_ships()
        print(f"{player.name}'s Board:")
        player.display_board()
        time.sleep(1)

    return player1, player2


def attack_phase(player1, player2):
    """Attack phase where players alternate turns."""
    print("\nLet the battle begin!")
    current_player, opponent = player1, player2

    while True:
        print(f"\n{current_player.name}'s Turn")
        opponent.display_board(show_ships=False)

        row, col = map(int, input("Enter coordinates to attack (row col): ").split())
        if opponent.board.attack((col, row)):
            print("Hit!")
        else:
            print("Miss!")

        if opponent.board.all_ships_sunk():
            print(f"\n{current_player.name} wins! All enemy ships are sunk.")
            break

        # Swap turns
        current_player, opponent = opponent, current_player


def main():
    player1, player2 = setup_game()
    attack_phase(player1, player2)


if __name__ == "__main__":
    main()