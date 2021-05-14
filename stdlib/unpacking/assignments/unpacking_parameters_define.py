"""
* Assignment: Unpacking Parameters Define
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Create function `mean()`, which calculates arithmetic mean
    2. Function can have arbitrary number of positional arguments
    3. Do not import any libraries and modules
    4. Run doctests - all must succeed

Polish:
    1. Napisz funkcję `mean()`, wyliczającą średnią arytmetyczną
    2. Funkcja przyjmuje dowolną ilość pozycyjnych argumentów
    3. Nie importuj żadnych bibliotek i modułów
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `sum(...) / len(...)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mean(1)
    1.0
    >>> mean(1, 3)
    2.0
    >>> mean()
    Traceback (most recent call last):
    ValueError: At least one argument is required
"""


# Solution
def mean(*args):
    if not args:
        raise ValueError('At least one argument is required')
    return sum(args) / len(args)
