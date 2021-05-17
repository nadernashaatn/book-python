"""
* Assignment: Entry Test File
* Complexity: hard
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Skip comments (`#`) and empty lines
    2. Extract from each line: ip, host and protocol and add to `result: list[dict]`
    3. Each line must be a separate dict
    4. Merge host names with the same IP
    5. IPv4 protocol address is when dot (`.`) is in ip address
    6. `result` must be `list[dict]`
    7. Run doctests - all must succeed

Polish:
    1. Pomiń komentarze (`#`) i puste linie
    2. Wyciągnij z każdej linii: ip, host i protokół i dodaj do `result: list[dict]`
    3. Każda linia ma być osobnym słownikiem
    4. Scal nazwy hostów dla tego samego IP
    5. Protokół IPv4 jest gdy kropka (`.`) znajduje się w adresie
    6. `result` musi być `list[dict]`
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result must be a list'

    >>> assert len(result) > 0, \
    'Result cannot be empty'

    >>> assert all(type(row) is dict for row in result), \
    'All elements in result must be a dict'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt'], 'protocol': 'ipv4'},
     {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int', 'roscosmos.ru'], 'protocol': 'ipv4'},
     {'ip': '255.255.255.255', 'hosts': ['broadcasthost'], 'protocol': 'ipv4'},
     {'ip': '::1', 'hosts': ['localhost'], 'protocol': 'ipv6'}]
"""

DATA = """
##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
 ##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""

result: list


# Solution
result = []

for line in DATA.splitlines():
    line = line.strip()

    if len(line) == 0:
        continue
    elif line.startswith('#'):
        continue

    ip, *hosts = line.split()

    for row in result:
        if row['ip'] == ip:
            row['hosts'] += hosts
            break
    else:
        result.append({
            'ip': ip,
            'hosts': hosts,
            'protocol': 'ipv4' if '.' in ip else 'ipv6'
        })
