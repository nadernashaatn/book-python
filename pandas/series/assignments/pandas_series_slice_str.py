"""
* Assignment: Slicing Slice Str
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Create `pd.Series` with 26 random integers in range `[10, 100)`
    3. Name indexes like letters from ASCII alphabet (`ascii_lowercase: str`)
    4. Find middle letter of alphabet
    5. Slice from series 3 elements up and down from middle
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `pd.Series` z 26 losowymi liczbami całkowitymi z przedziału `<10; 100)`
    3. Nazwij indeksy jak kolejne litery alfabetu ASCII (`ascii_lowercase: str`)
    4. Znajdź środkową literę alfabetu
    5. Wytnij z serii po 3 elementy w górę i w dół od wyszukanego środka
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.random.randint(..., ..., size=...)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> result
    j    97
    k    80
    l    98
    m    98
    n    22
    o    68
    p    75
    dtype: int64
"""


# Given
from statistics import median_low
import pandas as pd
import numpy as np
np.random.seed(0)


ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

# Solution
data = np.random.randint(10, 100, size=26)
alphabet = list(ascii_lowercase)
letter_position = median_low(alphabet)
position = alphabet.index(letter_position)

s = pd.Series(data, alphabet)
result = s[position-3:position+4]
