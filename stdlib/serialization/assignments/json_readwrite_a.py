"""
* Assignment: Serialization JSON Dump
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Extract from input a header and data
    2. Create `result: list[dict]`
        a. key - name from the header
        b. value - measurement or species
    3. Write structure to file `FILE` in JSON format
    4. Run doctests - all must succeed

Polish:
    1. Z danych wydziel nagłówek i pomiary
    2. Wygeneruj `result: list[dict]`
        a. klucz - nazwa z nagłówka
        b. wartość - wyniki pomiarów lub gatunek
    3. Zapisz strukturę do pliku `FILE` w formacie JSON
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'list'>
    >>> len(result) > 0
    True
    >>> all(type(row) is dict
    ...     for row in result)
    True
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)
    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    [{"Sepal length": 5.8, "Sepal width": 2.7, "Petal length": 5.1, "Petal width": 1.9, "Species": "virginica"},
     {"Sepal length": 5.1, "Sepal width": 3.5, "Petal length": 1.4, "Petal width": 0.2, "Species": "setosa"},
     {"Sepal length": 5.7, "Sepal width": 2.8, "Petal length": 4.1, "Petal width": 1.3, "Species": "versicolor"},
     {"Sepal length": 6.3, "Sepal width": 2.9, "Petal length": 5.6, "Petal width": 1.8, "Species": "virginica"},
     {"Sepal length": 6.4, "Sepal width": 3.2, "Petal length": 4.5, "Petal width": 1.5, "Species": "versicolor"},
     {"Sepal length": 4.7, "Sepal width": 3.2, "Petal length": 1.3, "Petal width": 0.2, "Species": "setosa"},
     {"Sepal length": 7.0, "Sepal width": 3.2, "Petal length": 4.7, "Petal width": 1.4, "Species": "versicolor"},
     {"Sepal length": 7.6, "Sepal width": 3.0, "Petal length": 6.6, "Petal width": 2.1, "Species": "virginica"},
     {"Sepal length": 4.9, "Sepal width": 3.0, "Petal length": 1.4, "Petal width": 0.2, "Species": "setosa"}]
"""

FILE = '_temporary.json'

DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa')]


# Solution
import json

header, *data = DATA
result = [dict(zip(header, row))
          for row in data]


with open(FILE, mode='w') as file:
    json.dump(result, file)
