"""
* Assignment: Pandas Read JSON OpenAPI
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from `DATA` as `df: pd.DataFrame`
    3. Use `requests` library
    4. Transpose data
    5. If cell is a `dict`, then extract value for `summary`
    6. If cell is empty, leave `pd.NA`
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    3. Użyj biblioteki `requests`
    4. Transponuj dane
    5. Jeżeli komórka jest `dict`, to wyciągnij wartość dla `summary`
    6. Jeżeli komórka jest pusta, pozostaw `pd.NA`
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> len(result) > 0
    True
    >>> list(result.columns)
    ['put', 'post', 'get', 'delete']
    >>> list(result.index)  # doctest: +NORMALIZE_WHITESPACE
    ['/pet', '/pet/findByStatus', '/pet/findByTags', '/pet/{petId}', '/pet/{petId}/uploadImage',
     '/store/inventory', '/store/order', '/store/order/{orderId}',
     '/user', '/user/createWithList', '/user/login', '/user/logout', '/user/{username}']
"""


# Given
import pandas as pd
import requests


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/openapi.json'

result = ...


# Solution
df = requests.get(DATA).json()
result = (pd.DataFrame(df['paths'])
            .transpose()
            .applymap(lambda x: x['summary'] if type(x) == dict else pd.NA))
