"""
* Assignment: Datetime Parse Local
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    3. Create `datetime` object by parsing `DATA`
    4. Using date formatting converts `DATA` to string and assign to `result`
       in american short date format (np. '07/21/69 2:56 AM')
    5. Make sure, that hour is without leading zero
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    3. Stwórz obiekt `datetime` parsując `DATA`
    4. Używając parametrów formatowania daty przekonwertuj `DATA` do stringa
       i zapisz do `result` w formacie amerykańskim krótkim (np. '07/21/69 2:56 AM')
    5. Upewnij się, że godzina jest bez wiodącego zera
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Add string `local time` to format statement

Hints:
    * Add quote sign `"` like normal text to `fmt` parameter of `.strptime()`
    * `%dst`
    * Use `%-I` or `%_I` on \*nix systems (macOS, BSD, Linux) to remove leading zero
    * Use `%#I` on Windows to remove leading zero

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is datetime, \
    'Variable `result` has invalid type, must be a datetime'

    >>> result
    datetime.datetime(1969, 7, 21, 2, 56, 15)
"""


# Given
from datetime import datetime


DATA = 'July 21st, 1969 2:56:15 AM local time'

result = ...  # datetime: representation of DATA


# Solution
result = datetime.strptime(DATA, '%B %dst, %Y %I:%M:%S %p local time')
