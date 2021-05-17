"""
* Assignment: DataFrame Export Pickle
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. Select 146 head rows, and last 11 from it
    3. Export data from column `Event` to file the `FILE`
    4. Data has to be in JSON format
    5. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `result: pd.DataFrame`
    2. Wybierz pierwszych 146 wierszy, a z nich ostatnie 11
    3. Wyeksportuj dane z kolumny `Event` do pliku `FILE`
    4. Dane mają być w formacie JSON
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 20)

    >>> pd.read_pickle(FILE)
    135                                    LM lunar landing.
    136                   LM powered descent  engine cutoff.
    137    Decision made to  proceed with EVA prior to fi...
    138                        Preparation for EVA  started.
    139                           EVA started (hatch  open).
    140                 CDR completely outside  LM on porch.
    141    Modular equipment  stowage assembly deployed (...
    142                    First clear TV picture  received.
    143    CDR at foot of ladder  (starts to report, then...
    144    CDR at foot of ladder  and described surface a...
    145    1st step  taken lunar surface (CDR). “That’s o...
    Name: Event, dtype: object

    >>> from os import remove
    >>> remove(FILE)
"""

import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/html/apollo11.html'
FILE = r'_temporary.pkl'


# Solution
result = pd.read_html(DATA, header=0)[0]
result = result.head(146).tail(11)
result['Event'].to_pickle(FILE)

