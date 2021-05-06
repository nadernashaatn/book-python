"""
* Assignment: Numpy Broadcasting Arithmetic
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. For given: `a: np.ndarray`, `b: np.ndarray`, `c: np.ndarray`
    3. Calculate square root of each element in `a` and `b`
    4. Calculate second power (square) of each element in `c`
    5. Add elements from `a` to `b`
    6. Multiply the result by `c`
    7. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dla danych: `a: np.ndarray`, `b: np.ndarray`, `c: np.ndarray`
    3. Oblicz pierwiastek kwadratowy każdego z elementu w `a` i `b`
    4. Oblicz drugą potęgę (kwadrat) każdego z elementu w `c`
    5. Dodaj elementy z `a` do `b`
    6. Przemnóż wynik przez `c`
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'numpy.ndarray'>

    >>> result
    array([[ 1.41421356,  2.73205081],
           [45.254834  ,  0.        ]])
"""


# Given
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
