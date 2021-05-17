"""
* Assignment: Numpy Concatenation
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Given are one-dimensional: `a: np.ndarray`, `b: np.ndarray`
    2. Concatenate them as `result: np.ndarray`
    3. Reshape `result` into two rows and three columns
    4. Run doctests - all must succeed

Polish:
    1. Dane są jednowymiarowe: `a: np.ndarray`, `b: np.ndarray`
    2. Połącz je ze sobą jako `result: np.ndarray`
    3. Przekształć `result` w dwa wiersze na trzy kolumny
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([[1, 2, 3],
           [4, 5, 6]])
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = ...


# Solution
result = np.concatenate((a, b)).reshape(2, 3)
