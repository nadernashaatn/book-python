"""
* Assignment: Unpacking Arguments Range
* Complexity: medium
* Lines of code: 25 lines
* Time: 21 min

English:
    1. Define function `myrange` with parameters: `start`, `stop`, `step`
    2. Write own implementation of a built-in `myrange(start, stop, step)` function
    3. How to implement passing only stop argument (`myrange(start=0, stop=???, step=1)`)?
    4. All tests must pass
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `myrange` z parametrami: `start`, `stop`, `step`
    2. Zaimplementuj własne rozwiązanie wbudowanej funkcji `myrange(start, stop, step)`
    3. Jak zaimplementować możliwość podawania tylko końca (`myrange(start=0, stop=???, step=1)`)?
    4. Wszystkie testy muszą przejść
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * use `*args` and `**kwargs`
    * `if len(args) == ...`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(myrange)

    >>> myrange(0, 10, 2)
    [0, 2, 4, 6, 8]

    >>> myrange(0, 5)
    [0, 1, 2, 3, 4]

    >>> myrange(5)
    [0, 1, 2, 3, 4]

    >>> myrange()
    Traceback (most recent call last):
    TypeError: myrange expected at least 1 argument, got 0

    >>> myrange(1,2,3,4)
    Traceback (most recent call last):
    TypeError: myrange expected at most 3 arguments, got 4

    >>> myrange(stop=2)
    Traceback (most recent call last):
    TypeError: myrange() takes no keyword arguments

    >>> myrange(start=1, stop=2)
    Traceback (most recent call last):
    TypeError: myrange() takes no keyword arguments

    >>> myrange(start=1, stop=2, step=2)
    Traceback (most recent call last):
    TypeError: myrange() takes no keyword arguments
"""


# Solution
def myrange(*args, **kwargs):
    if kwargs:
        raise TypeError('myrange() takes no keyword arguments')
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 0:
        raise TypeError('myrange expected at least 1 argument, got 0')
    else:
        raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')

    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result
