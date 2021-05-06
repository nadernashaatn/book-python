"""
* Assignment: Decorator Functools Args
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use code from "Given" section (see below)
    2. Use `functools.wraps` in correct place
    3. Run doctests - all must succeed

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Użyj `functools.wraps` w odpowiednim miejscu
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> @mydecorator(happy=False)
    ... def hello():
    ...     '''Hello Docstring'''

    >>> hello.__name__
    'hello'
    >>> hello.__doc__
    'Hello Docstring'
"""


# Given
from functools import wraps


def mydecorator(happy=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Solution
def mydecorator(happy=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
