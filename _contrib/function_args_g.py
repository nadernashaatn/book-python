"""
* Assignment: Function Arguments Numbers to Human
* Complexity: hard
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Define function converting `int` or `float` to text form
    2. Text form must be in proper grammar form
    3. Max 6 digits before decimal separator (point `.`)
    4. Max 5 digits after decimal separator (point `.`)
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję konwertującą `int` lub `float` na formę tekstową
    2. Forma tekstowa musi być poprawna gramatycznie
    3. Max 6 cyfr przed separatorem dziesiętnym (point `.`)
    4. Max 5 cyfr po separatorze dziesiętnym (point `.`)
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(number_to_str)
    True
    >>> number_to_str(1969)  # doctest: +SKIP
    'one thousand nine hundred sixty nine'
    >>> number_to_str(31337)  # doctest: +SKIP
    'thirty one thousand three hundred thirty seven'
    >>> number_to_str(13.37)  # doctest: +SKIP
    'thirteen and thirty seven hundredths'
    >>> number_to_str(31.337)  # doctest: +SKIP
    'thirty one and three hundreds thirty seven thousands'
    >>> number_to_str(-1969)  # doctest: +SKIP
    'minus one thousand nine hundred sixty nine'
    >>> number_to_str(-31.337)  # doctest: +SKIP
    'minus thirty one and three hundreds thirty seven thousands'
    >>> number_to_str(-49.35)  # doctest: +SKIP
    'minus forty nine and thirty five hundreds'
"""

MIN = 1e-3
MAX = 1e6


DIGITS = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four',
          5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}

TEENS = {10: 'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen',
         15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

TENS = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
        60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}


def number_to_str(number):
    return


# Solution
def number_to_str(number):
    if MIN <= number < MAX:
        raise OverflowError

