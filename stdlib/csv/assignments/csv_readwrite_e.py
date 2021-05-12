"""
* Assignment: CSV Read/Write Objects
* Complexity: medium
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Using `csv.DictWriter()` save data to CSV file
    2. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate columns
        c. Use `utf-8` encoding
        d. Use Unix `\n` line terminator
    3. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.DictWriter()` zapisz dane do pliku CSV
    2. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielenia kolumn
        c. Użyj kodowania `utf-8`
        d. Użyj zakończenia linii Unix `\n`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(obj)`
    * For Python before 3.8: `dict(OrderedDict)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = open(FILE).read()
    >>> print(result)
    sepal_length,sepal_width,petal_length,petal_width,species
    5.1,3.5,1.4,0.2,setosa
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    <BLANKLINE>
    >>> from os import remove
    >>> remove(FILE)
"""

from csv import DictWriter


class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species


FILE = r'_temporary.txt'

DATA = [Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
        Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
        Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
        Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
        Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
        Iris(6.4, 3.2, 4.5, 1.5, 'versicolor')]


# Solution
data = [vars(iris) for iris in DATA]
header = data[0].keys()

with open(FILE, mode='w', encoding='utf-8') as file:
    writer = DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
