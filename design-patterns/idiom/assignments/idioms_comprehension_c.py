"""
* Assignment: Idioms Comprehension Translate
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: list`
    2. Use list comprehension to iterate over `DATA`
    3. If letter is in `PL` then use conversion value as letter
    4. Add letter to `result`
    5. Redefine `result: str` as a joined `result`
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list`
    2. Użyj rozwinięcia listowego do iteracji po `DATA`
    3. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    4. Dodaj literę do `result`
    5. Przedefiniuj `result: str` jako złączony `result`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str
    >>> result
    'zazolc gesla jazn'
"""

PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

DATA = 'zażółć gęślą jaźń'

result: str


# Solution
result = ''.join(PL.get(x, x) for x in DATA)
