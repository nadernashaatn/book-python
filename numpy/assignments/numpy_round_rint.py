"""
* Assignment: Numpy Round Rint
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Round values to integers
    3. Convert data type to `np.int8`
    4. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zaokrąglij wartości do pełnych liczb całkowitych
    3. Przekonwertuj typ danych do `np.int8`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
          dtype=int8)
"""


# Given
import numpy as np


DATA = np.array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
                 0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152,
                 0.79172504, 0.52889492, 0.56804456, 0.92559664, 0.07103606,
                 0.0871293 , 0.0202184 , 0.83261985, 0.77815675, 0.87001215,
                 0.97861834])


result = ...


# Solution
result = np.rint(DATA).astype(np.int8)
