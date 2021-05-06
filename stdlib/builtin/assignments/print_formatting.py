"""
Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> print(result)
    Temperature | -     20°C | ....-4....°F
    Temperature | -     15°C | ....+5....°F
    Temperature | -     10°C | ...+14....°F
    Temperature | -      5°C | ...+23....°F
    Temperature | +      0°C | ...+32....°F
    Temperature | +      5°C | ...+41....°F
    Temperature | +     10°C | ...+50....°F
    Temperature | +     15°C | ...+59....°F
    Temperature | +     20°C | ...+68....°F
    Temperature | +     25°C | ...+77....°F
    Temperature | +     30°C | ...+86....°F
    Temperature | +     35°C | ...+95....°F
    Temperature | +     40°C | ...+104...°F
    <BLANKLINE>
"""

from typing import Union

STEP = 5
MAX = 41
MIN = -20

result = ''

def celsius_to_fahrenheit(degree: Union[int, float]) -> float:
    return degree * 1.8 + 32


for celsius in range(MIN, MAX, STEP):
    fahrenheit = celsius_to_fahrenheit(celsius)
    result += f'Temperature | {celsius:=+8d}°C | {fahrenheit:.^+10.0f}°F\n'
