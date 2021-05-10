"""
* Assignment: Datetime Parse US
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Given `DATA` is in long US date and time format
    2. Define `a: datetime` with converted `DATA` to `datetime` object
    3. Define `b: str` with converted `a` to `1961-04-12 06:07` format
    4. Run doctests - all must succeed

Polish:
    1. Dana `DATA` jest w długim formacie amerykańskim
    2. Zdefiniuj `a: datetime` z przekonwertowaną `DATA` do obiektu `datetime`
    3. Zdefiniuj `b: str` z przekonwertowaną `a` do formatu `1961-04-12 06:07`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(a) is datetime, \
    'Variable `a` has invalid type, must be a datetime'

    >>> assert type(b) is str, \
    'Variable `b` has invalid type, must be a str'

    >>> a
    datetime.datetime(1961, 4, 12, 6, 7)

    >>> b
    '1961-04-12 06:07'
"""

from datetime import datetime


DATA = 'April 12, 1961 6:07'

a = ...  # datetime: representing DATA
b = ...  # str: `a` formatted as '1961-04-12 06:07'


# Solution
a = datetime.strptime(DATA, '%B %d, %Y %H:%M')
b = a.strftime('%Y-%m-%d %H:%M')

