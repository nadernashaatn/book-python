"""

* Assignment: OOP Relations Model
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. In `DATA` we have two classes
    2. Model data using classes and relations
    3. Create instances dynamically based on `DATA`
    4. Run doctests - all must succeed

Polish:
    1. W `DATA` mamy dwie klasy
    2. Zamodeluj problem wykorzystując klasy i relacje między nimi
    3. Twórz instancje dynamicznie na podstawie `DATA`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list

    >>> assert all(type(astro) is Astronaut
    ...            for astro in result)

    >>> assert all(type(addr) is Address
    ...            for astro in result
    ...            for addr in astro.addresses)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Astronaut(firstname='Jan',
               lastname='Twardowski',
               addresses=[Address(street='Kamienica Pod św. Janem Kapistranem', city='Kraków', postcode='31-008', region='Małopolskie', country='Poland')]),
     Astronaut(firstname='José',
               lastname='Jiménez',
               addresses=[Address(street='2101 E NASA Pkwy', city='Houston', postcode=77058, region='Texas', country='USA'),
                          Address(street='', city='Kennedy Space Center', postcode=32899, region='Florida', country='USA')]),
     Astronaut(firstname='Mark',
               lastname='Watney',
               addresses=[Address(street='4800 Oak Grove Dr', city='Pasadena', postcode=91109, region='California', country='USA'),
                          Address(street='2825 E Ave P', city='Palmdale', postcode=93550, region='California', country='USA')]),
     Astronaut(firstname='Иван',
               lastname='Иванович',
               addresses=[Address(street='', city='Космодро́м Байкону́р', postcode='', region='Кызылординская область', country='Қазақстан'),
                          Address(street='', city='Звёздный городо́к', postcode=141160, region='Московская область', country='Россия')]),
     Astronaut(firstname='Melissa',
               lastname='Lewis',
               addresses=[]),
     Astronaut(firstname='Alex',
               lastname='Vogel',
               addresses=[Address(street='Linder Hoehe', city='Köln', postcode=51147, region='North Rhine-Westphalia', country='Germany')])]
"""

from dataclasses import dataclass
from typing import Optional, Union


DATA = [
    {"firstname": "Jan", "lastname": "Twardowski", "addresses": [
        {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "postcode": "31-008", "region": "Małopolskie", "country": "Poland"}]},
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "postcode": 77058, "region": "Texas", "country": "USA"},
        {"street": "", "city": "Kennedy Space Center", "postcode": 32899, "region": "Florida", "country": "USA"}]},
    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "postcode": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "postcode": 93550, "region": "California", "country": "USA"}]},
    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": "", "city": "Космодро́м Байкону́р", "postcode": "", "region": "Кызылординская область", "country": "Қазақстан"},
        {"street": "", "city": "Звёздный городо́к", "postcode": 141160, "region": "Московская область", "country": "Россия"}]},
    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},
    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "postcode": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
]

result: list


# Solution
@dataclass
class Address:
    street: str
    city: str
    postcode: Union[int, str]
    region: str
    country: str


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    addresses: Optional[list[Address]]


result = []

for row in DATA:
    addresses = [Address(**addr) for addr in row.pop('addresses')]
    astro = Astronaut(**row, addresses=addresses)
    result.append(astro)
