"""
Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [[6, 6, 0, 4, 8, 7, 6, 4, 7, 5, 9, 3, 8, 2, 4, 2],
     [1, 9, 4, 8, 9, 2, 4, 1, 1, 5, 7, 8, 1, 5, 6, 5],
     [9, 3, 8, 7, 7, 8, 4, 0, 8, 0, 1, 6, 0, 9, 7, 5],
     [3, 5, 1, 3, 9, 3, 3, 2, 8, 7, 1, 1, 5, 8, 7, 1],
     [4, 8, 4, 1, 8, 5, 8, 3, 9, 8, 9, 4, 7, 1, 9, 6],
     [5, 9, 3, 4, 2, 3, 2, 0, 9, 4, 7, 1, 1, 2, 2, 0],
     [1, 8, 6, 8, 4, 8, 3, 3, 9, 6, 9, 4, 7, 7, 5, 1],
     [5, 9, 1, 7, 9, 5, 3, 3, 0, 4, 1, 3, 5, 2, 5, 6],
     [0, 1, 2, 3, 0, 9, 8, 9, 1, 0, 1, 3, 9, 9, 1, 6],
     [1, 5, 1, 0, 9, 0, 3, 2, 1, 7, 3, 0, 0, 8, 6, 9],
     [1, 4, 1, 3, 1, 4, 5, 6, 2, 0, 8, 7, 0, 9, 1, 6],
     [3, 4, 5, 7, 9, 2, 3, 0, 2, 2, 5, 8, 4, 1, 9, 7],
     [2, 0, 7, 6, 9, 8, 4, 5, 6, 4, 2, 8, 0, 7, 1, 5],
     [0, 8, 4, 2, 3, 7, 5, 9, 4, 5, 9, 9, 2, 4, 6, 6],
     [1, 0, 9, 3, 5, 2, 3, 3, 7, 6, 9, 6, 0, 6, 9, 6],
     [0, 2, 7, 1, 4, 2, 7, 8, 7, 8, 9, 0, 0, 7, 5, 4]]

    >>> total
    62
"""

from random import seed, randint


X_MAX = 16
Y_MAX = 16
X_INNER = 4
Y_INNER = 4

seed(0)
result = []
total = 0

x_offset = int((X_MAX - X_INNER) / 2)
x_offset_left = x_offset
x_offset_right = X_MAX - x_offset

y_offset = int((Y_MAX - Y_INNER) / 2)
y_offset_left = y_offset
y_offset_right = Y_MAX - y_offset


for x in range(X_MAX):
    result.append([])

    for y in range(Y_MAX):
        result[x].append(randint(0, 9))

        if x_offset_left <= x < x_offset_right and y_offset_left <= y < y_offset_right:
            total += result[x][y]

