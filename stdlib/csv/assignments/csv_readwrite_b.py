"""
* Assignment: CSV Read/Write DictWriter
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Using `csv.DictWriter()` save `DATA` to file
    2. Open file in your spreadsheet program like Microsoft Excel / Libre Office / Numbers etc.
    3. Open file in simple in your IDE and simple text editor (like Notepad, vim, gedit)
    4. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate columns
        d. Use Unix `\n` line terminator
    5. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.DictWriter()` zapisz `DATA` do pliku
    2. Spróbuj otworzyć plik w arkuszu kalkulacyjnym tj. Microsoft Excel / Libre Office / Numbers itp
    3. Spróbuj otworzyć plik w IDE i prostym edytorze tekstu tj. Notepad, vim lub gedit
    4. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielenia kolumn
        d. Użyj zakończenia linii Unix `\n`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * For Python before 3.8: `dict(OrderedDict)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = open(FILE).read()
    >>> print(result)   # doctest: +NORMALIZE_WHITESPACE
    "firstname","lastname"
    "Jan","Twardowski"
    "Rick","Martinez"
    "Mark","Watney"
    "Ivan","Ivanovic"
    "Melissa","Lewis"
    >>> from os import remove
    >>> remove(FILE)
"""

FILE = r'_temporary.csv'

DATA = [{'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'firstname': 'Rick', 'lastname': 'Martinez'},
        {'firstname': 'Mark', 'lastname': 'Watney'},
        {'firstname': 'Ivan', 'lastname': 'Ivanovic'},
        {'firstname': 'Melissa', 'lastname': 'Lewis'}]


# Solution
from csv import DictWriter, QUOTE_ALL


with open(FILE, mode='w') as file:
    data = DictWriter(file, fieldnames=['firstname', 'lastname'],
                      delimiter=',', quotechar='"', quoting=QUOTE_ALL,
                      lineterminator='\n')

    data.writeheader()
    data.writerows(DATA)
