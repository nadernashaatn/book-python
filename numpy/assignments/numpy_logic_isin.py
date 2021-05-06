"""
* Assignment: Numpy Logic Isin
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Set random seed to zero
    2. Generate `a: np.ndarray` of 50 random integers from 0 to 100 (exclusive)
    3. Generate `b: np.ndarray` with sequential powers of 2 and exponential from 0 to 6 (inclusive)
    4. Check which elements from `a` are present in `b`
    5. Result assign to `result`
    X. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    2. Wygeneruj `a: np.ndarray` z 50 losowymi liczbami całkowitymi od 0 do 100 (rozłącznie)
    3. Wygeneruj `b: np.ndarray` z kolejnymi potęgami liczby 2, wykładnik od 0 do 6 (włącznie)
    4. Sprawdź, które elementy z `a` są obecne w `b`
    5. Wynik przypisz do `result`
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([False, False,  True, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False,
           False, False, False, False,  True, False, False, False, False,
           False, False, False, False, False,  True, False, False, False,
            True, False, False, False, False])
"""


# Given
import numpy as np
np.random.seed(0)


result = ...


# Solution
a = np.random.randint(0, 100, size=50)
b = 2 ** np.arange(7)
result = np.isin(a, b)
