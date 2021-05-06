"""
* Assignment: Pandas Read CSV Replace
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from `DATA` to `result: pd.DataFrame`
    3. Use provided column names in `COLUMNS`
    4. Read labels from the first row
    5. Replace data in `label` column with values extracted above
    6. Define `result: pd.DataFrame` with 20 first rows
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z `DATA` do `result: pd.DataFrame`
    3. Użyj podanych w `COLUMNS` nazw kolumn
    4. Wczytaj nazwy labeli z pierwszego wiersza
    5. Podmień dane w kolumnie `label` na wartości wyciągnięte powyżej
    6. Zdefiniuj `result: pd.DataFrame` z 20stoma pierwszymi wierszami
    X. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `hader = pd.read_csv(url, nrows=0).columns`
    * `cancer_types = dict(enumerate(header[2:]))`
    * `df['label'].replace({'from': 'to'}, inplace=True)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> len(result) == 20
    True
    >>> result.loc[[0,9,19], ['mean radius', 'mean texture', 'label']]
        mean radius  mean texture      label
    0         17.99         10.38  malignant
    9         12.46         24.04  malignant
    19        13.54         14.36     benign
"""


# Given
import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/breast-cancer.csv'

COLUMNS = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
           'mean smoothness', 'mean compactness', 'mean concavity',
           'mean concave points', 'mean symmetry', 'mean fractal dimension',
           'radius error', 'texture error', 'perimeter error', 'area error',
           'smoothness error', 'compactness error', 'concavity error',
           'concave points error', 'symmetry error',
           'fractal dimension error', 'worst radius', 'worst texture',
           'worst perimeter', 'worst area', 'worst smoothness',
           'worst compactness', 'worst concavity', 'worst concave points',
           'worst symmetry', 'worst fractal dimension', 'label']


# Solution
header = pd.read_csv(DATA, nrows=0).columns
cancer_types = dict(enumerate(header[2:]))

df = pd.read_csv(DATA, skiprows=1, names=COLUMNS)
df['label'].replace(to_replace=cancer_types, inplace=True)
result = df.head(20)
