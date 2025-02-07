"""
* Assignment: DataFrame Export CSV
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. Select 146 head rows, and last 11 from it
    3. Export data from column `Event` to file the `FILE`
    4. Data has to be in CSV format
    5. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `result: pd.DataFrame`
    2. Wybierz pierwszych 146 wierszy, a z nich ostatnie 11
    3. Wyeksportuj dane z kolumny `Event` do pliku `FILE`
    4. Dane mają być w formacie CSV
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = open(FILE).read()
    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    ,Event
    135,LM lunar landing.
    136,LM powered descent  engine cutoff.
    137,Decision made to  proceed with EVA prior to first rest period.
    138,Preparation for EVA  started.
    139,EVA started (hatch  open).
    140,CDR completely outside  LM on porch.
    141,Modular equipment  stowage assembly deployed (CDR).
    142,First clear TV picture  received.
    143,"CDR at foot of ladder  (starts to report, then pauses to listen)."
    144,CDR at foot of ladder  and described surface as “almost like a powder.”
    145,1st step  taken lunar surface (CDR). “That’s one small step for a man…one giant leap  for mankind.”
    <BLANKLINE>
    >>> from os import remove
    >>> remove(FILE)
"""

import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/html/apollo11.html'
FILE = r'_temporary.csv'


# Solution
result = pd.read_html(DATA, header=0)[0]
result = result.head(146).tail(11)
result['Event'].to_csv(FILE)

