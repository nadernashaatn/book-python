"""
* Assignment: Numpy Logic Even
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Set random seed to zero
    3. Check for even numbers of `DATA` which are less than 50 and save result to `result`
    4. Check if all `result` matches this condition, result assing to `result_all`
    5. Check if any `result` matches this condition, result assign to `result_any`
    6. Run doctests - all must succeed

Polish:
    1. Ustaw ziarno losowości na zero
    3. Sprawdź parzyste elementy `DATA`, które są mniejsze od 50 i wynik zapisz do `result`
    4. Sprawdź czy wszystkie `result` spełniają ten warunek, wynik zapisz do `result_all`
    5. Sprawdź czy jakakolwiek `result` spełnia ten warunek, wynik zapisz do `result_any`
    6. Uruchom doctesty - wszystkie muszą się powieść

    >>> type(result) is np.ndarray
    True
    >>> result
    array([ True, False, False, False, False, False, False, False,  True])
    >>> result_all
    False
    >>> result_any
    True
"""

import numpy as np
np.random.seed(0)

DATA = np.random.randint(0, 100, size=9)

result = ...
result_all = ...
result_any = ...


# Solution
result = np.logical_and(DATA < 50, DATA % 2 == 0)
result_all = result.all()
result_any = result.any()
