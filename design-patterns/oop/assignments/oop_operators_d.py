"""
* Assignment: OOP Operators Contains
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Use code from "Given" section (see below)
    2. Override operators for code to work correctly
    3. Do not use `dataclasses`
    4. Run doctests - all must succeed

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Nadpisz operatory aby poniższy kod zadziałał poprawnie
    3. Nie używaj `dataclasses`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> astro = Astronaut('Jan Twardowski', missions=[
    ...     Mission(1969, 'Apollo 11'),
    ...     Mission(2024, 'Artemis 3'),
    ...     Mission(2035, 'Ares 3'),
    ... ])

    >>> Mission(2035, 'Ares 3') == Mission(2035, 'Ares 3')
    True
    >>> Mission(2035, 'Ares 3') == Mission(1973, 'Apollo 18')
    False
    >>> Mission(2035, 'Ares 3') == Mission(2035, 'Apollo 18')
    False
    >>> Mission(2035, 'Ares 3') == Mission(1973, 'Ares 3')
    False

    >>> Mission(2024, 'Artemis 3') in astro
    True
    >>> Mission(1973, 'Apollo 18') in astro
    False
"""


# Given
class Astronaut:
    def __init__(self, name, missions):
        self.name = name
        self.missions = missions


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


# Solution
class Astronaut:
    def __init__(self, name, missions):
        self.name = name
        self.missions = missions

    def __contains__(self, flight):
        return flight in self.missions


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __eq__(self, other):
        return (self.year == other.year) \
           and (self.name == other.name)
