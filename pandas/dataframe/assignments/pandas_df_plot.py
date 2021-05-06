"""
* Assignment: DataFrame Plot
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from `DATA` as `df: pd.DataFrame`
    3. Select `Luminance` stylesheet
    4. Parse column with dates
    5. Select desired date and location, then resample by hour
    6. Display chart (line) with activity hours in "Sleeping Quarters upper" location
    7. Active is when `Luminance` is not zero
    8. Easy: for day 2019-09-28
    9. Advanced: for each day, as subplots
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    3. Wybierz arkusz `Luminance`
    4. Sparsuj kolumny z datami
    5. Wybierz pożądaną datę i lokację, następnie próbkuj co godzinę
    6. Aktywność jest gdy `Luminance` jest różna od zera
    7. Wyświetl wykres (line) z godzinami aktywności w dla lokacji "Sleeping Quarters upper"
    8. Łatwe: dla dnia 2019-09-28
    9. Zaawansowane: dla wszystkich dni, jako subplot
    X. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pd.Series.apply(np.sign)` :ref:`Numpy signum`
    * `pd.Series.resample('H').sum()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    datetime
    2019-09-28 00:00:00+00:00    1
    2019-09-28 01:00:00+00:00    1
    2019-09-28 02:00:00+00:00    1
    2019-09-28 03:00:00+00:00    1
    2019-09-28 04:00:00+00:00    0
                                ..
    2019-09-28 19:00:00+00:00    1
    2019-09-28 20:00:00+00:00    1
    2019-09-28 21:00:00+00:00    1
    2019-09-28 22:00:00+00:00    1
    2019-09-28 23:00:00+00:00    1
    Freq: H, Name: value, Length: 24, dtype: int64
"""


# Given
import numpy as np
import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/xlsx/sensors-optima.xlsx'
WHERE = 'Sleeping Quarters upper'
WHEN = '2019-09-28'

result = ...


# Solution
df = pd.read_excel(
    io=DATA,
    parse_dates=['datetime'],
    sheet_name='Luminance',
    header=1,
    index_col=0)

result = (df
    .loc[df['location'] == WHERE]
    .loc[WHEN, 'value']
    .apply(np.sign)
    .resample('H')
    .sum())

ax = result.plot(color='red', figsize=(16,5))
_ = ax.set_yticks([0, 1])
_ = ax.set_yticklabels(['sleep', 'awake'])
