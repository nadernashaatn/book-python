"""
* Assignment: Idioms Comprehension Create
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use list comprehension
    2. Generate `result: list[int]` of even numbers from 5 to 20 (without 20)
    3. Run doctests - all must succeed

Polish:
    1. Użyj rozwinięcia listowego
    2. Wygeneruj `result: list[int]` parzystych liczb z przedziału 5 do 20 (bez 20)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list
    >>> assert all(type(x) is int for x in result)

    >>> result
    [6, 8, 10, 12, 14, 16, 18]
"""

result: list


# Solution
result = [x for x in range(5,20) if x % 2 == 0]

