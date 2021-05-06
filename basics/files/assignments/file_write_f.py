"""
* Assignment: File Write CSV
* Required: yes
* Complexity: medium
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Separate header from data
    2. Write data to file: `FILE`
    3. First line in file must be a header (first line of `DATA`)
    4. For each row, convert it's values to `str`
    5. Use coma (`,`) as a value separator
    6. Add line terminator (`\n`) to each row
    7. Save row values to file
    8. Run doctests - all must succeed

Polish:
    1. Odseparuj nagłówek od danych
    2. Zapisz dane do pliku: `FILE`
    3. Pierwsza linia w pliku musi być nagłówkiem (pierwsza linia `DATA`)
    4. Dla każdego wiersza przekonwertuj jego wartości do `str`
    5. Użyj przecinka (`,`) jako separatora wartości
    6. Użyj `\n` jako koniec linii w każdym wierszu
    7. Zapisz do pliku wartości z wiersza
    8. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `','.join(...)`
    * `[str(x) for x in ...]`
    * Add newline `\n` at the end of line and file

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = open(FILE).read()
    >>> print(result)
    Sepal length,Sepal width,Petal length,Petal width,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    4.7,3.2,1.3,0.2,setosa
    <BLANKLINE>
    >>> from os import remove; remove(FILE)
"""

FILE = '_temporary.csv'
DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


# Solution
header, *data = DATA

data = []
for row in DATA:
    row = ','.join(str(x) for x in row)
    data.append(row + '\n')

with open(FILE, mode='w') as file:
    file.writelines(data)
