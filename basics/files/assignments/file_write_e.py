"""
* Assignment: File Write Iris
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Write `DATA` to file `FILE`
    2. Check in your operating system if data was written correctly
    3. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do pliku `FILE`
    2. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `','.join(...)`
    * Add newline `\n` at the end of line and file

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> open(FILE).read()
    '5.8,2.7,5.1,1.9\\n5.1,3.5,1.4,0.2\\n5.7,2.8,4.1,1.3\\n'
    >>> from os import remove; remove(FILE)
"""

FILE = '_temporary.txt'
DATA = [
    ('5.8', '2.7', '5.1', '1.9'),
    ('5.1', '3.5', '1.4', '0.2'),
    ('5.7', '2.8', '4.1', '1.3'),
]


# Solution
data = []

for row in DATA:
    line = ','.join(row) + '\n'
    data.append(line)

with open(FILE, mode='wt') as file:
    file.writelines(data)
