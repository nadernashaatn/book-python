"""
* Assignment: Unpacking Assignment Flat
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Using `str.split()` split input data by white space
    2. Separate ip address and host names
    3. Use asterisk `*` notation
    4. Run doctests - all must succeed

Polish:
    1. Używając `str.split()` podziel dane wejściowe po białych znakach
    2. Odseparuj adres ip i nazw hostów
    3. Skorzystaj z notacji z gwiazdką `*`
    4. Uruchom doctesty - wszystkie muszą się powieść

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

DATA = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

ip: str
hosts: list


# Solution
ip, *hosts = DATA.split()
