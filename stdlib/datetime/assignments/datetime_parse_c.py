"""
* Assignment: Datetime Parse Local
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Create `datetime` object by parsing `DATA`
    2. Using date formatting converts `DATA` to `datetime`
    3. Make sure, that hour is without leading zero
    4. Run doctests - all must succeed

Polish:
    1. Stwórz obiekt `datetime` parsując `DATA`
    2. Używając parametrów formatowania daty przekonwertuj `DATA` do `datetime`
    3. Upewnij się, że godzina jest bez wiodącego zera
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Add string `local time` to format statement

Hints:
    * Add `local time` text to format parameter
    * `%dst`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is datetime, \
    'Variable `result` has invalid type, must be a datetime'

    >>> result
    datetime.datetime(1969, 7, 21, 2, 56, 15)
"""

from datetime import datetime


DATA = 'July 21st, 1969 2:56:15 AM local time'

result = ...  # datetime: representation of DATA


# Solution
result = datetime.strptime(DATA, '%B %dst, %Y %I:%M:%S %p local time')
