"""
* Assignment: Datetime Timezone Define
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Create `timezone` object of:
        a. UTC
        b. London, United Kingdom
        c. Moscow, Russian Federation
        d. Warsaw, Poland
        e. Tokyo, Japan
        f. Sydney, Australia
        g. Auckland, New Zealand
        h. New York, USA
    2. Use `List of tz database time zones` [1]
    3. Run doctests - all must succeed

Polish:
    1. Stwórz obiekt `timezone` z:
        a. UCT
        b. London, Wielka Brytania
        c. Moscow, Rosja
        d. Warsaw, Polska
        e. Tokyo, Japan
        f. Sydney, Australia
        g. Auckland, Nowa Zelandia
        h. New York, USA
    2. Użyj `List of tz database time zones` [1]
    3. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Wikipedia. List of tz database time zones.
        URL: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        Retrieved: 2021-03-24
    [2] IANA. Time Zone Database.
        URL: https://data.iana.org/time-zones/releases/
        Retrieved: 2021-03-24

Extra Task:
    1. Cape Canaveral, FL, USA
    2. Houston, TX, USA
    3. Bajkonur Cosmodrome, Kazachstan
    5. North Pole
    6. South Pole (Henryk Arctowski Polish Antarctic Station)

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pytz.tzinfo import DstTzInfo, BaseTzInfo

    >>> assert isinstance(utc, BaseTzInfo), \
    'Variable `utc` has invalid type, must be a BaseTzInfo'

    >>> assert isinstance(london, DstTzInfo), \
    'Variable `london` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(moscow, DstTzInfo), \
    'Variable `moscow` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(warsaw, DstTzInfo), \
    'Variable `warsaw` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(tokyo, DstTzInfo), \
    'Variable `tokyo` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(sydney, DstTzInfo), \
    'Variable `sydney` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(auckland, DstTzInfo), \
    'Variable `auckland` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(new_york, DstTzInfo), \
    'Variable `new_york` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(cape_canaveral, DstTzInfo), \
    'Variable `cape_canaveral` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(houston, DstTzInfo), \
    'Variable `houston` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(bajkonur, DstTzInfo), \
    'Variable `bajkonur` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(north_pole, DstTzInfo), \
    'Variable `north_pole` has invalid type, must be a DstTzInfo'

    >>> assert isinstance(south_pole, DstTzInfo), \
    'Variable `south_pole` has invalid type, must be a DstTzInfo'

    >>> utc._utcoffset
    datetime.timedelta(0)
    >>> london._utcoffset
    datetime.timedelta(days=-1, seconds=86340)
    >>> moscow._utcoffset
    datetime.timedelta(seconds=9000)
    >>> warsaw._utcoffset
    datetime.timedelta(seconds=5040)
    >>> tokyo._utcoffset
    datetime.timedelta(seconds=33540)
    >>> sydney._utcoffset
    datetime.timedelta(seconds=36300)
    >>> auckland._utcoffset
    datetime.timedelta(seconds=41940)
    >>> new_york._utcoffset
    datetime.timedelta(days=-1, seconds=68640)
    >>> cape_canaveral._utcoffset
    datetime.timedelta(days=-1, seconds=68640)
    >>> houston._utcoffset
    datetime.timedelta(days=-1, seconds=65340)
    >>> bajkonur._utcoffset
    datetime.timedelta(seconds=18480)
    >>> north_pole._utcoffset
    datetime.timedelta(seconds=2580)
    >>> south_pole._utcoffset
    datetime.timedelta(seconds=5040)
"""

from pytz import timezone


utc: timezone = ...  # timezone in UTC
london: timezone = ...  # timezone in London, United Kingdom
moscow: timezone = ...  # timezone in Moscow, Russian Federation
warsaw: timezone = ...  # timezone in Warsaw, Poland
tokyo: timezone = ...  # timezone in Tokyo, Japan
sydney: timezone = ...  # timezone in Sydney, Australia
auckland: timezone = ...  # timezone in Auckland, New Zealand
new_york: timezone = ...  # timezone in New York, USA

cape_canaveral: timezone = ...  # timezone in Cape Canaveral, FL, USA
houston: timezone = ...  # timezone in Houston, TX, USA
bajkonur: timezone = ...  # timezone in Bajkonur Cosmodrome, Kazachstan
north_pole: timezone = ...  # timezone in North Pole
south_pole: timezone = ...  # timezone in South Pole


# Solution
utc = timezone('UTC')
london = timezone('Europe/London')
moscow = timezone('Europe/Moscow')
warsaw = timezone('Europe/Warsaw')
tokyo = timezone('Asia/Tokyo')
sydney = timezone('Australia/Sydney')
auckland = timezone('Pacific/Auckland')
new_york = timezone('America/New_York')

cape_canaveral = timezone('America/New_York')
houston = timezone('America/Chicago')
bajkonur = timezone('Asia/Almaty')
north_pole = timezone('Arctic/Longyearbyen')
south_pole = timezone('Europe/Warsaw')

