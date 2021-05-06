"""
* Assignment: OOP Stringify Repr
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Print representation of each instance with values (use `repr()`)
    2. Result of sum round to two decimal places
    3. Run doctests - all must succeed

Polish:
    1. Wypisz reprezentację każdej z instancji z wartościami (użyj `repr()`)
    2. Wynik sumowania zaokrąglij do dwóch miejsc po przecinku
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = [Iris(X,y) for *X,y in DATA]
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Iris(features=[4.7, 3.2, 1.3, 0.2], label='setosa'),
     Iris(features=[7.0, 3.2, 4.7, 1.4], label='versicolor'),
     Iris(features=[7.6, 3.0, 6.6, 2.1], label='virginica')]
"""


DATA = [
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
]


class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label


# Solution
class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label

    def __repr__(self):
        features = self.features
        label = self.label
        return f'Iris({features=}, {label=})'
