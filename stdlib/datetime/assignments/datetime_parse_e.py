"""
* Assignment: Datetime Parse Formats
* Complexity: medium
* Lines of code: 8 lines
* Time: 8 min

English:
    1. List `DATA` has dates in multiple formats
    2. Define `result: list` with converted `DATA` elements
       to `datetime` objects
    3. Run doctests - all must succeed

Polish:
    1. Lista `DATA` ma dane w różnych formatach
    2. Zdefiniuj `result: list` z przekonwertowanymi elementami `DATA`
       do obiektów `datetime`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `try ... except`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, must be a list'

    >>> assert all(type(element) is datetime for element in result), \
    'All elements in `result` must be a datetime'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [datetime.datetime(1961, 4, 12, 6, 7),
     datetime.datetime(1961, 4, 12, 6, 7)]
"""

from datetime import datetime


DATA = ['1961-04-12 06:07',
        '1961-04-12 06:07:00']

result = ...  # list[datetime]: DATA elements in datetime format

# Solution
result = []

for line in DATA:
    try:
        date = datetime.strptime(line, '%Y-%m-%d %H:%M:%S')
        result.append(date)
    except ValueError:
        date = datetime.strptime(line, '%Y-%m-%d %H:%M')
        result.append(date)
