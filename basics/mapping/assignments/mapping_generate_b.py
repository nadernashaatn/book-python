"""
* Assignment: Mapping Generate Enumerate
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: dict`
    2. Using `enumerate()` convert data to `dict` and assign to `result`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniu `result: dict`
    2. Używając `enumerate()` przekonwertuj dane do `dict` i przypisz do `result`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>
    >>> all(type(x) is int for x in result.keys())
    True
    >>> all(type(x) is str for x in result.values())
    True

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {0: 'setosa',
     1: 'versicolor',
     2: 'virginica'}
"""

DATA = ['setosa', 'versicolor', 'virginica']

result = ...  # dict[int,str]: converted enumeration of DATA

# Solution
result = dict(enumerate(DATA))
