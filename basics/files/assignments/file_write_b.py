"""
* Assignment: File Write Multiline
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

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> open(FILE).read()
    '127.0.0.1       localhost\\n10.13.37.1      nasa.gov esa.int roscosmos.ru\\n255.255.255.255 broadcasthost\\n::1             localhost\\n'
    >>> from os import remove; remove(FILE)
"""

FILE = '_temporary.txt'
DATA = """127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""


# Solution
with open(FILE, mode='wt') as file:
    file.write(DATA)
