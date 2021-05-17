"""
* Assignment: Series Alter
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. From input data create `s: pd.Series`
    2. Drop values at index 2, 4, 6
    3. Drop duplicates
    4. Reindex series (without old copy)
    5. Run doctests - all must succeed

Polish:
    1. Z danych wejściowych stwórz `s: pd.Series`
    2. Usuń wartości na indeksach 2, 4, 6
    3. Usuń duplikujące się wartości
    4. Zresetuj indeks (bez kopii starego)
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> result
    0    1.0
    1    NaN
    2    2.0
    dtype: float64
"""

import pandas as pd

DATA = [1, None, 5, None, 1, 2, 1]

result = ...


# Solution
result = (pd.Series(DATA)
          .drop([2, 4, 6])
          .drop_duplicates()
          .reset_index(drop=True))


# ## Solution 1
# s = pd.Series(DATA)
# s.drop(2, inplace=True)
# s.drop(4, inplace=True)
# s.drop(6, inplace=True)
# s.drop_duplicates(inplace=True)
# s.reset_index(drop=True, inplace=True)
# result = s
#
# ## Solution 2
# s = pd.Series(DATA)
# s.drop([2, 4, 6], inplace=True)
# s.drop_duplicates(inplace=True)
# s.reset_index(drop=True, inplace=True)
#
#
# ## Solution 3
# s = pd.Series(DATA)
# s = s.drop([2, 4, 6])
# s = s.drop_duplicates()
# s = s.reset_index(drop=True)
#
# ## Solution 4
# s = pd.Series(DATA) \
#      .drop([2, 4, 6]) \
#      .drop_duplicates() \
#      .reset_index(drop=True)
