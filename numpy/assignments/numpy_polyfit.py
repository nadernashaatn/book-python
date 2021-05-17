"""
* Assignment: Numpy Polyfit
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Given are points coordinates in Cartesian system
    2. Separate first row (header) from data
    3. Calculate coefficients of best approximating polynomial of 3rd degree
    4. Run doctests - all must succeed

Polish:
    1. Dane są koordynaty punktów w układzie kartezjańskim
    2. Odseparuj pierwszy wiersz (nagłówek) do danych
    3. Oblicz współczynniki najlepiej dopasowanego wielomianu 3 stopnia
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([ 0.25,  0.75, -1.5 , -2.  ])
"""

import numpy as np

DATA = [('x', 'y'),
        (-4.0, 0.0),
        (-3.0, 2.5),
        (-2.0, 2.0),
        (0.0, -2.0),
        (2.0, 0.0),
        (3.0, 7.0)]


result = ...


# Solution
data = np.array(DATA[1:])
x = data[:, 0]
y = data[:, 1]

result = np.polyfit(x, y, deg=3)
