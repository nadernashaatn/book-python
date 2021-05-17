"""
* Assignment: Decorator Function Type Check
* Complexity: hard
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Modify decorator `typecheck`
    2. Decorator checks types of all arguments (`*args` oraz `**kwargs`)
    3. Decorator checks return type
    4. In case when received type is not expected throw an exception `TypeError` with:
        a. argument name
        b. actual type
        c. expected type
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj dekorator `typecheck`
    2. Dekorator sprawdza typy wszystkich argumentów (`*args` oraz `**kwargs`)
    3. Dekorator sprawdza typ zwracany
    4. W przypadku gdy otrzymany typ nie jest równy oczekiwanemu wyrzuć wyjątek `TypeError` z:
        a. nazwa argumentu
        b. aktualny typ
        c. oczekiwany typ
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `echo.__annotations__`
    # {'a': <class 'str'>,
    #  'b': <class 'int'>,
    #  'c': <class 'float'>,
    #  'return': <class 'bool'>}

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> @typecheck
    ... def echo(a: str, b: int, c: float = 0.0) -> bool:
    ...     return bool(a * b)

    >>> echo('one', 1)
    True
    >>> echo('one', 1, 1.1)
    True
    >>> echo('one', b=1)
    True
    >>> echo('one', 1, c=1.1)
    True
    >>> echo('one', b=1, c=1.1)
    True
    >>> echo(a='one', b=1, c=1.1)
    True
    >>> echo(c=1.1, b=1, a='one')
    True
    >>> echo(b=1, c=1.1, a='one')
    True
    >>> echo('one', c=1.1, b=1)
    True
    >>> echo(1, 1)
    Traceback (most recent call last):
    TypeError: "a" is <class 'int'>, but <class 'str'> was expected
    >>> echo('one', 'two')
    Traceback (most recent call last):
    TypeError: "b" is <class 'str'>, but <class 'int'> was expected
    >>> echo('one', 1, 'two')
    Traceback (most recent call last):
    TypeError: "c" is <class 'str'>, but <class 'float'> was expected
    >>> echo(b='one', a='two')
    Traceback (most recent call last):
    TypeError: "b" is <class 'str'>, but <class 'int'> was expected
    >>> echo('one', c=1.1, b=1.1)
    Traceback (most recent call last):
    TypeError: "b" is <class 'float'>, but <class 'int'> was expected
"""

def typecheck(func):
    def merge(*args, **kwargs):
        """Function merges *args, and **kwargs into single dict"""
        args = dict(zip(func.__annotations__.keys(), args))
        return kwargs | args          # Python 3.9
        # return {**args, **kwargs)}  # Python 3.7, 3.8

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# Solution
def typecheck(func):
    def validate(argname, argval):
        argtype = type(argval)
        expected = func.__annotations__[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, but {expected} was expected')

    def merge(*args, **kwargs):
        args = dict(zip(func.__annotations__.keys(), args))
        return kwargs | args          # Python 3.9
        # return {**args, **kwargs)}  # Python 3.7, 3.8

    def wrapper(*args, **kwargs):
        for argname, argval in merge(*args, **kwargs).items():
            validate(argname, argval)

        result = func(*args, **kwargs)
        validate('return', result)
        return result
    return wrapper
