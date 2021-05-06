"""
* Assignment: Numpy Select Isin
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Set random seed to 0
    2. Generate `a: np.ndarray` of size 50x50
    3. `a` must contains random integers from 0 to 1024 inclusive
    4. Create `result: np.ndarray` with elements selected from `a` which are power of two
    5. Sort `result` in descending order
    X. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na 0
    2. Wygeneruj `a: np.ndarray` rozmiaru 50x50
    3. `a` musi zawierać losowe liczby całkowite z zakresu od 0 do 1024 włącznie
    4. Stwórz `result: np.ndarray` z elementami wybranymi z `a`, które są potęgami dwójki
    5. Posortuj `result` w kolejności malejącej
    X. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.isin(a, b)`
    * `np.flip(a)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([1024, 1024, 1024, 1024, 1024, 1024,  512,  512,  512,  512,  256,
            256,  256,  256,  256,  128,  128,  128,  128,  128,   64,   32,
             32,   32,   32,   32,   16,   16,   16,   16,   16,   16,    8,
              8,    4,    2,    2,    2,    2,    2])
"""


# Given
import numpy as np
np.random.seed(0)


result = ...


# Solution
a = np.random.randint(0, 1025, size=(50, 50))
selection = 2 ** np.arange(11)

mask = np.isin(a, selection)
result = a[mask]
result.sort()
result = np.flip(result)


# ## Alternative solution
# np.random.seed(0)
#
# MIN = 0
# MAX = 1025
# SIZE = (50, 50)
# SELECT = 2 ** np.arange(11)
#
#
# a = np.random.randint(MIN, MAX, size=SIZE)
# b = a[np.isin(a, SELECT)]
# result.sort()
# np.flip(result)
#
#
# ## Alternative solution
# sorted(a[np.isin(a, SELECT)], reverse=True)
