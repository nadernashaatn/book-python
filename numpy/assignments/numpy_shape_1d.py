"""
* Assignment: Numpy Shape 1d
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result_ravel` with result of flattening `DATA` using `.ravel()` method
    2. Define `result_flatten` with result of flattening `DATA` using `.flatten()` method
    3. Define `result_reshape` with result of reshaping `DATA` into 1x9
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result_ravel` z wynikiem spłaszczenia `DATA` używając metody `.ravel()`
    2. Zdefiniuj `result_flatten` z wynikiem spłaszczenia `DATA` używając metody `.flatten()`
    3. Zdefiniuj `result_reshape` z wynikiem zmiany kształtu `DATA` na 1x9
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result_ravel) is np.ndarray
    True
    >>> type(result_flatten) is np.ndarray
    True
    >>> type(result_reshape) is np.ndarray
    True
    >>> result_flatten
    array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> result_ravel
    array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> result_reshape
    array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
"""


# Given
import numpy as np


DATA = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


result_ravel = ...
result_flatten = ...
result_reshape = ...


# Solution
result_ravel = DATA.ravel()
result_flatten = DATA.flatten()
result_reshape = DATA.reshape(1, 9)

