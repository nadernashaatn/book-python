"""
* Assignment: Protocol Classmethod CSV
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. To class `CSVMixin` add methods:
        a. `to_csv(self) -> str`
        b. `from_csv(self, text: str) -> Union['Astronaut', 'Cosmonaut']`
    2. `CSVMixin.to_csv()` should return attribute values separated with coma
    3. `CSVMixin.from_csv()` should return instance of a class on which it was called
    4. Use `@classmethod` decorator in proper place
    5. All tests must pass
    6. Run doctests - all must succeed

Polish:
    1. Do klasy `CSVMixin` dodaj metody:
        a. `to_csv(self) -> str`
        b. `from_csv(self, text: str) -> Union['Astronaut', 'Cosmonaut']`
    2. `CSVMixin.to_csv()` powinna zwracać wartości atrybutów klasy rozdzielone po przecinku
    3. `CSVMixin.from_csv()` powinna zwracać instancje klasy na której została wywołana
    4. Użyj dekoratora `@classmethod` w odpowiednim miejscu
    5. Wszystkie testy muszą przejść
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `CSVMixin.to_csv()` should add newline `\n` at the end of line
    * `CSVMixin.from_csv()` should remove newline `\n` at the end of line

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from dataclasses import dataclass

    >>> @dataclass
    ... class Astronaut(CSVMixin):
    ...     firstname: str
    ...     lastname: str
    ...
    >>> @dataclass
    ... class Cosmonaut(CSVMixin):
    ...     firstname: str
    ...     lastname: str

    >>> mark = Astronaut('Mark', 'Watney')
    >>> jan = Cosmonaut('Jan', 'Twardowski')
    >>> mark.to_csv()
    'Mark,Watney\\n'
    >>> jan.to_csv()
    'Jan,Twardowski\\n'

    >>> with open('_temporary.txt', mode='wt') as file:
    ...     data = mark.to_csv() + jan.to_csv()
    ...     file.writelines(data)

    >>> result = []
    >>> with open('_temporary.txt', mode='rt') as file:
    ...     lines = file.readlines()
    ...     result += [Astronaut.from_csv(lines[0])]
    ...     result += [Cosmonaut.from_csv(lines[1])]

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Astronaut(firstname='Mark', lastname='Watney'),
     Cosmonaut(firstname='Jan', lastname='Twardowski')]
    >>> from os import remove
    >>> remove('_temporary.txt')
"""

from typing import Union


class CSVMixin:
    def to_csv(self) -> str:
        ...

    @classmethod
    def from_csv(cls, line: str) -> Union['Astronaut', 'Cosmonaut']:
        ...


# Solution
class CSVMixin:
    def to_csv(self) -> str:
        return ','.join(self.__dict__.values()) + '\n'

    @classmethod
    def from_csv(cls, line: str) -> Union['Astronaut', 'Cosmonaut']:
        data = line.strip().split(',')
        return cls(*data)
