"""
* Assignment: OOP Dataclass Syntax
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Use Dataclass to define class `Point` with attributes:
        a. `x: int` with default value `0`
        b. `y: int` with default value `0`
    2. When `x` or `y` has negative value raise en exception `ValueError('Coordinate cannot be negative')`
    3. Use `datalass` and validation in `__post_init__()`
    4. Run doctests - all must succeed

Polish:
    1. Użyj Dataclass do zdefiniowania klasy `Point` z atrybutami:
        a. `x: int` z domyślną wartością `0`
        b. `y: int` z domyślną wartością `0`
    2. Gdy `x` lub `y` mają wartość ujemną podnieś wyjątek `ValueError('Coordinate cannot be negative')`
    3. Użyj `datalass` i walidacji w `__post_init__()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Point)
    >>> assert hasattr(Point, 'x')
    >>> assert hasattr(Point, 'y')

    >>> Point()
    Point(x=0, y=0)

    >>> Point(x=0, y=0)
    Point(x=0, y=0)

    >>> Point(x=1, y=2)
    Point(x=1, y=2)

    >>> Point(x=-1, y=0)
    Traceback (most recent call last):
    ValueError: Coordinate cannot be negative

    >>> Point(x=0, y=-1)
    Traceback (most recent call last):
    ValueError: Coordinate cannot be negative
"""


# Given
from dataclasses import dataclass


# Solution
@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError('Coordinate cannot be negative')
