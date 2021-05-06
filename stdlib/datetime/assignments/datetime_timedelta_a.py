"""
* Assignment: Datetime Timedelta Duration
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Calculate how many years passed between Gagarin's launch
       and Armstrong's first step on the Moon
    3. Assume:
        a. year = 365.2425 days
        b. month = 30.436875 days
    4. Result round to one decimal place
    5. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Podany jest czas, który upłynął między startem Gagarina a pierwszym krokiem Armstronga na Księżycu
    3. Uwzględnij założenie:
        a. rok = 365.2425 dni
        b. miesiąc = 30.436875 dni
    4. Rezultat zaokrąglij jednego miejsca po przecinku
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is float, \
    'Variable `result` has invalid type, must be a float'

    >>> result
    8.3
"""


# Given
from datetime import datetime, timedelta


DAY = 1
MONTH = 30.436875 * DAY
YEAR = 365.2425 * DAY

GAGARIN = datetime(1961, 4, 12, 6, 7)
ARMSTRONG = datetime(1969, 7, 21, 2, 56, 15)

# Solution
duration = ARMSTRONG - GAGARIN
result = round(duration.days / YEAR, 1)
