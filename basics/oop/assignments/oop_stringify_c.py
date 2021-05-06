"""
* Assignment: OOP Stringify Format
* Required: yes
* Complexity: easy
* Lines of code: 8 lines
* Time: 5 min

English:
    1. Overload `__format__()` to convert length units
    2. Run doctests - all must succeed

Polish:
    1. Przeciąż `__format__()` aby konwertował jednostki długości
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 1 km = 1000 m
    * 1 m = 100 cm

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = Distance(meters=1337)
    >>> format(result, 'km')
    '1.337'
    >>> format(result, 'cm')
    '133700'
    >>> format(result, 'm')
    '1337'
"""


class Distance:
    def __init__(self, meters):
        self.meters = meters


# Solution
class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __format__(self, unit):
        if unit in ('cm', 'centimeter', 'centimeters'):
            result = self.meters * 100
        elif unit in ('m', 'meter', 'meters'):
            result = self.meters
        elif unit in ('km', 'kilometer', 'kilometers'):
            result = self.meters / 1000
        return str(result)
