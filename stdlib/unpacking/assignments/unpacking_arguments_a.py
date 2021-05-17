"""
* Assignment: Unpacking Arguments Define
* Complexity: medium
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Create function `mean(*args)`, which calculates arithmetic mean for `args`
    2. Do not import any libraries and modules
    3. Define `result: list[tuple[str, float]]`
    4. Iterate over `DATA` separating `features` from `label`
    5. To `result` append `label` and arithmetic mean of `features`
    6. Run doctests - all must succeed

Polish:
    1. Stwórz funkcję `mean(*args)`, która liczy średnią arytmetyczną dla `args`
    2. Nie importuj żadnych bibliotek i modułów
    3. Zdefiniuj `result: list[tuple[str, float]]`
    4. Iteruj po `DATA` separując `features` od `label`
    5. Do `result` dodawaj `label` oraz wynik średniej arytmetycznej `features`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mean(1)
    1.0
    >>> mean(1, 3)
    2.0
    >>> mean(1, 2, 3)
    2.0

    >>> assert type(result) is list
    >>> assert all(type(row) is tuple for row in result)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('virginica', 3.875),
     ('setosa', 2.65),
     ('versicolor', 3.475),
     ('virginica', 6.0),
     ('versicolor', 3.95),
     ('setosa', 4.7)]

"""

DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 5.7, 'virginica'),
        (6.4, 1.5, 'versicolor'),
        (4.7,  'setosa')]


def mean(*args):
    return sum(args) / len(args)


# Solution
result = [(label, mean(*features))
          for *features, label in DATA[1:]]
