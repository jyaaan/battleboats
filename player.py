from main import Board
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
        self.board_size = board_size

    def place_ship(self):
        print(f"{self.name}, place your ships!")

        coordinates = input("row, col")
        row, col = map(int, coordinates.split(","))

        if (row - 1) not in range(self.board_size) or (col - 1) not in range(
            self.board_size
        ):
            raise IndexError("Invalid input")

        direction = input("up/down/left/right")
        if direction not in directions:
            raise ValueError("invalid direction")
        next_ship_coor = directions[direction]
        self.board.set_board_pos((row, col), Symbol.SHIP.value)
        self.board.set_board_pos(
            (row + next_ship_coor[0], col + next_ship_coor[1]), Symbol.SHIP.value
        )

    def display_board(self):
        self.board.draw_board()


if __name__ == "__main__":
    player = Player(1, "hank", 10)
    player.place_ship()
    player.display_board()
