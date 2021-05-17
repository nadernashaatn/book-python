"""
* Assignment: Functional Map Filter Lambda
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Używając generatora zbuduj listę zawierającą wszystkie liczby podzielne przez 3 z zakresu od 1 do 33:
    2. Używając funkcji `filter()` usuń z niej wszystkie liczby parzyste
    3. Używając wyrażenia `lambda` i funkcji `map()` podnieś wszystkie elementy tak otrzymanej listy do sześcianu
    4. Odpowiednio używając funkcji `sum()`  i `len()` oblicz średnią arytmetyczną z elementów tak otrzymanej listy.
    5. Uruchom doctesty - wszystkie muszą się powieść
"""

NUMBERS = range(1, 34)



# Solution
div3 = [x for x in NUMBERS if x % 3 == 0]
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]

even = filter(lambda x: not x % 2 == 0, div3)
# <filter object at 0x117c639d0>
# [3, 9, 15, 21, 27, 33]

pow3 = map(lambda x: pow(x, 3), even)
# <map object at 0x117c7ac10>
# [3, 9, 15, 21, 27, 33]

numbers = list(pow3)
# [27, 729, 3375, 9261, 19683, 35937]

mean = sum(numbers) / len(numbers)
# 11502.0
