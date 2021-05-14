"""
* Assignment: Function Unpack Split
* Required: yes
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

    >>> assert ip is not Ellipsis, 'Assignment solution must be in `ip` instead of ... (Ellipsis)'
    >>> assert hosts is not Ellipsis, 'Assignment solution must be in `hosts` instead of ... (Ellipsis)'
    >>> assert type(ip) is str, 'Variable `ip` has invalid type, should be str'
    >>> assert type(hosts) is list, 'Variable `hosts` has invalid type, should be list'
    >>> assert all(type(host) is str for host in hosts)

    >>> ip
    '10.13.37.1'
    >>> hosts
    ['nasa.gov', 'esa.int', 'roscosmos.ru']
"""

DATA = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

ip = ...  # str: first str: 10.13.37.1
hosts = ...  # list[str]: list with all the other str: ['nasa.gov', 'esa.int', 'roscosmos.ru']

# Solution
ip, *hosts = DATA.split()
