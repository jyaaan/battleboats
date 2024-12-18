
class Ship:
    def __init__(self, size: int):
        self.size = size
        self.positions: list[tuple[int, int]] = []
        self.hits_remaining: int = size