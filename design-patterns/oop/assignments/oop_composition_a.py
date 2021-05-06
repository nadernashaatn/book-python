"""
* Assignment: OOP Composition Multilevel
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `MarsMission` from classes `Habitat`, `Rocket`, `Astronaut`
    3. Use multilevel inheritance
    4. Assignment demonstrates syntax, so do not add any attributes and methods
    5. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `MarsMission` z klas `Habitat`, `Rocket`, `Astronaut`
    3. Użyj wielopoziomowego dziedziczenia
    4. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    5. Uruchom doctesty - wszystkie muszą się powieść

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


# Solution
class Habitat:
    pass


class Astronaut(Habitat):
    pass


class Rocket(Astronaut):
    pass


class MarsMission(Rocket):
    pass
