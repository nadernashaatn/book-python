"""
* Assignment: Entry Test List of Dict
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Define `result: list[dict]`
    2. Convert `DATA` from `list[tuple]` to `list[dict]`
        a. key - name from the header
        b. value - numerical value or species name
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`
    2. Przekonwertuj `DATA` z `list[tuple]` do `list[dict]`
        a. klucz - nazwa z nagłówka
        b. wartość - wartość numeryczna lub nazwa gatunku
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result must be a list'

    >>> assert len(result) > 0, \
    'Result cannot be empty'

    >>> assert all(type(element) is dict for element in result), \
    'All elements in result must be a dict'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
     {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
     {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
     {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
     {'Sepal length': 6.4, 'Sepal width': 3.2, 'Petal length': 4.5, 'Petal width': 1.5, 'Species': 'versicolor'},
     {'Sepal length': 4.7, 'Sepal width': 3.2, 'Petal length': 1.3, 'Petal width': 0.2, 'Species': 'setosa'}]
"""

DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]


result: list


# Solution
header, *data = DATA
result = []

for row in data:
    paris = zip(header, row)
    result.append(dict(paris))
