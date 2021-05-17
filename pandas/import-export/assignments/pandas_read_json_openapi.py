"""
* Assignment: Pandas Read JSON OpenAPI
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Define `resp` with result of `requests.get()` for `DATA`
    2. Define `data` with conversion of `resp` from JSON to Python dict by calling `.json()` on `resp`
    3. Define `result: pd.DataFrame` from value for key `paths` in `data` dict
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `resp` z resultatem `requests.get()` dla `DATA`
    2. Zdefiniuj `data` z przekształceniem `resp` z JSON do Python dict wywołując `.json()` na `resp`
    3. Zdefiniuj `result: pd.DataFrame` dla wartości z klucza `paths` w słowniku `data`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pd.DataFrame(data)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> list(result.index)
    ['put', 'post', 'get', 'delete']
    >>> list(result.columns)  # doctest: +NORMALIZE_WHITESPACE
    ['/pet', '/pet/findByStatus', '/pet/findByTags', '/pet/{petId}', '/pet/{petId}/uploadImage',
     '/store/inventory', '/store/order', '/store/order/{orderId}',
     '/user', '/user/createWithList', '/user/login', '/user/logout', '/user/{username}']
"""

import pandas as pd
import requests

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/openapi.json'


resp = ...
data = ...
result = ...

# Solution
resp = requests.get(DATA)
data = resp.json()['paths']
result = pd.DataFrame(data)
