"""
* Assignment: Regexp Match Phones
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Use regular expressions to validate phone numbers
    3. Valid phone number format: `+## ### ### ###` or `+## ## ### ####`
    4. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj wyrażeń regularnych do walidacji numeru telefonu
    3. Poprawne format numeru: `+## ### ### ###` lub `+## ## ### ####`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> def is_valid_phone(number):
    ...     if re.match(pattern, number):
    ...         return True
    ...     else:
    ...         return False

    >>> is_valid_phone('+48 (12) 355 5678')
    False
    >>> is_valid_phone('+48 123 555 678')
    True
    >>> is_valid_phone('123 555 678')
    False
    >>> is_valid_phone('+48 12 355 5678')
    True
    >>> is_valid_phone('+48 123-555-678')
    False
    >>> is_valid_phone('+48 123 555 6789')
    False
    >>> is_valid_phone('+1 (123) 555-6789')
    False
    >>> is_valid_phone('+1 (123).555.6789')
    False
    >>> is_valid_phone('+1 800-python')
    False
    >>> is_valid_phone('+48123555678')
    False
    >>> is_valid_phone('+48 123 555 678 wew. 1337')
    False
    >>> is_valid_phone('+48 123555678,1')
    False
    >>> is_valid_phone('+48 123555678,1,2,3')
    False
"""


# Given
import re

pattern = ...  # str: pattern matching `+## ### ### ###` and `+## ## ### ####`


# Solution
cell = r'\+\d{2} \d{3} \d{3} \d{3}'
work = r'\+\d{2} \d{2} \d{3} \d{4}'
pattern = f'^({cell}|{work})$'
