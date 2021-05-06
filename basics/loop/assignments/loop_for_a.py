"""
* Assignment: Loop For Count
* Required: yes
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Count occurrences of each color
    2. Run doctests - all must succeed

Polish:
    1. Zlicz wystąpienia każdego z kolorów
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(red)
    <class 'int'>
    >>> type(green)
    <class 'int'>
    >>> type(blue)
    <class 'int'>
    >>> red
    3
    >>> green
    2
    >>> blue
    2
"""

DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

red = ...  # int: number of 'red' elements in DATA
green = ...  # int: number of 'green' elements in DATA
blue = ...  # int: number of 'blue' elements in DATA

# Solution
red = 0
green = 0
blue = 0

for color in DATA:
    if color == 'red':
        red += 1
    elif color == 'green':
        green += 1
    elif color == 'blue':
        blue += 1
