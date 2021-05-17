"""
* Assignment: Decorator Functools Func
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `functools.wraps` in correct place
    2. Run doctests - all must succeed

Polish:
    1. Użyj `functools.wraps` w odpowiednim miejscu
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> @mydecorator
    ... def hello():
    ...     '''Hello Docstring'''

    >>> hello.__name__
    'hello'
    >>> hello.__doc__
    'Hello Docstring'
"""

from functools import wraps


def mydecorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# Solution
def mydecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
