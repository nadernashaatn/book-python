"""

* Assignment: Numpy Algebra Euclidean Ndim
* Complexity: easy
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Use code from "Input" section (see below)
    2. Given are two points `a: Sequence[int]` and `b: Sequence[int]`
    3. Coordinates are in cartesian system
    4. Points `a` and `b` are in n-dimensional space
    5. Points `a` and `b` must be in the same space
    6. Calculate distance between points using Euclidean algorithm
    X. Run doctests - all must succeed

Polish:
    1. Użyj kodu z sekcji "Input" (patrz poniżej)
    2. Dane są dwa punkty `a: Sequence[int]` i `b: Sequence[int]`
    3. Koordynaty są w systemie kartezjańskim
    4. Punkty `a` i `b` są w n-wymiarowej przestrzeni
    5. Punkty `b` i `b` muszą być w tej samej przestrzeni
    6. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    X. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `for n1,n2 in zip(a,b)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> euclidean_distance((0,0,1,0,1), (1,1))
    Traceback (most recent call last):
    ValueError: Points must be in the same dimensions

    >>> euclidean_distance((0,0,0), (0,0,0))
    0.0

    >>> euclidean_distance((0,0,0), (1,1,1))
    1.7320508075688772

    >>> euclidean_distance((0,1,0,1), (1,1,0,0))
    1.4142135623730951

    >>> euclidean_distance((0,0,1,0,1), (1,1,0,0,1))
    1.7320508075688772
"""


# Given
from math import sqrt


def euclidean_distance(a, b):
    pass


# Solution
def euclidean_distance(a, b):
    if len(a) != len(b):
        raise ValueError('Points must be in the same dimensions')

    under_sqrt = 0

    for n1, n2 in zip(a, b):
        under_sqrt += (n2-n1) ** 2

    return sqrt(under_sqrt)
