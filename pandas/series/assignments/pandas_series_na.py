"""
* Assignment: Series NA
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. From input data create `pd.Series`
    3. Fill first missing value with zero
    4. Drop missing values
    5. Reindex series (without old copy)
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Z danych wejściowych stwórz `pd.Series`
    3. Wypełnij pierwszą brakującą wartość zerem
    4. Usuń brakujące wartości
    5. Zresetuj indeks (bez kopii starego)
    6. Uruchom doctesty - wszystkie muszą się powieść
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> result
    0    1.0
    1    0.0
    2    5.0
    3    1.0
    4    2.0
    5    1.0
    dtype: float64
"""


# Given
import pandas as pd

DATA = [1, None, 5, None, 1, 2, 1]


# Solution
result = (pd.Series(DATA)
            .fillna(0, limit=1)
            .dropna()
            .reset_index(drop=True))


# Alternative Solution
# s = pd.Series(DATA)
# s = s.fillna(0, limit=1)
# s = s.dropna()
# s = s.reset_index(drop=True)

# Alternative Solution
# s = pd.Series(DATA)
# s.fillna(0, limit=1, inplace=True)
# s.dropna(inplace=True)
# s.reset_index(drop=True, inplace=True)
