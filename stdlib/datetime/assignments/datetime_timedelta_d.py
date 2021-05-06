"""
* Assignment: Datetime Timedelta Dict
* Complexity: easy
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Given period `DATA` is the time between Gagarin launch and Armstrong first step on the Moon
    3. Assume:
        a. year = 365.2425 days
        b. month = 30.436875 days
    4. Define `result: dict[str, int]` representing period
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Podany jest okres `DATA`, który upłynął między startem Gagarina a pierwszym krokiem Armstronga na Księżycu
    3. Uwzględnij założenie:
        a. rok = 365.2425 dni
        b. miesiąc = 30.436875 dni
    4. Zdefiniuj `result: dict[str, int]` reprezentujący okres
    X. Uruchom doctesty - wszystkie muszą się powieść

Given:
    * 8 years
    * 3 months
    * 8 days
    * 20 hours
    * 49 minutes
    * 15 seconds

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, must be a dict'

    >>> result.keys()
    dict_keys(['years', 'months', 'days', 'hours', 'minutes', 'seconds'])

    >>> assert all(type(value) is int for value in result.values()), \
    'All elements in `result` must be an int'

    >>> result
    {'years': 8, 'months': 3, 'days': 9, 'hours': 6, 'minutes': 50, 'seconds': 9}
"""


# Given
from datetime import timedelta


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30.436875 * DAY
YEAR = 365.2425 * DAY

DATA = timedelta(days=3022, seconds=24609)

result = {
    'years': ...,
    'months': ...,
    'days': ...,
    'hours': ...,
    'minutes': ...,
    'seconds': ...,
}


# Solution
years, seconds = divmod(DATA.total_seconds(), YEAR)
months, seconds = divmod(seconds, MONTH)
days, seconds = divmod(seconds, DAY)
hours, seconds = divmod(DATA.seconds, HOUR)
minutes, seconds = divmod(seconds, MINUTE)

result = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}
