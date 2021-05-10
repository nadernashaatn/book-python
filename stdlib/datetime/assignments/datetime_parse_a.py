"""
* Assignment: Datetime Parse ISO
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Given `DATA` is in ISO format
    2. Define `a: datetime` with converted `DATA` to `datetime` object
    3. Define `b: str` with converted `a` to to ISO format
    4. Run doctests - all must succeed

Polish:
    1. Dana `DATA` jest w formacie ISO
    2. Zdefiniuj `a: datetime` z przekonwertowaną `DATA` do obiektu `datetime`
    3. Zdefiniuj `b: str` z przekonwertowaną `a` do formatu ISO
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(a) is datetime, \
    'Variable `a` has invalid type, must be a datetime'

    >>> assert type(b) is str, \
    'Variable `b` has invalid type, must be a str'

    >>> a
    datetime.datetime(1969, 7, 21, 2, 56, 15, 123000)

    >>> b
    '1969-07-21T02:56:15.123000'
"""

from datetime import datetime


DATA = '1969-07-21T02:56:15.123'

a = ...  # datetime: representing DATA
b = ...  # str: `a` formatted as '1969-07-21T02:56:15.123000'

# Solution
a = datetime.fromisoformat(DATA)
b = a.isoformat()
