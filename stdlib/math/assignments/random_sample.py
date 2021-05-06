"""
Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> sorted(result)
    [3, 17, 25, 27, 33, 49]
"""

from random import sample, seed
seed(0)

result = sample(range(1, 49), 6)


# Alternative solution
from random import randint, seed
seed(0)

MAX_VALUE = 49
MIN_VALUE = 1
REPETITIONS = 6

result = set()

while len(result) < REPETITIONS:
    number = randint(MIN_VALUE, MAX_VALUE)
    result.add(number)
