"""
* Assignment: OOP Composition Syntax
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Compose class `MarsMission` from `Habitat`, `Rocket`, `Astronaut`
    2. Assignment demonstrates syntax, so do not add any attributes and methods
    3. Run doctests - all must succeed

Polish:
    1. Skomponuj klasę `MarsMission` z `Habitat`, `Rocket`, `Astronaut`
    2. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Habitat)
    >>> assert isclass(Astronaut)
    >>> assert isclass(Rocket)
    >>> assert isclass(MarsMission)
    >>> assert issubclass(MarsMission, Habitat)
    >>> assert issubclass(MarsMission, Astronaut)
    >>> assert issubclass(MarsMission, Rocket)
"""

class Habitat:
    pass


class Astronaut:
    pass


class Rocket:
    pass


# Solution
class MarsMission(Habitat, Astronaut, Rocket):
    pass
