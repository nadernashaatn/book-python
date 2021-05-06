"""
* Assignment: OOP Composition Mixin
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `MarsMission` from classes `Habitat`, `Rocket`, `Astronaut`
    3. Use mixins classes
    4. You can modify given classes
    5. Assignment demonstrates syntax, so do not add any attributes and methods
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `MarsMission` z klas `Habitat`, `Rocket`, `Astronaut`
    3. Użyj klas domieszkowych (mixin)
    4. Możesz modyfikować dane klasy
    5. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    6. Uruchom doctesty - wszystkie muszą się powieść

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


class Astronaut:
    pass


class Rocket:
    pass


class MarsMission(Habitat, Astronaut, Rocket):
    pass
