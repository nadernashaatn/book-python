"""
* Assignment: JSON Datetime Encode/Decode
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Save data to `FILE` in JSON format
    2. Read data from `FILE`
    3. Recreate data structure
    4. Run doctests - all must succeed

Polish:
    1. Zapisz dane do `FILE` w formacie JSON
    2. Odczytaj dane z `FILE`
    3. Odtwórz strukturę danych
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> isclass(Encoder)
    True
    >>> isclass(Decoder)
    True
    >>> issubclass(Encoder, json.JSONEncoder)
    True
    >>> issubclass(Decoder, json.JSONDecoder)
    True
    >>> with open(FILE, mode='w') as file:
    ...     json.dump(DATA, file, cls=Encoder)
    >>> with open(FILE, mode='r') as file:
    ...     result = json.load(file, cls=Decoder)
    >>> from os import remove
    >>> remove(FILE)
    >>> type(result)
    <class 'dict'>
    >>> len(result) > 0
    True
    >>> all(type(key) is str
    ...     and type(value) in (str, datetime, list)
    ...     for key, value in result.items())
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'mission': 'Ares 3',
     'launch_date': datetime.datetime(2035, 6, 29, 0, 0, tzinfo=datetime.timezone.utc),
     'destination': 'Mars',
     'destination_landing': datetime.datetime(2035, 11, 7, 0, 0, tzinfo=datetime.timezone.utc),
     'destination_location': 'Acidalia Planitia',
     'crew': [{'astronaut': 'Melissa Lewis', 'date_of_birth': datetime.date(1995, 7, 15)},
              {'astronaut': 'Rick Martinez', 'date_of_birth': datetime.date(1996, 1, 21)},
              {'astronaut': 'Alex Vogel', 'date_of_birth': datetime.date(1994, 11, 15)},
              {'astronaut': 'Chris Beck', 'date_of_birth': datetime.date(1999, 8, 2)},
              {'astronaut': 'Beth Johansen', 'date_of_birth': datetime.date(2006, 5, 9)},
              {'astronaut': 'Mark Watney', 'date_of_birth': datetime.date(1994, 10, 12)}]}
"""

from datetime import datetime, date, timezone
import json

FILE = '_temporary.json'

DATA = {'mission': 'Ares 3',
        'launch_date': datetime(2035, 6, 29, tzinfo=timezone.utc),
        'destination': 'Mars',
        'destination_landing': datetime(2035, 11, 7, tzinfo=timezone.utc),
        'destination_location': 'Acidalia Planitia',
        'crew': [{'astronaut': 'Melissa Lewis', 'date_of_birth': date(1995, 7, 15)},
                 {'astronaut': 'Rick Martinez', 'date_of_birth': date(1996, 1, 21)},
                 {'astronaut': 'Alex Vogel', 'date_of_birth': date(1994, 11, 15)},
                 {'astronaut': 'Chris Beck', 'date_of_birth': date(1999, 8, 2)},
                 {'astronaut': 'Beth Johansen', 'date_of_birth': date(2006, 5, 9)},
                 {'astronaut': 'Mark Watney', 'date_of_birth': date(1994, 10, 12)}]}


class Encoder(json.JSONEncoder):
    def default(self, value: datetime) -> str:
        return ...


class Decoder(json.JSONDecoder):
    def __init__(self) -> None:
        super().__init__(object_hook=self.default)

    def default(self, data: dict) -> dict:
        ...


# Solution
class Encoder(json.JSONEncoder):
    def default(self, value: datetime) -> str:
        return value.isoformat()


class Decoder(json.JSONDecoder):
    def __init__(self) -> None:
        super().__init__(object_hook=self.default)

    def default(self, data: dict) -> dict:
        for key, value in data.items():
            if key in ['destination_landing', 'launch_date']:
                data[key] = datetime.fromisoformat(value)
            elif key == 'date_of_birth':
                data[key] = datetime.fromisoformat(value).date()
        return data
