"""
* Assignment: Function Arguments Range
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Define function `myrange` with parameters: `start`, `stop`, `step`
    2. Write own implementation of a built-in `myrange(start, stop, step)` function
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `myrange` z parametrami: `start`, `stop`, `step`
    2. Zaimplementuj własne rozwiązanie wbudowanej funkcji `myrange(start, stop, step)`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `while`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(myrange)

    >>> myrange(0, 10, 2)
    [0, 2, 4, 6, 8]

    >>> myrange(0, 5)
    [0, 1, 2, 3, 4]
"""


# Solution
def myrange(start, stop, step=1):
    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result
