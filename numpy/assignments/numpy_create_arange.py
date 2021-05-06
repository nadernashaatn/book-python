"""
* Assignment: Numpy Create Arange
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Create `a: np.ndarray` with even numbers from 0 to 100 (without 100)
    2. Numbers must be `float` type
    X. Run doctests - all must succeed

Polish:
    1. Stwórz `a: np.ndarray` z liczbami parzystymi od 0 do 100 (bez 100)
    2. Liczby muszą być typu `float`
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([ 0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20., 22., 24.,
           26., 28., 30., 32., 34., 36., 38., 40., 42., 44., 46., 48., 50.,
           52., 54., 56., 58., 60., 62., 64., 66., 68., 70., 72., 74., 76.,
           78., 80., 82., 84., 86., 88., 90., 92., 94., 96., 98.])
"""


# Given
import numpy as np


result = ...


# Solution
result = np.arange(0, 100, step=2, dtype=float)

