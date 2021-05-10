"""
* Assignment: Datetime Parse ZeroPadded
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Create `datetime` object by parsing `DATA`
    2. Using date formatting converts `DATA` to string and assign to `result`
       in american short date format (np. '07/21/69 2:56 AM')
    3. Make sure, that hour is without leading zero
    4. Run doctests - all must succeed

Polish:
    1. Stwórz obiekt `datetime` parsując `DATA`
    2. Używając parametrów formatowania daty przekonwertuj `DATA` do stringa
       i zapisz do `result` w formacie amerykańskim krótkim (np. '07/21/69 2:56 AM')
    3. Upewnij się, że godzina jest bez wiodącego zera
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Add string `local time` to format statement

Hints:
    * Add quote sign `"` like normal text to `fmt` parameter of `.strptime()`
    * `%dst`
    * Use `%-I` or `%_I` on \*nix systems (macOS, BSD, Linux) to remove leading zero
    * Use `%#I` on Windows to remove leading zero

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, must be a str'

    >>> result
    '07/21/69 2:56 AM'
"""

from datetime import datetime


DATA = datetime(1969, 7, 21, 2, 56, 15)

result = ...  # str: DATA formatted in short US format: '07/21/69 2:56 AM'


# Solution
result = DATA.strftime('%m/%d/%y %#I:%M %p')  # Windows
result = DATA.strftime('%m/%d/%y %-I:%M %p')  # *nix
