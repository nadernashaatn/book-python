"""
* Assignment: Numpy Broadcasting Arithmetic
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. For given: `a: np.ndarray`, `b: np.ndarray`, `c: np.ndarray`
    2. Calculate square root of each element in `a` and `b`
    3. Calculate second power (square) of each element in `c`
    4. Add elements from `a` to `b`
    5. Multiply the result by `c`
    6. Run doctests - all must succeed

Polish:
    1. Dla danych: `a: np.ndarray`, `b: np.ndarray`, `c: np.ndarray`
    2. Oblicz pierwiastek kwadratowy każdego z elementu w `a` i `b`
    3. Oblicz drugą potęgę (kwadrat) każdego z elementu w `c`
    4. Dodaj elementy z `a` do `b`
    5. Przemnóż wynik przez `c`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'numpy.ndarray'>

    >>> result
    array([[ 1.41421356,  2.73205081],
           [45.254834  ,  0.        ]])
"""

import numpy as np


a = np.array([[0, 1], [2, 3]], float)
b = np.array([2, 3], float)
c = np.array([[1, 1], [4, 0]], float)

result = ...


# Solution
a = np.sqrt(a)
b = np.sqrt(b)
c = c ** 2

result = (a + b) * c
