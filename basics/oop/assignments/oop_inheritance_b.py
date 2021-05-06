"""
* Assignment: OOP Inheritance Multiple
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Create class `Astronaut` which inherits from all of those classes
    2. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Astronaut`, która dziedziczy po tych wszystkich klasach
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Scientist)
    >>> assert isclass(Engineer)
    >>> assert isclass(Pilot)
    >>> assert isclass(MedicalDoctor)
    >>> assert isclass(Astronaut)
    >>> assert issubclass(Astronaut, Scientist)
    >>> assert issubclass(Astronaut, Engineer)
    >>> assert issubclass(Astronaut, Pilot)
    >>> assert issubclass(Astronaut, MedicalDoctor)
"""


class Scientist:
    pass


class Engineer:
    pass


class Pilot:
    pass


class MedicalDoctor:
    pass


# Solution
class Astronaut(Scientist, Engineer, Pilot, MedicalDoctor):
    pass
