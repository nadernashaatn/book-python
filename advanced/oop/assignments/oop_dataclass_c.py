"""
* Assignment: OOP Dataclass JSON
* Complexity: medium
* Lines of code: 23 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. You received input data in JSON format from the API
    3. Using `dataclass` Model data as class `User`
    4. Parse fields with dates and store as `datetime` objects
    5. Parse fields with `true` and `false` values and store as `bool` objects
    6. Do not create additional classes to represent `permission` filed, leave it as `list[dict]`
    6. Iterate over records and create instances of this class
    7. Collect all instances to one list
    8. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Otrzymałeś z API dane wejściowe w formacie JSON
    3. Wykorzystując `dataclass` zamodeluj dane za pomocą klasy `User`
    4. Sparsuj pola zwierające daty i zapisz je jako obiekty `datetime`
    5. Sparsuj pola zawierające `true` lub `false` i zapamiętaj ich wartości jako obiekty `bool`
    6. Nie twórz dodatkowych klas do reprezentacji pola `permission`, niech zostanie jako `list[dict]`
    7. Iterując po rekordach twórz instancje tej klasy
    8. Zbierz wszystkie instancje do jednej listy
    9. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [User(firstname='Melissa', lastname='Lewis', role='commander', username='mlewis', password='pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=', email='melissa.lewis@nasa.gov', date_of_birth=datetime.date(1995, 7, 15), last_login=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'eclss': ['add', 'modify', 'view']}, {'communication': ['add', 'modify', 'view']}, {'medical': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Rick', lastname='Martinez', role='pilot', username='rmartinez', password='pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=', email='rick.martinez@ansa.gov', date_of_birth=datetime.date(1996, 1, 21), last_login=None, is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'communication': ['add', 'view']}, {'eclss': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Alex', lastname='Vogel', role='chemist', username='avogel', password='pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=', email='alex.vogel@esa.int', date_of_birth=datetime.date(1994, 11, 15), last_login=None, is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'eclss': ['add', 'modify', 'view']}, {'communication': ['add', 'modify', 'view']}, {'medical': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Chris', lastname='Beck', role='crew-medical-officer', username='cbeck', password='pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=', email='chris.beck@nasa.gov', date_of_birth=datetime.date(1999, 8, 2), last_login=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'communication': ['add', 'view']}, {'medical': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Beth', lastname='Johansen', role='sysop', username='bjohansen', password='pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=', email='', date_of_birth=datetime.date(2006, 5, 9), last_login=None, is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'communication': ['add', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Mark', lastname='Watney', role='botanist', username='mwatney', password='pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=', email='', date_of_birth=datetime.date(1994, 10, 12), last_login=None, is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'communication': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}])]
"""


# Given
import json
from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Optional, Union

DATA = '[{"model":"authorization.user","pk":1,"fields":{"firstname":"Melissa","lastname":"Lewis","role":"commander","username":"mlewis","password":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=","email":"melissa.lewis@nasa.gov","date_of_birth":"1995-07-15","last_login":"1970-01-01T00:00:00.000Z","is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"firstname":"Rick","lastname":"Martinez","role":"pilot","username":"rmartinez","password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","date_of_birth":"1996-01-21","last_login":null,"email":"rick.martinez@ansa.gov","is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":3,"fields":{"firstname":"Alex","lastname":"Vogel","role":"chemist","username":"avogel","password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","email":"alex.vogel@esa.int","date_of_birth":"1994-11-15","last_login":null,"is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":4,"fields":{"firstname":"Chris","lastname":"Beck","role":"crew-medical-officer","username":"cbeck","password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","email":"chris.beck@nasa.gov","date_of_birth":"1999-08-02","last_login":"1970-01-01T00:00:00.000Z","is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"communication":["add","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":5,"fields":{"firstname":"Beth","lastname":"Johansen","role":"sysop","username":"bjohansen","password":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=","email":"","date_of_birth":"2006-05-09","last_login":null,"is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"communication":["add","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":6,"fields":{"firstname":"Mark","lastname":"Watney","role":"botanist","username":"mwatney","password":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","email":"","date_of_birth":"1994-10-12","last_login":null,"is_active":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"communication":["add","modify","view"]},{"science":["add","modify","view"]}]}}]'  # noqa


def _clean_time(text: str) -> Union[datetime,date,None]:
    if not text:
        return None

    try:
        return datetime.strptime(text, '%Y-%m-%d').date()
    except ValueError:
        pass

    try:
        return datetime.strptime(text, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
    except TypeError:
        pass


# Solution
@dataclass
class User:
    firstname: str
    lastname: str
    role: str
    username: str
    password: str
    email: str
    date_of_birth: date
    last_login: Optional[datetime]
    is_active: bool
    is_staff: bool
    is_superuser: bool
    user_permissions: list[dict]

    def __post_init__(self):
        self.date_of_birth = _clean_time(self.date_of_birth)
        self.last_login = _clean_time(self.last_login)


result = [User(**u['fields'])
          for u in json.loads(DATA)]

