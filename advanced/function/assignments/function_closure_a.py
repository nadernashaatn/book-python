"""
* Assignment: Function Closure Define
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define function `check` which takes `func: Callable` as an argument
    2. Define closure function `wrapper` inside `check`
    3. Function `wrapper` takes `*args` and `**kwargs` as arguments
    4. Function `wrapper` returns `None`
    5. Function `check` must return `wrapper: Callable`
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `check`, która przyjmuje `func: Callable` jako argument
    2. Zdefiniuj funkcję closure `wrapper` wewnątrz `check`
    3. Funkcja `wrapper` przyjmuje `*args` i `**kwargs` jako argumenty
    4. Funkcja `wrapper` zwraca `None`
    5. Funkcja `check` ma zwracać `wrapper: Callable`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert callable(check)
    >>> assert callable(check(lambda x: x))
    >>> result = check(lambda x: x).__call__()
    >>> result is None
    True
"""


# Solution
def check(func):
    def wrapper(*args, **kwargs):
        return None
    return wrapper

