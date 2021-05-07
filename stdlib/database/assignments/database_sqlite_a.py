"""
* Assignment: Database SQLite Logs
* Complexity: easy
* Lines of code: 17 lines
* Time: 21 min

English:
    1. Extract date, time, log level and message from each line in `FILE`
    2. Collect data to `data: list[dict]` (see below)
    3. Create database schema for logs
    4. Add all logs to database
    5. Use `SQL_SELECT` query to extract data
    6. Iterate over rows and append each to `result: list[dict]`
    7. Run doctests - all must succeed

Polish:
    1. Wyciągnij datę, czas, poziom logowania i teść z każdej linii w `FILE`
    2. Zbierz dane do `data: list[dict]` (patrz sekcja input)
    3. Stwórz schemat bazy danych dla logów
    4. Dodaj wszystkie linie do bazy danych
    5. Użyj zapytania `SQL_SELECT` do wyciągnięcia danych
    6. Iterując po wierszach dopisuj je do `result: list[dict]`
    7. Uruchom doctesty - wszystkie muszą się powieść

References:
    * Apollo 11 timeline https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm

Hints:
    * `datetime.fromisoformat()`

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
    [{'id': 28, 'datetime': '1969-07-24 17:29:00', 'level': 'INFO', 'message': 'Crew egress'},
     {'id': 27, 'datetime': '1969-07-24 16:50:35', 'level': 'WARNING', 'message': 'Splashdown (went to apex-down)'},
     {'id': 26, 'datetime': '1969-07-24 16:35:05', 'level': 'WARNING', 'message': 'Entry'},
     {'id': 25, 'datetime': '1969-07-24 16:21:12', 'level': 'INFO', 'message': 'CM/SM separation'},
     {'id': 24, 'datetime': '1969-07-22 04:55:42', 'level': 'WARNING', 'message': 'Transearth injection ignition (SPS)'},
     {'id': 23, 'datetime': '1969-07-21 21:35:00', 'level': 'INFO', 'message': 'CSM/LM docked'},
     {'id': 22, 'datetime': '1969-07-21 17:54:00', 'level': 'WARNING', 'message': 'LM lunar liftoff ignition (LM APS)'},
     {'id': 21, 'datetime': '1969-07-21 05:11:13', 'level': 'DEBUG', 'message': 'EVA ended (hatch closed)'},
     {'id': 20, 'datetime': '1969-07-21 03:15:16', 'level': 'INFO', 'message': 'LMP on lunar surface'},
     {'id': 19, 'datetime': '1969-07-21 03:05:58', 'level': 'DEBUG', 'message': 'Contingency sample collection started (CDR)'},
     {'id': 18, 'datetime': '1969-07-21 02:56:15', 'level': 'WARNING', 'message': "That's one small step for [a] man... one giant leap for mankind"},
     {'id': 17, 'datetime': '1969-07-21 02:56:15', 'level': 'WARNING', 'message': '1st step taken lunar surface (CDR)'},
     {'id': 16, 'datetime': '1969-07-21 02:39:33', 'level': 'DEBUG', 'message': 'EVA started (hatch open)'},
     {'id': 15, 'datetime': '1969-07-20 20:17:39', 'level': 'WARNING', 'message': 'LM lunar landing'},
     {'id': 14, 'datetime': '1969-07-20 20:14:18', 'level': 'ERROR', 'message': 'LM 1201 alarm'},
     {'id': 13, 'datetime': '1969-07-20 20:10:22', 'level': 'ERROR', 'message': 'LM 1202 alarm'},
     {'id': 12, 'datetime': '1969-07-20 20:05:05', 'level': 'WARNING', 'message': 'LM powered descent engine ignition'},
     {'id': 11, 'datetime': '1969-07-20 17:44:00', 'level': 'INFO', 'message': 'CSM/LM undocked'},
     {'id': 10, 'datetime': '1969-07-16 21:43:36', 'level': 'INFO', 'message': 'Lunar orbit circularization ignition'},
     {'id': 9, 'datetime': '1969-07-16 17:21:50', 'level': 'INFO', 'message': 'Lunar orbit insertion ignition'},
     {'id': 8, 'datetime': '1969-07-16 16:56:03', 'level': 'INFO', 'message': 'CSM docked with LM/S-IVB'},
     {'id': 7, 'datetime': '1969-07-16 16:22:13', 'level': 'INFO', 'message': 'Translunar injection'},
     {'id': 6, 'datetime': '1969-07-16 13:39:40', 'level': 'DEBUG', 'message': 'S-II center engine cutoff'},
     {'id': 5, 'datetime': '1969-07-16 13:35:17', 'level': 'DEBUG', 'message': 'Launch escape tower jettisoned'},
     {'id': 4, 'datetime': '1969-07-16 13:34:44', 'level': 'WARNING', 'message': 'S-II ignition'},
     {'id': 3, 'datetime': '1969-07-16 13:33:23', 'level': 'DEBUG', 'message': 'Maximum dynamic pressure (735.17 lb/ft^2)'},
     {'id': 2, 'datetime': '1969-07-16 13:31:53', 'level': 'WARNING', 'message': 'S-IC engine ignition (#5)'},
     {'id': 1, 'datetime': '1969-07-14 21:00:00', 'level': 'INFO', 'message': 'Terminal countdown started'}]

    >>> from pathlib import Path
    >>> Path(DATABASE).unlink(missing_ok=True)
"""

import sqlite3
from datetime import datetime, timezone

DATABASE = r'_temporary.sqlite3'

DATA = """1969-07-14, 21:00:00, INFO, Terminal countdown started
1969-07-16, 13:31:53, WARNING, S-IC engine ignition (#5)
1969-07-16, 13:33:23, DEBUG, Maximum dynamic pressure (735.17 lb/ft^2)
1969-07-16, 13:34:44, WARNING, S-II ignition
1969-07-16, 13:35:17, DEBUG, Launch escape tower jettisoned
1969-07-16, 13:39:40, DEBUG, S-II center engine cutoff
1969-07-16, 16:22:13, INFO, Translunar injection
1969-07-16, 16:56:03, INFO, CSM docked with LM/S-IVB
1969-07-16, 17:21:50, INFO, Lunar orbit insertion ignition
1969-07-16, 21:43:36, INFO, Lunar orbit circularization ignition
1969-07-20, 17:44:00, INFO, CSM/LM undocked
1969-07-20, 20:05:05, WARNING, LM powered descent engine ignition
1969-07-20, 20:10:22, ERROR, LM 1202 alarm
1969-07-20, 20:14:18, ERROR, LM 1201 alarm
1969-07-20, 20:17:39, WARNING, LM lunar landing
1969-07-21, 02:39:33, DEBUG, EVA started (hatch open)
1969-07-21, 02:56:15, WARNING, 1st step taken lunar surface (CDR)
1969-07-21, 02:56:15, WARNING, That's one small step for [a] man... one giant leap for mankind
1969-07-21, 03:05:58, DEBUG, Contingency sample collection started (CDR)
1969-07-21, 03:15:16, INFO, LMP on lunar surface
1969-07-21, 05:11:13, DEBUG, EVA ended (hatch closed)
1969-07-21, 17:54:00, WARNING, LM lunar liftoff ignition (LM APS)
1969-07-21, 21:35:00, INFO, CSM/LM docked
1969-07-22, 04:55:42, WARNING, Transearth injection ignition (SPS)
1969-07-24, 16:21:12, INFO, CM/SM separation
1969-07-24, 16:35:05, WARNING, Entry
1969-07-24, 16:50:35, WARNING, Splashdown (went to apex-down)
1969-07-24, 17:29, INFO, Crew egress"""


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime DATETIME,
        level TEXT,
        message TEXT);"""

SQL_CREATE_INDEX = """
    CREATE INDEX IF NOT EXISTS
        logs_datetime_index ON logs (datetime);"""

SQL_INSERT = """
    INSERT INTO logs VALUES (
        NULL,
        :datetime,
        :level,
        :message);"""

SQL_SELECT = 'SELECT * FROM logs ORDER BY datetime DESC'


result: list = []

# Solution
data = []

for line in DATA.splitlines():
    date, time, level, message = line.strip().split(', ', maxsplit=3)
    date = datetime.strptime(date, '%Y-%m-%d').date()

    try:
        time = datetime.strptime(time, '%H:%M:%S').time()
    except ValueError:
        time = datetime.strptime(time, '%H:%M').time()

    dt = datetime.combine(date, time)
    data.append({'datetime': dt, 'level': level, 'message': message})


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.execute(SQL_CREATE_INDEX)
    db.executemany(SQL_INSERT, data)
    db.row_factory = sqlite3.Row

    for row in db.execute(SQL_SELECT):
        result.append(dict(row))

