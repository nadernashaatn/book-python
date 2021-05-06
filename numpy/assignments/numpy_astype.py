"""
* Assignment: Numpy Dtype Astype
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Given `DATA: np.ndarray` (see below)
    3. Convert to `int` and save result as `result_int`
    4. Convert to `bool` and save result as `result_bool`
    5. What happened in each of those steps?
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dany `DATA: np.ndarray` (patrz sekcja input)
    3. Przekonwertuj do typu `int` i wynik zapisz jako `result_int`
    4. Przekonwertuj do typu `bool` i wynik zapisz jako `result_bool`
    5. Co się stało w każdym z tych kroków?
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result_int) is np.ndarray
    True
    >>> type(result_bool) is np.ndarray
    True
    >>> result_int
    array([[-1,  0,  1],
           [ 2,  3,  4]])
    >>> result_bool
    array([[ True, False,  True],
           [ True,  True,  True]])
"""


# Given
import numpy as np


DATA = np.array([[-1.1, 0.0, 1.1],
                 [2.2, 3.3, 4.4]])


result_int = ...
result_bool = ...

# Solution
result_int = DATA.astype(int)
result_bool = DATA.astype(bool)

