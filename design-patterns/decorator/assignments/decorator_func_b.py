"""
* Assignment: Decorator Function Disable
* Complexity: easy
* Lines of code: 1 lines
* Time: 5 min

English:
    1. Modify decorator `disable`
    2. Decorator raises an exception `PermissionError` and does not execute function
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj dekorator `disable`
    2. Dekorator podnosi wyjątek `PermissionError` i nie wywołuje funkcji
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(disable)
    >>> assert isfunction(disable(lambda: None))

    >>> @disable
    ... def echo(text):
    ...     print(text)

    >>> echo('hello')
    Traceback (most recent call last):
    PermissionError: Function is disabled
"""

def disable(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# Solution
def disable(func):
    def wrapper(*args, **kwargs):
        raise PermissionError('Function is disabled')
    return wrapper

