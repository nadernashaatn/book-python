"""
* Assignment: Idioms Comprehension Translate
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: list`
    3. Use list comprehension to iterate over `DATA`
    4. If letter is in `PL` then use conversion value as letter
    5. Add letter to `result`
    6. Redefine `result: str` as a joined `result`
    7. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: list`
    3. Użyj rozwinięcia listowego do iteracji po `DATA`
    4. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    5. Dodaj literę do `result`
    6. Przedefiniuj `result: str` jako złączony `result`
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str
    >>> result
    'zazolc gesla jazn'
"""


# Given
PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

DATA = 'zażółć gęślą jaźń'

result: str


# Solution
result = ''.join(PL.get(x, x) for x in DATA)
