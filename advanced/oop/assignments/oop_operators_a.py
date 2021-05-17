"""
* Assignment: OOP Overload Matmul
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Overload `@` operator
    2. Set position based on argument `tuple[int, int]`
    3. Run doctests - all must succeed

Polish:
    1. Przeciąż operator `@`
    2. Ustaw pozycję na podstawie argumentu `tuple[int, int]`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> position = Position()
    >>> position
    Position(x=0, y=0)
    >>> position @ (1, 2)
    >>> position
    Position(x=1, y=2)
"""

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
