"""
* Assignment: Decorator Function Memoization
* Complexity: easy
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Create decorator `@cache`
    2. Decorator must check before running function, if for given argument
       the computation was already done:
        a. if yes, return from `_cache`
        b. if not, calculate new result, update cache and return computed value
    3. Compare execution time using `timeit` (it might take around 30 seconds)
    4. Last three tests will fail, this is only infomation about execution time
    5. Run doctests - all must succeed

Polish:
    1. Stwórz dekorator `@cache`
    2. Decorator ma sprawdzać przed uruchomieniem funkcji, czy dla danego
       argumentu wynik został już wcześniej obliczony:
        a. jeżeli tak, to zwraca dane z `_cache`
        b. jeżeli nie, to oblicza, aktualizuje `_cache`, a następnie zwraca wartość
    3. Porównaj prędkość działania za pomocą `timeit` (może to trwać około 30 sekund)
    4. Ostatnie trzy testy nie przejdą, to tylko informacja o czasie wykonywania
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from timeit import timeit
    >>> sys.setrecursionlimit(5000)

    >>> @cache
    ... def fn1(n):
    ...     if n == 0:
    ...         return 1
    ...     else:
    ...         return n * fn1(n - 1)


    >>> def fn2(n):
    ...     if n == 0:
    ...         return 1
    ...     else:
    ...         return n * fn2(n - 1)

    >>> duration_cache = timeit(stmt='fn1(500); fn1(400); fn1(450); fn1(350)',
    ...                         globals=globals(), number=10_000)

    >>> duration_nocache = timeit(stmt='fn2(500); fn2(400); fn2(450); fn2(350)',
    ...                           globals=globals(), number=10_000)

    >>> duration_ratio = duration_nocache / duration_cache
    >>> print(f'With Cache time: {duration_cache:.4f} seconds')
    >>> print(f'Without Cache time: {duration_nocache:.3f} seconds')
    >>> print(f'Cached solution is {duration_ratio:.1f} times faster')

    TODO: Make tests faster
"""

_cache = {}


def cache(func):
    def wrapper(n):
        return func(n)
    return wrapper


# Solution
def cache(func):
    def wrapper(n):
        if n not in _cache:
            _cache[n] = func(n)
        return _cache[n]
    return wrapper
