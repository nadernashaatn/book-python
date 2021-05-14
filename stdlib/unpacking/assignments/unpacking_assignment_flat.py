"""
* Assignment: Unpacking Assignment Flat
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Using `str.split()` split input data by white space
    3. Separate ip address and host names
    4. Use asterisk `*` notation
    5. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Używając `str.split()` podziel dane wejściowe po białych znakach
    3. Odseparuj adres ip i nazw hostów
    4. Skorzystaj z notacji z gwiazdką `*`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Use `str.split()` without any argument

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(ip)
    <class 'str'>
    >>> type(hosts)
    <class 'list'>
    >>> assert all(type(host) is str for host in hosts)
    >>> '' not in hosts
    True
    >>> ip
    '10.13.37.1'
    >>> hosts
    ['nasa.gov', 'esa.int', 'roscosmos.ru']
"""


# Given
DATA = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

ip: str
hosts: list


# Solution
ip, *hosts = DATA.split()
