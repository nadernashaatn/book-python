"""
* Assignment: Function First Class Define
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define function `wrapper`
    2. Function `wrapper` takes arbitrary number of positional and keyword arguments
    3. Function `wrapper` prints `hello from wrapper`
    4. Define function `check` with `func: Callable` as a parameter
    5. Function `check` must return `wrapper: Callable`
    X. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `wrapper`
    2. Funkcja `wrapper` przyjmuje dowolną ilość argumentów pozycyjnych i nazwanych
    3. Funkcja `wrapper` wypisuje `hello from wrapper`
    4. Zdefiniuj funkcję `check` z `func: Callable` jako parametr
    5. Funkcja `check` ma zwracać `wrapper: Callable`
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(check)
    >>> assert isfunction(wrapper)
    >>> assert isfunction(check(lambda: None))
    >>> check(lambda: None)()
    hello from wrapper
"""


# Solution
def wrapper(*args, **kwargs):
    print('hello from wrapper')


def check(func):
    return wrapper
