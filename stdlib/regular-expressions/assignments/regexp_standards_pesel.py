"""
* Assignment: Regexp Standards PESEL
* Complexity: medium
* Lines of code: 0 lines
* Time: 5 min
* Warning: Do no write any code - **discussion only**

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Przeprowadź eksperyment myślowy (**tylko dyskusja**)
    2. Jak sprawdzić za pomocą wyrażeń regularnych czy:
        a. czy pesel jest poprawny?
        b. jaka jest data urodzenia? (podaj obiekt `datetime.date`)
        c. płeć użytkownika który podał PESEL
    3. Mając PESEL "69072101234"
        a. Jakie wyrażenie może być na pierwszym miejscu w PESEL?
        b. Jakie wyrażenie może być na drugim miejscu w PESEL?
        c. Jakie wyrażenie może być na trzecim miejscu w PESEL?
        d. Jakie wyrażenie może być na czwartym miejscu w PESEL?
        e. Jakie wyrażenie może być na piątym miejscu w PESEL?
        f. Jakie wyrażenie może być na szóstym miejscu w PESEL?
    4. Mając PESEL "18220812345"
        a. Jakie wyrażenie może być na pierwszym miejscu w PESEL?
        b. Jakie wyrażenie może być na drugim miejscu w PESEL?
        c. Jakie wyrażenie może być na trzecim miejscu w PESEL?
        d. Jakie wyrażenie może być na czwartym miejscu w PESEL?
        e. Jakie wyrażenie może być na piątym miejscu w PESEL?
        f. Jakie wyrażenie może być na szóstym miejscu w PESEL?
    5. Sprawdź sumę kontrolną
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> is_pesel_valid('69072101234')
    True
    >>> is_pesel_valid('18220812345')
    True
    >>> is_pesel_woman('69072101234')
    False
    >>> is_pesel_woman('18220812345')
    True
"""


# Given
import re


def is_pesel_valid(pesel: str) -> bool:
    ...


def is_pesel_woman(pesel: str) -> bool:
    """
    Check whether PESEL is woman's.
    If the second to last number is even,
    then PESEL is woman's, in other case PESEL is man's.
    """
    ...


# Solution
pattern = r'^\d{11}$'


def is_pesel_valid(pesel):
    if re.match(pattern, pesel):
        return True
    else:
        return False


def is_pesel_woman(pesel):
    if int(pesel[-2]) % 2 == 0:
        return True
    else:
        return False
