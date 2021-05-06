"""
* Assignment: OOP Overload Matmul
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use code from "Given" section (see below)
    2. Overload `@` operator
    3. Set position based on argument `tuple[int, int]`
    4. Run doctests - all must succeed

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Przeciąż operator `@`
    3. Ustaw pozycję na podstawie argumentu `tuple[int, int]`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> position = Position()
    >>> position
    Position(x=0, y=0)
    >>> position @ (1, 2)
    >>> position
    Position(x=1, y=2)
"""


# Given
from dataclasses import dataclass


@dataclass
class Position:
    x: int = 0
    y: int = 0


# Solution
@dataclass
class Position:
    x: int = 0
    y: int = 0

    def __matmul__(self, other: tuple[int, int]) -> None:
        self.x = other[0]
        self.y = other[1]
