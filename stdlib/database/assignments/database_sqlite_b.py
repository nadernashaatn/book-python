"""
* Assignment: Database SQLite CSV
* Complexity: easy
* Lines of code: 30 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Save `DATA` to `FILE`
    3. Read data from `FILE` (don't use `csv` or `pandas` library)
    4. Replace species from `int` to `str` according to `SPECIES` conversion table
    5. Connect to the `sqlite3` using context manager (`with`)
    6. Create table `iris` and write data to it
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do `FILE`
    3. Wczytaj dane z `FILE` (nie używaj biblioteki `csv` lub `pandas`)
    4. Podmień gatunki z `int` na `str` zgodnie z tabelą podstawień `SPECIES`
    5. Połącz się do bazy danych `sqlite3` używając context managera (`with`)
    6. Stwórz tabelę `iris` i zapisz do niej dane
    X. Uruchom doctesty - wszystkie muszą się powieść

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
     [{'id': 4, 'species': 'virginica', 'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4},
      {'id': 3, 'species': 'versicolor', 'sepal_length': 5.7, 'sepal_width': 4.4, 'petal_length': 1.5, 'petal_width': 0.4},
      {'id': 5, 'species': 'versicolor', 'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.3},
      {'id': 8, 'species': 'versicolor', 'sepal_length': 5.4, 'sepal_width': 3.4, 'petal_length': 1.7, 'petal_width': 0.2},
      {'id': 1, 'species': 'setosa', 'sepal_length': 4.3, 'sepal_width': 3.0, 'petal_length': 1.1, 'petal_width': 0.1},
      {'id': 2, 'species': 'setosa', 'sepal_length': 5.8, 'sepal_width': 4.0, 'petal_length': 1.2, 'petal_width': 0.2},
      {'id': 6, 'species': 'setosa', 'sepal_length': 5.7, 'sepal_width': 3.8, 'petal_length': 1.7, 'petal_width': 0.3},
      {'id': 7, 'species': 'setosa', 'sepal_length': 5.1, 'sepal_width': 3.8, 'petal_length': 1.5, 'petal_width': 0.3},
      {'id': 9, 'species': 'setosa', 'sepal_length': 5.1, 'sepal_width': 3.7, 'petal_length': 1.5, 'petal_width': 0.4},
      {'id': 10, 'species': 'setosa', 'sepal_length': 4.6, 'sepal_width': 3.6, 'petal_length': 1.0, 'petal_width': 0.2}]
    >>> from os import remove
    >>> remove(FILE)
    >>> remove(DATABASE)
"""


# Given
import sqlite3

DATABASE = r'_temporary.sqlite3'
FILE = r'_temporary.csv'

SPECIES = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'}

DATA = """4.3,3.0,1.1,0.1,0
5.8,4.0,1.2,0.2,0
5.7,4.4,1.5,0.4,1
5.4,3.9,1.3,0.4,2
5.1,3.5,1.4,0.3,1
5.7,3.8,1.7,0.3,0
5.1,3.8,1.5,0.3,0
5.4,3.4,1.7,0.2,1
5.1,3.7,1.5,0.4,0
4.6,3.6,1.0,0.2,0"""

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        species TEXT,
        sepal_length REAL,
        sepal_width REAL,
        petal_length REAL,
        petal_width REAL);"""

SQL_CREATE_INDEX = """
    CREATE INDEX IF NOT EXISTS
        iris_species_index ON iris (species);"""

SQL_INSERT = """
    INSERT INTO iris VALUES (
        NULL,
        :species,
        :sepal_length,
        :sepal_width,
        :petal_length,
        :petal_width);"""

SQL_SELECT = """
    SELECT *
    FROM iris
    ORDER BY species DESC, id ASC"""

result: list


# Solution
result = []
data = []

with open(FILE, mode='w') as file:
    file.write(DATA)

with open(FILE) as file:
    for line in file:
        line = line.strip().split(',')
        data.append({
            'sepal_length': float(line[0]),
            'sepal_width': float(line[1]),
            'petal_length': float(line[2]),
            'petal_width': float(line[3]),
            'species': SPECIES[int(line[4])],
        })


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, data)
    db.row_factory = sqlite3.Row

    for row in db.execute(SQL_SELECT):
        result.append(dict(row))
