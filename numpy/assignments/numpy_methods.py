"""
* Assignment: Numpy Methods
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Reshape `result` to 3x4
    3. Fill last column with zeros (0)
    4. Transpose `result`
    5. Convert `result` to float
    6. Fill first row with `np.nan`
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zmień kształt na 3x4
    3. Wypełnij ostatnią kolumnę zerami (0)
    4. Transponuj `result`
    5. Przekonwertuj `result` do float
    6. Wypełnij pierwszy wiersz `np.nan`
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([[nan, nan, nan],
           [47.,  9., 87.],
           [64., 83., 70.],
           [ 0.,  0.,  0.]])
"""


# Given
import numpy as np

DATA = np.array([[44, 47, 64, 67],
                 [67,  9, 83, 21],
                 [36, 87, 70, 88]])


result = ...


# Solution
DATA[:, -1].fill(0)
result = DATA.transpose()
result = result.astype(float)
result[0].fill(np.nan)
