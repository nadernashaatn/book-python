"""
* Assignment: Numpy Slice 1
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Print inner 2x2 elements
    3. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wybierz wewnętrzne 2x2 elementy
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([[8, 4],
           [5, 2]])
"""


# Given
import numpy as np


DATA = np.array([
    [2, 8, 1, 5],
    [8, 8, 4, 4],
    [5, 5, 2, 5],
    [1, 0, 6, 0],
])


result = ...


# Solution
result = DATA[1:3, 1:3]
