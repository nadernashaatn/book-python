"""
* Assignment: Protocol Reflection Delattr
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create class `Point` with `x`, `y`, `z` attributes
    3. Prevent deleting attributes
    4. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `Point` z atrybutami `x`, `y`, `z`
    3. Zablokuj usuwanie atrybutów
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pt = Point(1, 2, 3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)

    >>> del pt.x
    Traceback (most recent call last):
    PermissionError: Cannot delete attributes

    >>> del pt.notexisting
    Traceback (most recent call last):
    PermissionError: Cannot delete attributes
"""


# Given
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# Solution
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __delattr__(self, item):
        raise PermissionError('Cannot delete attributes')
