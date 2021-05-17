"""
* Assignment: Numpy Iteration
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use `for` to iterate over `DATA`
    2. Define `result: list[int]` with even numbers from `DATA`
    3. Run doctests - all must succeed

Polish:
    1. Używając `for` iteruj po `DATA`
    2. Zdefiniuj `result: list[int]` z liczbami parzystymi z `DATA`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `number % 2 == 0`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is list
    True
    >>> result
    [2, 4, 6, 8]
"""

import numpy as np


DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


result: list


# Solution
result = []

for value in DATA.ravel():
    if value % 2 == 0:
        result.append(value)


# ## Alternative solution
# for row in DATA:
#     for value in row:
#         if value % 2 == 0:
#             result.append(value)


