# from ship import Ship
# from util import Symbol


# class Board:
#     def __init__(self, size: int):
#         self.size = size
#         # Let's call Board.board game_board for now
#         # self.board = [[Symbol.EMPTY.value for _ in range(size)] for _ in range(size)]
#         self.board = [[{'symbol': Symbol.EMPTY, 'ship': None} for _ in range(size)] for _ in range(size)]
        
        
#     def set_board_pos(self, pos: tuple[int, int], symbol: Symbol, ship: Ship) -> None:
#         col, row = pos
#         if not (0 <= col < self.size and 0 <= row < self.size):
#             raise IndexError("Out of bounds!")

#         self.board[row][col] = {
#             'symbol': symbol,
#             'ship': ship,
#         }

#     def draw_board(self) -> None:
#         for row in self.board:
#             print(" ".join(cell['symbol'] for cell in row))
#         print("\n\n")

#     def clear_board(self) -> None:
#         self.board = [
#             [Symbol.EMPTY.value for _ in range(self.size)] for _ in range(self.size)
#         ]


from ship import Ship
from util import Symbol

class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[{'symbol': Symbol.EMPTY, 'ship': None} for _ in range(size)] for _ in range(size)]

    def set_board_pos(self, pos: tuple[int, int], symbol: Symbol, ship: Ship) -> None:
        col, row = pos
        if not (0 <= col < self.size and 0 <= row < self.size):
            raise IndexError("Out of bounds!")

        if self.board[row][col]['symbol'] != Symbol.EMPTY:
            raise ValueError("Position already occupied!")
        self.board[row][col] = {'symbol': symbol, 'ship': ship}
        ship.positions.append((col, row))

    def attack(self, pos: tuple[int, int]) -> bool:
        """Handles an attack and updates the board."""
        col, row = pos
        if not (0 <= col < self.size and 0 <= row < self.size):
            raise IndexError("Attack out of bounds!")

        cell = self.board[row][col]
        if cell['symbol'] in (Symbol.HIT, Symbol.MISS, Symbol.SUNK):
            print("You already attacked this position!")
            return False

        if cell['ship']:
            cell['symbol'] = Symbol.HIT
            cell['ship'].hits_remaining -= 1
            if cell['ship'].hits_remaining == 0:
                print("Ship sunk!")
                self.sink_ship(cell['ship'])
            return True
        else:
            cell['symbol'] = Symbol.MISS
            return False

    def sink_ship(self, ship: Ship) -> None:
        """Marks a ship as sunk on the board."""
        for col, row in ship.positions:
            self.board[row][col]['symbol'] = Symbol.SUNK

    def all_ships_sunk(self) -> bool:
        """Check if all ships on the board are sunk."""
        for row in self.board:
            for cell in row:
                if cell['ship'] and cell['symbol'] != Symbol.SUNK:
                    return False
        return True

    def draw_board(self, show_ships=True) -> None:
        for row in self.board:
            line = []
            for cell in row:
                if not show_ships and cell['symbol'] == Symbol.SHIP:
                    line.append(Symbol.EMPTY)
                else:
                    line.append(cell['symbol'])
            print(" ".join(line))
        print("\n")
