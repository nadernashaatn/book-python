"""
* Assignment: OOP Composition Syntax
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Compose class `MarsMission` from `Habitat`, `Rocket`, `Astronaut`
    3. Assignment demonstrates syntax, so do not add any attributes and methods
    4. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Skomponuj klasę `MarsMission` z `Habitat`, `Rocket`, `Astronaut`
    3. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    4. Uruchom doctesty - wszystkie muszą się powieść

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


# Given
class Habitat:
    pass


class Astronaut:
    pass


class Rocket:
    pass


# Solution
class MarsMission(Habitat, Astronaut, Rocket):
    pass
