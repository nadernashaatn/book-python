"""
* Assignment: Protocol Iterator Range
* Complexity: medium
* Lines of code: 14 lines
* Time: 13 min

English:
    1. Define class `Range` with parameters: `start`, `stop`, `step`
    2. Write own implementation of a built-in `range(start, stop, step)` function
    3. Assume, that user will never give only one argument; always it will be either two or three arguments
    4. Use Iterator protocol
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Range` z parametrami: `start`, `stop`, `step`
    2. Zaimplementuj własne rozwiązanie wbudowanej funkcji `range(start, stop, step)`
    3. Przyjmij, że użytkownik nigdy nie poda tylko jednego argumentu; zawsze będą to dwa lub trzy argumenty
    4. Użyj protokołu Iterator
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Range)

    >>> r = Range(0, 0, 0)
    >>> assert hasattr(r, '__iter__')
    >>> assert hasattr(r, '__next__')
    >>> assert ismethod(r.__iter__)
    >>> assert ismethod(r.__next__)

    >>> list(Range(0, 10, 2))
    [0, 2, 4, 6, 8]

    >>> list(Range(0, 5))
    [0, 1, 2, 3, 4]
"""
from dataclasses import dataclass


@dataclass
class Range:
    start: int = 0
    stop: int = None
    step: int = 1


# Solution
@dataclass
class Range:
    start: int = 0
    stop: int = None
    step: int = 1

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result
