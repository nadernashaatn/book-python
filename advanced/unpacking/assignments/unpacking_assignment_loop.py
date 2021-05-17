"""
* Assignment: Unpacking Assignment Loop
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Iterate over data splitting `*features` from `label`
    2. Define `result: list[str]` with species names ending with "ca" or "osa"
    3. Run doctests - all must succeed

Polish:
    1. Iteruj po danych rozdzielając `*features` od `label`
    2. Zdefiniuj `result: list[str]` z nazwami gatunków kończącymi się na "ca" lub "osa"
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.endswith()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'list'>
    >>> len(result) > 0
    True
    >>> assert all(type(x) is str for x in result)
    >>> result
    ['virginica', 'setosa', 'virginica', 'setosa']
"""

DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]

SUFFIXES = ('ca', 'osa')

result: list


# Solution
result = [label
          for *features, label in DATA[1:]
          if label.endswith(SUFFIXES)]

