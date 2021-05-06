"""
* Assignment: File Read Passwd
* Required: no
* Complexity: hard
* Lines of code: 100 lines
* Time: 55 min

English:
    1. Save listings content to files:
        a. `etc_passwd.txt`
        b. `etc_shadow.txt`
        c. `etc_group.txt`
    2. Copy also comments and empty lines
    3. Parse files and convert it to `result: list[dict]`
    4. Return list of users with `UID` greater than 1000
    5. User dict should contains data collected from all files
    6. Run doctests - all must succeed

Polish:
    1. Zapisz treści listingów do plików:
        a. `etc_passwd.txt`
        b. `etc_shadow.txt`
        c. `etc_group.txt`
    2. Skopiuj również komentarze i puste linie
    3. Sparsuj plik i przedstaw go w formacie `result: list[dict]`
    4. Zwróć listę użytkowników, których `UID` jest większy niż 1000
    5. Dict użytkownika powinien zawierać dane z wszystkich plików
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'username': 'watney',
      'uid': 1000,
      'gid': 1000,
      'home': '/home/watney',
      'shell': '/bin/bash',
      'algorithm': None,
      'password': None,
      'groups': ['astronauts', 'mars'],
      'last_changed': datetime.date(2015, 4, 25),
      'locked': True},
     {'username': 'twardowski',
      'uid': 1001,
      'gid': 1001,
      'home': '/home/twardowski',
      'shell': '/bin/bash',
      'algorithm': 'SHA-512',
      'password': 'tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50',
      'groups': ['astronauts', 'sysadmin', 'moon'],
      'last_changed': datetime.date(2015, 7, 16),
      'locked': False},
     {'username': 'ivanovic',
      'uid': 1002,
      'gid': 1002,
      'home': '/home/ivanovic',
      'shell': '/bin/bash',
      'algorithm': 'MD5',
      'password': 'SWlkjRWexrXYgc98F.',
      'groups': ['astronauts', 'sysadmin'],
      'last_changed': datetime.date(2005, 2, 11),
      'locked': False}]
"""

from datetime import date
from os.path import dirname, join

BASE_DIR = dirname(__file__)
FILE_GROUP = join(BASE_DIR, '../data/etc-group.txt')
FILE_SHADOW = join(BASE_DIR, '../data/etc-shadow.txt')
FILE_PASSWD = join(BASE_DIR, '../data/etc-passwd.txt')

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}

result: list


# Solution
result_group = {}
result_shadow = {}
result_passwd = {}
result = []

try:
    with open(FILE_GROUP, encoding='utf-8') as file:
        etc_group = file.readlines()
except FileNotFoundError:
    print(f'File {FILE_GROUP} does not exist')
except PermissionError:
    print('Permission denied')


try:
    with open(FILE_SHADOW, encoding='utf-8') as file:
        etc_shadow = file.readlines()
except FileNotFoundError:
    print(f'File {FILE_SHADOW} does not exist')
except PermissionError:
    print('Permission denied')


try:
    with open(FILE_PASSWD, encoding='utf-8') as file:
        etc_passwd = file.readlines()
except FileNotFoundError:
    print(f'File {FILE_PASSWD} does not exist')
except PermissionError:
    print('Permission denied')


for line in etc_group:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    group_name, _, _, members, *_ = line.split(':')

    if not members:
        continue

    for member in members.split(','):
        if member not in result_group.keys():
            result_group[member] = list()

        result_group[member].append(group_name)


for line in etc_shadow:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    username, password, last_change, *_ = line.split(':')
    timestamp = int(last_change) * DAY
    last_change = date.fromtimestamp(timestamp)

    if password.startswith('$'):
        locked = False
        password = password.split('$')
        password_algorithm = ALGORITHMS[password[1]]
        password_salt = password[2]
        password_password = password[3]
    else:
        locked = True
        password_algorithm = None
        password_salt = None
        password_password = None

    result_shadow[username] = {
        'password': password_password,
        'salt': password_salt,
        'algorithm': password_algorithm,
        'last_change': last_change,
        'locked': locked,
    }


for line in etc_passwd:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    record = line.split(':')
    username = record[0]

    result_passwd[username] = {
        'password': record[1],
        'uid': int(record[2]),
        'gid': int(record[3]),
        'gecos': record[4],
        'home': record[5],
        'shell': record[6],
    }


for user in result_passwd:
    passwd = result_passwd.get(user)
    groups = result_group.get(user)
    shadow = result_shadow.get(user)

    if passwd['uid'] < 1000:
        continue

    result.append(
        {
            'username': user,
            'uid': passwd['uid'],
            'gid': passwd['gid'],
            'home': passwd['home'],
            'shell': passwd['shell'],
            'algorithm': shadow['algorithm'],
            'password': shadow['password'],
            'groups': groups,
            'last_changed': shadow['last_change'],
            'locked': shadow['locked'],
        }
    )
