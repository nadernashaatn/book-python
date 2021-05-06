"""
* Assignment: Numpy Round Floor and Ceil
* Complexity: medium
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Ceil round `data` values and assign to `result_ceil`
    3. Floor round `data` values and assign to `result_floor`
    4. Round `data` values and assign to `result_round`
    5. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zaokrąglij wartości `data` w górę (ceil) i przypisz do `result_ceil`
    3. Zaokrąglij wartości `data` w dół (floor) i przypisz do `result_floor`
    4. Zaokrąglij wartości `data` i przypisz do `result_round`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result_ceil) is np.ndarray
    True
    >>> type(result_floor) is np.ndarray
    True
    >>> type(result_round) is np.ndarray
    True
    >>> result_ceil
    array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
           1., 1., 1., 1.])

    >>> result_floor
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0.])

    >>> result_round
    array([1., 1., 1., 1., 0., 1., 0., 1., 1., 0., 1., 1., 1., 1., 0., 0., 0.,
           1., 1., 1., 1.])
"""


# Given
import numpy as np
np.random.seed(0)


DATA = np.array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
                 0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152,
                 0.79172504, 0.52889492, 0.56804456, 0.92559664, 0.07103606,
                 0.0871293 , 0.0202184 , 0.83261985, 0.77815675, 0.87001215,
                 0.97861834])

result_ceil = ...
result_floor = ...
result_round = ...


# Solution
result_ceil = np.ceil(DATA)
result_floor = np.floor(DATA)
result_round = np.round(DATA)
