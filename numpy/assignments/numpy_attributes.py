"""
* Assignment: Numpy Attributes
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: dict` with:
        a. number of dimensions;
        b. number of elements;
        c. data type;
        d. element size;
        e. shape;
        f. strides.
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: dict` z:
        a. liczbę wymiarów,
        b. liczbę elementów,
        c. typ danych,
        d. rozmiar elementu,
        e. kształt,
        f. przeskoki (strides).
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is dict
    True

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'number of dimensions': 2,
     'number of elements': 6,
     'data type': dtype('float64'),
     'element size': 8,
     'shape': (2, 3),
     'strides': (24, 8)}
"""


# Given
import numpy as np

DATA = np.array([[-1.1, 0.0, 1.1],
                 [2.2, 3.3, 4.4]])

result = {
    'number of dimensions': ...,
    'number of elements': ...,
    'data type': ...,
    'element size': ...,
    'shape': ...,
    'strides': ...,
}


# Solution
result = {
    'number of dimensions': DATA.ndim,
    'number of elements': DATA.size,
    'data type': DATA.dtype,
    'element size': DATA.itemsize,
    'shape': DATA.shape,
    'strides': DATA.strides,
}
