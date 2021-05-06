"""

* Assignment: Series Mapping Clean
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Convert `DATA` (see input section) to `pd.Series`
    3. Write function to clean up data
    4. Function takes one `str` argument
    5. Function returns cleaned text
    6. Apply function to all elements of `pd.Series`
    7. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj `DATA` (patrz sekcja input) do `pd.Series`
    3. Napisz funkcję czyszczącą dane
    4. Funkcja przyjmuje jeden argument typu `str`
    5. Funkcja zwraca oczyszczony tekst
    6. Zaaplikuj funkcję na wszystkich elementach `pd.Series`
    7. Uruchom doctesty - wszystkie muszą się powieść
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.Series
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    0               Mieszka II
    1        Zygmunta III Wazy
    2      Bolesława Chrobrego
    3     Jana III Sobieskiego
    4     Jana III Sobieskiego
                  ...
    6     Jana III Sobieskiego
    7     Jana III Sobieskiego
    8     Jana III Sobieskiego
    9     Jana III Sobieskiego
    10    Jana III Sobieskiego
    Length: 11, dtype: object

TODO: Translate input data to English
"""


# Given
import pandas as pd



DATA = ['ul.Mieszka II',
        'UL. Zygmunta III WaZY',
        '  bolesława chrobrego ',
        'ul Jana III SobIESkiego',
        '\tul. Jana trzeciego Sobieskiego',
        'ulicaJana III Sobieskiego',
        'UL. JA    NA 3 SOBIES  KIEGO',
        'ULICA JANA III SOBIESKIEGO  ',
        'ULICA. JANA III SOBIeskieGO',
        ' Jana 3 Sobieskiego  ',
        'Jana III Sobi  eskiego ']

def clean(text: str) -> str:
    pass


# Solution

def clean(text: str) -> str:
    # Common format
    text = text.upper()

    # Remove unwanted whitespaces
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('     ', '')
    text = text.replace('    ', '')
    text = text.replace('   ', '')
    text = text.replace('  ', '')

    # Remove unwanted special characters
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('-', '')
    text = text.replace('|', '')

    # Remove unwanted text
    text = text.replace('ULICA', '')
    text = text.replace('UL', '')
    text = text.replace('TRZECIEGO', 'III')
    text = text.replace('3', 'III')

    # Formatting
    text = text.title()
    text = text.replace('Iii', 'III')
    text = text.replace('Ii', 'II')

    # Return
    return text.strip()



result = pd.Series(DATA).apply(clean)
