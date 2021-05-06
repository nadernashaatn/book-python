"""
* Assignment: Idioms Range Impl
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Define function `myrange` with parameters: `start`, `stop`, `step`
    2. Write own implementation of a built-in `myrange(start, stop, step)` function
    3. How to implement passing only stop argument (`myrange(start=0, stop=???, step=1)`)?
    4. Assume, that user will:
        a. never give only one argument; always it will be either two or three arguments
        b. never give keyword arguments; always it will be positional arguments
        c. never give more than three arguments
    5. All tests must pass
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `myrange` z parametrami: `start`, `stop`, `step`
    2. Zaimplementuj własne rozwiązanie wbudowanej funkcji `myrange(start, stop, step)`
    3. Jak zaimplementować możliwość podawania tylko końca (`myrange(start=0, stop=???, step=1)`)?
    4. Przyjmij, że użytkownik:
        a. nigdy nie poda tylko jednego argumentu; zawsze będą to dwa lub trzy argumenty
        b. nigdy nie poda argumentów keywordowych; zawsze będą to argumenty pozycyjne
        c. nigdy nie poda więcej niż trzy argumenty
    5. Wszystkie testy muszą przejść
    6. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `if len(args) == ...`

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
def myrange(start=0, stop=None, step=1):
    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result
