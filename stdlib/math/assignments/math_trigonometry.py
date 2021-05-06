"""
Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result
    {'sin': 0.02, 'cos': 1.0, 'tg': 0.02, 'ctg': 0.02, 'PI': 3.14}
"""

import math

# Stub
def input(__prompt):
    """Stub user input, for testing purpose only"""
    return '1'


PRECISION = 2

degrees = input('What is the angle [deg]?: ')
radians = math.radians(float(degrees))

result = {
    'sin': round(math.sin(radians), PRECISION),
    'cos': round(math.cos(radians), PRECISION),
    'tg': round(math.tan(radians), PRECISION),
    'ctg': round(math.atan(radians), PRECISION),
    'PI': round(math.pi, PRECISION),
}
