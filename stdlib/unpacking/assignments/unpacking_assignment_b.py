"""
* Assignment: Unpacking Assignment Nested
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Separate header and records
    2. Use asterisk `*` notation
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj nagłówek od danych
    2. Skorzystaj z konstrukcji z gwiazdką `*`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(header)
    <class 'tuple'>
    >>> type(data)
    <class 'list'>
    >>> len(header) > 0
    True
    >>> len(data) > 0
    True
    >>> assert all(type(x) is str for x in header)
    >>> assert all(type(row) is tuple for row in data)
    >>> header
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')
    >>> data  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa')]

"""

DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]

header: tuple
data: list


# Solution
header, *data = DATA
