"""
* Assignment: File Write Non-Str
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Write `DATA` to file `FILE`
    2. Check in your operating system if data was written correctly
    3. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do pliku `FILE`
    2. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `[str(x) for x in ...]`
    * `','.join(...)`
    * Add newline `\n` at the end of line and file

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> open(FILE).read()
    '5.1,3.5,1.4,0.2,setosa\\n'
    >>> from os import remove; remove(FILE)
"""

FILE = '_temporary.txt'
DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')


# Solution
data = ','.join(str(x) for x in DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(data)
