"""
* Assignment: Series Create Float
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create `result: pd.Series` with 5 float numbers
    2. One of those values must be `None`
    X. Run doctests - all must succeed

Polish:
    1. Stwórz `result: pd.Series` z 5 liczbami zmiennoprzecinkowymi
    2. Jedną z tych wartości musi być `None`
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> result
    0    1.1
    1    2.2
    2    NaN
    3    4.4
    4    5.5
    dtype: float64
"""


# Given
import pandas as pd


result = ...


# Solution
data = [1.1, 2.2, None, 4.4, 5.5]
result = pd.Series(data)

