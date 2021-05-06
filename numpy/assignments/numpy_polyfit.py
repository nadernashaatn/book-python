"""
* Assignment: Numpy Polyfit
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Given are points coordinates in Cartesian system
    3. Separate first row (header) from data
    4. Calculate coefficients of best approximating polynomial of 3rd degree
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dane są koordynaty punktów w układzie kartezjańskim
    3. Odseparuj pierwszy wiersz (nagłówek) do danych
    4. Oblicz współczynniki najlepiej dopasowanego wielomianu 3 stopnia
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is np.ndarray
    True
    >>> result
    array([ 0.25,  0.75, -1.5 , -2.  ])
"""


# Given
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
