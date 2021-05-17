"""
* Assignment: OOP AccessModifiers Protected
* Complexity: easy
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Modify class `Iris` to add attributes:
        a. Protected attributes: sepal_length, sepal_width, petal_length, petal_width
        b. Public attribute: species
    2. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `Iris` by dodać atrybuty:
        a. Chronione atrybuty: sepal_length, sepal_width, petal_length, petal_width
        b. Publiczne atrybuty: species`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> isclass(Iris)
    True
    >>> iris = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')
    >>> assert hasattr(iris, '_sepal_length')
    >>> assert hasattr(iris, '_sepal_width')
    >>> assert hasattr(iris, '_petal_length')
    >>> assert hasattr(iris, '_petal_width')
    >>> assert hasattr(iris, 'species')

    >>> DATA = [Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
    ...         Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
    ...         Iris(5.7, 2.8, 4.1, 1.3, 'versicolor')]
    >>>
    >>> result = [{attribute: value}
    ...           for row in DATA
    ...           for attribute, value in row.__dict__.items()
    ...           if not attribute.startswith('_')]
    >>>
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'species': 'virginica'},
     {'species': 'setosa'},
     {'species': 'versicolor'}]
"""

class Iris:
    pass


# Solution
class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self._sepal_width = sepal_width
        self._sepal_length = sepal_length
        self._petal_width = petal_width
        self._petal_length = petal_length
        self.species = species
