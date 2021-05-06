"""
* Assignment: DataFrame Sample
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    3. Ustaw wszystkie wiersze w losowej kolejności
    4. Zresetuj index nie pozostawiając kopii zapasowej starego
    5. Zdefiniuj `result` z ostatnimi 10% wierszy
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
                        Name        Country Gender                                            Flights  Total Flights Total Flight Time (ddd:hh:mm)
    0        Viktor Patsayev   Soviet Union    Man                                    Soyuz 11 (1971)              1                     023:21:21
    1       Stephen G. Bowen  United States    Man     STS-126 (2008), STS-132 (2010), STS-133 (2011)              3                     040:10:04
    2           Sergei Revin         Russia    Man                               Soyuz TMA-04M (2012)              1                     124:23:51
    3         Maksim Surayev         Russia    Man          Soyuz TMA-16 (2009), Soyuz TMA-13M (2014)              2                     334:12:09
    4          Andrew Thomas  United States    Man  STS-77 (1996), STS-89 (1998), STS-102 (2001), ...              4                     177:09:14
    ..                   ...            ...    ...                                                ...            ...                           ...
    562  Lawrence J. DeLucas  United States    Man                                      STS-50 (1992)              1                     013:19:30
    563   Aleksandr Laveykin   Soviet Union    Man                                  Soyuz TM-2 (1987)              1                     174:03:25
    564        Owen Garriott  United States    Man                      Skylab 3 (1973), STS-9 (1983)              2                     069:17:56
    565          Ivan Vagner         Russia    Man                                 Soyuz MS-16 (2020)              1                     145:04:14
    566     Yuri Malenchenko         Russia    Man  Soyuz TM-19 (1994), STS-106 (2000), Soyuz TMA-...              6                     826:09:22
    <BLANKLINE>
    [567 rows x 6 columns]
"""


# Given
import pandas as pd
import numpy as np
np.random.seed(0)


DATA = r'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/astro-database.csv'

result = ...


# Solution
df = pd.read_csv(DATA)
df = df.sample(frac=1.0)
df.reset_index(drop=True, inplace=True)

result = df
