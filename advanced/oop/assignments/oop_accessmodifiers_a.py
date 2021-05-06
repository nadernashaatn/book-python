"""
* Assignment: OOP Access Protected
* Complexity: easy
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: list[dict]`
    3. Define class `Iris` with attributes
    4. Protected attributes: `sepal_length`, `sepal_width`, `petal_length`, `petal_width`
    5. Public attribute: `species`
    6. Iterate over `DATA` and add all public attributes to `result`
    7. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: list[dict]`
    3. Zdefiniuj klasę `Iris`
    4. Chronione atrybuty: `sepal_length`, `sepal_width`, `petal_length`, `petal_width`
    5. Publiczne atrybuty: `species`
    6. Iteruj po `DATA` i dodaj wszystkie publiczne atrybuty do `result`
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> DATA = [Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
    ...         Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
    ...         Iris(5.7, 2.8, 4.1, 1.3, 'versicolor')]

    >>> result = [{attribute: value}
    ...           for row in DATA
    ...           for attribute, value in row.__dict__.items()
    ...           if not attribute.startswith('_')]

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'species': 'virginica'},
     {'species': 'setosa'},
     {'species': 'versicolor'}]
"""


# Given
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
