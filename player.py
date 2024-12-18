# from main import Board
# from util import Symbol

# directions = {
#     "up": (0, -1),
#     "right": (1, 0),
#     "down": (0, 1),
#     "left": (-1, 0),
# }


# class Player:
#     def __init__(self, id: int, name: str, board_size: int):
#         self.id = id
#         self.name = name
#         self.board = Board(board_size)
#         self.board_size = board_size

#     def place_ship(self):
#         print(f"{self.name}, place your ships!")

#         coordinates = input("row, col")
#         row, col = map(int, coordinates.split(","))

#         if (row - 1) not in range(self.board_size) or (col - 1) not in range(
#             self.board_size
#         ):
#             raise IndexError("Invalid input")

#         direction = input("up/down/left/right")
#         if direction not in directions:
#             raise ValueError("invalid direction")
#         next_ship_coor = directions[direction]
#         self.board.set_board_pos((row, col), Symbol.SHIP.value)
#         self.board.set_board_pos(
#             (row + next_ship_coor[0], col + next_ship_coor[1]), Symbol.SHIP.value
#         )

#     def display_board(self):
#         self.board.draw_board()


# if __name__ == "__main__":
#     player = Player(1, "hank", 10)
#     player.place_ship()
#     player.display_board()


from board import Board
from ship import Ship
from util import Symbol

directions = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0),
}

class Player:
    def __init__(self, id: int, name: str, board_size: int):
        self.id = id
        self.name = name
        self.board = Board(board_size)
        self.ships = []

    def place_ships(self):
        """Allows player to place a predefined number of ships."""
        ship_sizes = [3, 2]  # Example: one 3-length ship and one 2-length ship
        for size in ship_sizes:
            print(f"Placing a ship of size {size}")
            while True:
                try:
                    row, col = map(int, input("Enter starting row and col: ").split())
                    direction = input("Enter direction (up/down/left/right): ").lower()
                    if direction not in directions:
                        raise ValueError("Invalid direction!")

                    new_ship = Ship(size)
                    for i in range(size):
                        next_col = col + i * directions[direction][0]
                        next_row = row + i * directions[direction][1]
                        self.board.set_board_pos((next_col, next_row), Symbol.SHIP, new_ship)

                    self.ships.append(new_ship)
                    self.display_board()
                    break
                except (IndexError, ValueError) as e:
                    print(f"Error: {e}. Try again.")

    def display_board(self, show_ships=True):
        print(f"{self.name}'s Board:")
        self.board.draw_board(show_ships=show_ships)
