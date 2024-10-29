from enum import StrEnum


class Symbol(StrEnum):
    EMPTY = "•"
    SHIP = "S"
    MISS = "M"
    HIT = "H"
    SUNK = "X"
