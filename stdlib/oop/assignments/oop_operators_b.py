"""
* Assignment: OOP Operators IAdd
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Override operator `+=` for code to work correctly
    2. Run doctests - all must succeed

Polish:
    1. Nadpisz operatory `+=` aby poniższy kod zadziałał poprawnie
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `obj.__iadd__(other) -> self`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> astro = Astronaut(firstname='Jan', lastname='Twardowski', missions=[
    ...     Mission(1969, 'Apollo 11'),
    ... ])
    >>> astro += Mission(2024, 'Artemis 3')
    >>> astro += Mission(2035, 'Ares 3')

    >>> print(astro)  # doctest: +NORMALIZE_WHITESPACE
    Astronaut(firstname='Jan', lastname='Twardowski',
              missions=[Mission(year=1969, name='Apollo 11'),
                        Mission(year=2024, name='Artemis 3'),
                        Mission(year=2035, name='Ares 3')])
"""

from dataclasses import dataclass


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: list


@dataclass
class Mission:
    year: int
    name: str


# Solution
@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: list

    def __iadd__(self, other):
        self.missions.append(other)
        return self


@dataclass
class Mission:
    year: int
    name: str
