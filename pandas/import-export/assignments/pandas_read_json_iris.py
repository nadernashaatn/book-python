"""
* Assignment: Pandas Read JSON
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from `DATA` as `result: pd.DataFrame`
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z DATA jako result: pd.DataFrame
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> result.loc[[0,10,20]]
        sepalLength  sepalWidth  petalLength  petalWidth     species
    0           5.1         3.5          1.4         0.2      setosa
    10          7.0         3.2          4.7         1.4  versicolor
    20          6.3         3.3          6.0         2.5   virginica
"""


# Given
import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/iris.json'


# Solution
result = pd.read_json(DATA)
