"""
* Assignment: Pandas Series Attributes
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: dict` with:
        a. number of dimensions;
        b. number of elements;
        c. data type;
        e. shape.
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: dict` z:
        a. liczbę wymiarów,
        b. liczbę elementów,
        c. typ danych,
        e. kształt.
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is dict
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'number of dimensions': 1,
     'number of elements': 3,
     'data type': dtype('O'),
     'shape': (3,)}
"""


# Given
import pandas as pd

DATA = pd.Series(['a', 'b', 'c'])

result = {
    'number of dimensions': ...,
    'number of elements': ...,
    'data type': ...,
    'shape': ...,
}


# Solution
result = {
    'number of dimensions': DATA.ndim,
    'number of elements': DATA.size,
    'data type': DATA.dtype,
    'shape': DATA.shape,
}
