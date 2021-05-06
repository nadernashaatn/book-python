"""
* Assignment: OOP Abstract Interface
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Define abstract class `IrisAbstract`
    3. Abstract methods: `__init__`, `sum()`, `len()`, `mean()`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę abstrakcyjną `IrisAbstract`
    3. Metody abstrakcyjne: `__init__`, `sum()`, `len()`, `mean()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isabstract

    >>> assert isabstract(IrisAbstract)
    >>> assert hasattr(IrisAbstract, 'mean')
    >>> assert hasattr(IrisAbstract, 'sum')
    >>> assert hasattr(IrisAbstract, 'len')
    >>> assert IrisAbstract.mean.__isabstractmethod__
    >>> assert IrisAbstract.sum.__isabstractmethod__
    >>> assert IrisAbstract.len.__isabstractmethod__
"""


# Given
from abc import ABCMeta, abstractmethod


# Solution
class IrisAbstract(metaclass=ABCMeta):
    @abstractmethod
    def mean(self) -> float:
        ...

    @abstractmethod
    def sum(self) -> float:
        ...

    @abstractmethod
    def len(self) -> int:
        ...
