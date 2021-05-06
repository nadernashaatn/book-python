"""
* Assignment: Mapping Generate Zip
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: dict`
    2. Using `zip()` convert data to `dict` and assign to `result`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict`
    2. Używając `zip()` przekonwertuj dane do `dict` i przypisz do `result`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>
    >>> all(type(x) is str for x in result.keys())
    True
    >>> ('Sepal length' in result.keys()
    ...  and 'Sepal width' in result.keys()
    ...  and 'Petal length' in result.keys()
    ...  and 'Petal width' in result.keys()
    ...  and 'Species' in result.keys())
    True
    >>> (5.8 in result.values()
    ...  and 2.7 in result.values()
    ...  and 5.1 in result.values()
    ...  and 1.9 in result.values()
    ...  and 'virginica' in result.values())
    True

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Sepal length': 5.8,
     'Sepal width': 2.7,
     'Petal length': 5.1,
     'Petal width': 1.9,
     'Species': 'virginica'}
"""

KEYS = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
VALUES = [5.8, 2.7, 5.1, 1.9, 'virginica']

result = ...  # dict[str,float|str]: converted zipped KEYS and VALUES

# Solution
result = dict(zip(KEYS, VALUES))
