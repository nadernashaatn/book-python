"""
* Assignment: OOP Overload Equals
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use code from "Given" section (see below)
    2. Override operator for code to work correctly
    3. Do not use `dataclasses`
    4. Run doctests - all must succeed

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Nadpisz operator aby poniższy kod zadziałał poprawnie
    3. Nie używaj `dataclasses`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> Mission(2035, 'Ares 3') == Mission(2035, 'Ares 3')
    True
    >>> Mission(2035, 'Ares 3') == Mission(1973, 'Apollo 18')
    False
    >>> Mission(2035, 'Ares 3') == Mission(2035, 'Apollo 18')
    False
    >>> Mission(2035, 'Ares 3') == Mission(1973, 'Ares 3')
    False
"""


# Given
class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


# Solution
class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __eq__(self, other):
        return (self.year == other.year) \
           and (self.name == other.name)
