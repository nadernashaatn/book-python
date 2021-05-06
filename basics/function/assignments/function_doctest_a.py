"""
* Assignment: Function Doctest Temperature
* Required: no
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Write implementation of a function `celsius_to_kelvin`
    3. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Napisz implementację funkcji `celsius_to_kelvin`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(celsius_to_kelvin)
    True
    >>> celsius_to_kelvin(0)
    273.15
    >>> celsius_to_kelvin(1)
    274.15
    >>> celsius_to_kelvin(-1)
    272.15
    >>> celsius_to_kelvin('a')
    Traceback (most recent call last):
    TypeError: Invalid argument
    >>> celsius_to_kelvin([0, 1])
    [273.15, 274.15]
    >>> celsius_to_kelvin((0, 1))
    (273.15, 274.15)
    >>> celsius_to_kelvin({0, 1})
    {273.15, 274.15}
"""


# Solution
def celsius_to_kelvin(degrees):
    if type(degrees) in (int, float):
        return 273.15 + degrees

    if type(degrees) is tuple:
        return tuple(x + 273.15 for x in degrees)

    if type(degrees) is list:
        return list(x + 273.15 for x in degrees)

    if type(degrees) is set:
        return set(x + 273.15 for x in degrees)

    raise TypeError('Invalid argument')


## Solution 2
# if type(degrees) in (int, float):
#     return 273.15 + degrees
#
# if type(degrees) in (list, tuple, set):
#     cls = type(degrees)
#     return cls(x+273.15 for x in degrees)
#
# raise TypeError('Invalid argument')
