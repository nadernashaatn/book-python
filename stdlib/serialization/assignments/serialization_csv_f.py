"""
* Assignment: Serialization CSV Relations
* Complexity: hard
* Lines of code: 11 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Using `csv.DictWriter()` save contacts from addressbook to CSV file
    3. How to write relations to CSV file (contact has many addresses)?
    4. Recreate object structure from CSV file
    5. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate mission fields
        c. Use `;` to separate missions
        d. Use Unix `\n` newline
        e. Sort fieldnames
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Za pomocą `csv.DictWriter()` zapisz kontakty z książki adresowej w pliku
    3. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
    4. Odtwórz strukturę obiektów na podstawie danych odczytanych z pliku
    5. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielania pól mission
        c. Użyj `;` do oddzielenia missions
        d. Użyj zakończenia linii Unix `\n`
        e. Posortuj fieldnames
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(obj)`
    * For Python before 3.8: `dict(OrderedDict)`

Tests:
    >>> result = open(FILE).read()
    >>> print(result)
    "lastname","missions","name"
    "Twardowski","1969,Apollo 11;2024,Artemis 3","Jan"
    "Watney","2035,Ares 3","Mark"
    "Lewis","","Melissa"
    <BLANKLINE>
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
import csv

FILE = r'_temporary.csv'


class Astronaut:
    def __init__(self, firstname, lastname, missions=None):
        self.name = firstname
        self.lastname = lastname
        self.missions = list(missions) if missions else []

class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


CREW = [
    Astronaut('Jan', 'Twardowski', missions=[
        Mission(1969, 'Apollo 11'),
        Mission(2024, 'Artemis 3')]),

    Astronaut('Mark', 'Watney', missions=[
        Mission(2035, 'Ares 3')]),

    Astronaut('Melissa', 'Lewis'),
]

result: list

# Solution
result = list()

for member in CREW:
    astronaut = vars(member)
    missions = [','.join(str(x) for x in vars(mission).values())
                for mission in astronaut.pop('missions')]
    astronaut['missions'] = ';'.join(missions)
    result.append(astronaut)


# result = [astronaut | {'missions': ';'.join(values)}
#           for member in CREW
#           if (astronaut := vars(member))
#           and (values := [','.join(str(x) for x in vars(mission).values())
#                           for mission in astronaut.pop('missions')]) or True]



with open(FILE, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(result[0].keys()), quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)
