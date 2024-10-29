from util import Symbol


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
