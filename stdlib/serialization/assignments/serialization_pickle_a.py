"""
* Assignment: Pickle Serialization
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Using `pickle` save data structure to file
    2. Recreate data structure from file
    3. Run doctests - all must succeed

Polish:
    1. Za pomocą `pickle` zapisz strukturę danych do pliku
    2. Odtwórz strukturę danych na podstawie danych z pliku
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Astronaut(name='Jan Twardowski', missions=[Mission(year=1969, name='Apollo 18'), Mission(year=2024, name='Artemis 3')]),
     Astronaut(name='Mark Watney', missions=[Mission(year=2035, name='Ares 3')]),
     Astronaut(name='Melissa Lewis', missions=[])]
    >>> from os import remove
    >>> remove(FILE)
"""

import pickle
from dataclasses import dataclass, field

FILE = r'_temporary.pkl'


@dataclass
class Astronaut:
    name: str
    missions: list = field(default_factory=list)


@dataclass
class Mission:
    year: int
    name: str


CREW = [
    Astronaut('Jan Twardowski', missions=[
        Mission(1969, 'Apollo 18'),
        Mission(2024, 'Artemis 3')]),

    Astronaut('Mark Watney', missions=[
        Mission(2035, 'Ares 3')]),

    Astronaut('Melissa Lewis'),
]


# Solution
with open(FILE, mode='wb') as file:
    pickle.dump(CREW, file)


with open(FILE, mode='rb') as file:
    result = pickle.load(file)
