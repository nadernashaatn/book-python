"""
* Assignment: Decorator Class Abspath
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Absolute path is when `path` starts with `current_directory`
    2. Create class decorator `Abspath`
    3. If `path` is relative, then `Abspath` will convert it to absolute
    4. If `path` is absolute, then `Abspath` will not modify it
    5. Run doctests - all must succeed

Polish:
    1. Ścieżka bezwzględna jest gdy `path` zaczyna się od `current_directory`
    2. Stwórz klasę dekorator `Abspath`
    3. Jeżeli `path` jest względne, to `Abspath` zamieni ją na bezwzględną
    4. Jeżeli `path` jest bezwzględna, to `Abspath` nie będzie jej modyfikował
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `path = Path(CURRENT_DIR, filename)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> @Abspath
    ... def display(path):
    ...     return str(path)

    >>> display('iris.csv').startswith(str(CURRENT_DIR))
    True
    >>> display('iris.csv').endswith('iris.csv')
    True
    >>> display('/home/python/iris.csv')
    '/home/python/iris.csv'
"""

from pathlib import Path


CURRENT_DIR = Path().cwd()


# Solution
class Abspath:
    def __init__(self, func):
        self._func = func

    def __call__(self, file):
        file = Path(CURRENT_DIR, file)
        return self._func(file)

