"""
* Assignment: Numpy Indexing
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: np.ndarray`
    3. Add to `result` elements from `DATA` at indexes:
        a. row 0, column 2
        b. row 2, column 2
        c. row 0, column 0
        d. row 1, column 0
    4. `result` size must be 2x2
    5. `result` type must be float
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: np.ndarray`
    3. Dodaj do `result` elementy z `DATA` o indeksach:
        a. wiersz 0, kolumna 2
        b. wiersz 2, kolumna 2
        c. wiersz 0, kolumna 0
        d. wiersz 1, kolumna 0
    4. Rozmiar `result` musi być 2x2
    5. Typ `result` musi być float
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.zeros(shape, dtype)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([[3., 9.],
           [1., 4.]])
"""


# Given
import numpy as np


DATA = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

result = ...


# Solution
result = np.empty(shape=(2,2), dtype=float)
result[0,0] = DATA[0,2]
result[0,1] = DATA[2,2]
result[1,0] = DATA[0,0]
result[1,1] = DATA[1,0]

# ## Alternative Solution
# result = np.array([
#     DATA[0][2],
#     DATA[2][2],
#     DATA[0][0],
#     DATA[1][2],
# ], float).reshape(2, 2)
#
# ## Alternative Solution
# result = np.array([
#     [DATA[0,2], DATA[2,2]],
#     [DATA[0,0], DATA[1,0]],
# ], float)
