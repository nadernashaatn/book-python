"""
* Assignment: Datetime Parse Many
* Complexity: medium
* Lines of code: 12 lines
* Time: 8 min

English:
    1. Define `result: list[datetime]` with parsed `DATA` dates
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[datetime]` ze sparsowanymi datami `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `for ... in``
    * nested `try ... except`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, must be a list'

    >>> assert all(type(element) is datetime for element in result), \
    'All elements in `result` must be a datetime'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [datetime.datetime(1957, 10, 4, 19, 28, 34),
     datetime.datetime(1961, 4, 12, 6, 7),
     datetime.datetime(1969, 7, 21, 2, 56, 15)]
"""

from datetime import datetime


DATA = [
    '1957-10-04 19:28:34',  # Sputnik launch (first satellite in space)
    '1961-04-12 06:07',  # Gagarin launch (first human in space)
    '1969-07-21T02:56:15',  # Armstrong first step on the Moon
]

result = ...  # list[datetime]: DATA elements in datetime format

# Solution
result = []

for line in DATA:
    try:
        date = datetime.strptime(line, '%Y-%m-%d %H:%M:%S')
        result.append(date)
    except ValueError:
        try:
            date = datetime.strptime(line, '%Y-%m-%d %H:%M')
            result.append(date)
        except ValueError:
            date = datetime.strptime(line, '%Y-%m-%dT%H:%M:%S')
            result.append(date)
