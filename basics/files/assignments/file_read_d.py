"""
* Assignment: File Read Dict
* Required: no
* Complexity: medium
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Write `DATA` to file `FILE`
    2. Read `FILE` and for each line:
        a. Remove leading and trailing whitespaces
        b. Skip line if it is empty
        c. Split line by whitespace
        d. Separate IP address and hosts names
        e. Append IP address and hosts names to `result`
    3. Merge hostnames for the same IP
    4. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do pliku `FILE`
    2. Wczytaj `FILE` i dla każdej linii:
        a. Usuń białe znaki na początku i końcu linii
        b. Pomiń linię, jeżeli jest pusta
        c. Podziel linię po białych znakach
        d. Odseparuj adres IP i nazwy hostów
        e. Dodaj adres IP i nazwy hostów do `result`
    3. Scal nazwy hostów dla tego samego IP
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.isspace()`
    * `str.split()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'127.0.0.1': ['localhost'],
     '10.13.37.1': ['nasa.gov', 'esa.int', 'roscosmos.ru'],
     '255.255.255.255': ['broadcasthost'],
     '::1': ['localhost']}
    >>> from os import remove; remove(FILE)
"""

FILE = '_temporary.txt'

DATA = """127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='w') as file:
    file.write(DATA)


result = {}


# Solution
with open(FILE) as file:
    for line in file:
        ip, *hosts = line.strip().split()

        if ip in result:
            result[ip] += hosts
        else:
            result[ip] = hosts
