"""
* Assignment: OOP Overload Equals
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Override operator for code to work correctly
    2. Do not use `dataclasses`
    3. Run doctests - all must succeed

Polish:
    1. Nadpisz operator aby poniższy kod zadziałał poprawnie
    2. Nie używaj `dataclasses`
    3. Uruchom doctesty - wszystkie muszą się powieść

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
