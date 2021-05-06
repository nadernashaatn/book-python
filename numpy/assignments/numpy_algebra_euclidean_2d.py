"""
* Assignment: Numpy Algebra Euclidean 2D
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Use code from "Input" section (see below)
    2. Given are two points `a: tuple[int, int]` and `b: tuple[int, int]`
    3. Coordinates are in cartesian system
    4. Points `a` and `b` are in two dimensional space
    5. Calculate distance between points using Euclidean algorithm
    X. Run doctests - all must succeed

Polish:
    1. Użyj kodu z sekcji "Input" (patrz poniżej)
    2. Dane są dwa punkty `a: tuple[int, int]` i `b: tuple[int, int]`
    3. Koordynaty są w systemie kartezjańskim
    4. Punkty `a` i `b` są w dwuwymiarowej przestrzeni
    5. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> a = (1, 0)
    >>> b = (0, 1)
    >>> euclidean_distance(a, b)
    1.4142135623730951

    >>> euclidean_distance((0,0), (1,0))
    1.0

    >>> euclidean_distance((0,0), (1,1))
    1.4142135623730951

    >>> euclidean_distance((0,1), (1,1))
    1.0

    >>> euclidean_distance((0,10), (1,1))
    9.055385138137417
"""


# Given
from math import sqrt


def euclidean_distance(a, b):
    pass


# Solution
def euclidean_distance(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    return sqrt((x2-x1)**2 + (y2-y1)**2)
