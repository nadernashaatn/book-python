"""
* Assignment: Database SQLite Relations
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Create database and two tables `astronaut` and `address`
    2. Insert data to separate tables
    3. Join information from both tables
    4. Run doctests - all must succeed

Polish:
    1. Stwórz bazę danych i dwie tabele `astronaut` i `address`
    2. Zapisz dane do osobnych tabel
    3. Połączącz informacje z obu tabel
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'list'>
    >>> len(result) > 0
    True
    >>> all(type(row) is dict
    ...     for row in result)
    True

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'id': 1, 'firstname': 'José', 'lastname': 'Jiménez', 'astronaut_id': 1, 'street': '2101 E NASA Pkwy', 'city': 'Houston', 'state': 'Texas', 'code': 77058, 'country': 'USA'},
     {'id': 1, 'firstname': 'José', 'lastname': 'Jiménez', 'astronaut_id': 1, 'street': None, 'city': 'Kennedy Space Center', 'state': 'Florida', 'code': 32899, 'country': 'USA'},
     {'id': 2, 'firstname': 'Mark', 'lastname': 'Watney', 'astronaut_id': 2, 'street': '4800 Oak Grove Dr', 'city': 'Pasadena', 'state': 'California', 'code': 91109, 'country': 'USA'},
     {'id': 2, 'firstname': 'Mark', 'lastname': 'Watney', 'astronaut_id': 2, 'street': '2825 E Ave P', 'city': 'Palmdale', 'state': 'California', 'code': 93550, 'country': 'USA'},
     {'id': 3, 'firstname': 'Иван', 'lastname': 'Иванович', 'astronaut_id': 3, 'street': '', 'city': 'Космодро́м Байкону́р', 'state': 'Кызылординская область', 'code': None, 'country': 'Қазақстан'},
     {'id': 5, 'firstname': 'Alex', 'lastname': 'Vogel', 'astronaut_id': 5, 'street': 'Linder Hoehe', 'city': 'Köln', 'state': None, 'code': 51147, 'country': 'Germany'}]

    >>> from pathlib import Path
    >>> Path(DATABASE).unlink(missing_ok=True)
"""


# Given
import sqlite3

DATABASE = r'_temporary.sqlite3'

SQL_CREATE_TABLE_ASTRONAUT = """
    CREATE TABLE IF NOT EXISTS astronaut (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT);"""

SQL_CREATE_TABLE_ADDRESS = """
    CREATE TABLE IF NOT EXISTS address (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        astronaut_id INTEGER,
        street TEXT,
        city TEXT,
        state TEXT,
        code INT,
        country TEXT);"""

SQL_CREATE_INDEX_ASTRONAUT_LASTNAME = """
    CREATE INDEX IF NOT EXISTS lastname_index ON astronaut (lastname);"""

SQL_INSERT_ASTRONAUT = """
    INSERT INTO astronaut VALUES (
        NULL,
        :firstname,
        :lastname);"""

SQL_INSERT_ADDRESS = """
    INSERT INTO address VALUES (
        NULL,
        :astronaut_id,
        :street,
        :city,
        :state,
        :code,
        :country);"""

SQL_SELECT = """
    SELECT *
    FROM astronaut
    JOIN address
    ON astronaut.id=address.astronaut_id;
"""

DATA = [
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "code": 77058, "city": "Houston", "state": "Texas", "country": "USA"},
        {"street": None, "code": 32899, "city": "Kennedy Space Center", "state": "Florida", "country": "USA"}]},

    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "code": 91109, "city": "Pasadena", "state": "California", "country": "USA"},
        {"street": "2825 E Ave P", "code": 93550, "city": "Palmdale", "state": "California", "country": "USA"}]},

    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": "", "code": None, "city": "Космодро́м Байкону́р", "state": "Кызылординская область", "country": "Қазақстан"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "code": 51147, "state": None, "country": "Germany"}]}
]

result: list = []

# Solution
with sqlite3.connect(DATABASE) as connection:
    db = connection.cursor()
    db.row_factory = sqlite3.Row

    db.execute(SQL_CREATE_TABLE_ASTRONAUT)
    db.execute(SQL_CREATE_TABLE_ADDRESS)
    db.execute(SQL_CREATE_INDEX_ASTRONAUT_LASTNAME)

    for astronaut in DATA:
        addresses = astronaut.pop('addresses')
        db.execute(SQL_INSERT_ASTRONAUT, astronaut)
        astronaut_id = db.lastrowid

        for addr in addresses:
            addr['astronaut_id'] = astronaut_id
            db.execute(SQL_INSERT_ADDRESS, addr)

    for row in db.execute(SQL_SELECT):
        result.append(dict(row))
