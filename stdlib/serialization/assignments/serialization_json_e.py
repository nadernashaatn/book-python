"""
* Assignment: Serialization JSON HTTP
* Complexity: easy
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    1. Use `requests` library (requires installation)
    2. Download data from https://api.github.com/users
    3. Model data as class `User`
    4. Iterate over records and create instances of this class
    5. Collect all instances to one list
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    1. Użyj biblioteki `requests` (wymagana instalacja)
    2. Pobierz dane z https://api.github.com/users
    3. Zamodeluj dane za pomocą klasy `User`
    4. Iterując po rekordach twórz instancje tej klasy
    5. Zbierz wszystkie instancje do jednej listy
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'list'>
    >>> len(result) > 0
    True
    >>> all(type(row) is User
    ...     for row in result)
    True
    >>> result[0]  # doctest: +NORMALIZE_WHITESPACE
    User(login='mojombo',
         id=1,
         node_id='MDQ6VXNlcjE=',
         avatar_url='https://avatars.githubusercontent.com/u/1?v=4',
         gravatar_id='',
         url='https://api.github.com/users/mojombo',
         html_url='https://github.com/mojombo',
         followers_url='https://api.github.com/users/mojombo/followers',
         following_url='https://api.github.com/users/mojombo/following{/other_user}',
         gists_url='https://api.github.com/users/mojombo/gists{/gist_id}',
         starred_url='https://api.github.com/users/mojombo/starred{/owner}{/repo}',
         subscriptions_url='https://api.github.com/users/mojombo/subscriptions',
         organizations_url='https://api.github.com/users/mojombo/orgs',
         repos_url='https://api.github.com/users/mojombo/repos',
         events_url='https://api.github.com/users/mojombo/events{/privacy}',
         received_events_url='https://api.github.com/users/mojombo/received_events',
         type='User',
         site_admin=False)
"""


# Given
import requests


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/github-users.json'
DATA = requests.get(DATA).json()
result: list = []


class User:
    pass


# Solution
from dataclasses import dataclass


@dataclass
class User:
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


result = [User(**user) for user in DATA]

