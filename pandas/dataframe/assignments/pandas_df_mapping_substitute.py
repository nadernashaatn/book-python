"""
* Assignment: DataFrame Mapping Substitute
* Complexity: medium
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from `DATA` as `df: pd.DataFrame`
    3. Select `Polish` spreadsheet
    4. Set header and index to data from file
    5. Mind the encoding
    6. Substitute Polish Diacritics to English alphabet letters
    7. Compare `df.replace(regex=True)` with `df.applymap()`
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    3. Wybierz arkusz `Polish`
    4. Ustaw nagłówek i index na dane zaczytane z pliku
    5. Zwróć uwagę na encoding
    6. Podmień polskie znaki diakrytyczne na litery z alfabetu angielskiego
    7. Porównaj `df.replace(regex=True)` z `df.applymap()`
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 3)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
                                                 Definicja  ...                                 Kryteria wyjsciowe
    TRL                                                     ...
    1    Zaobserwowanie i opisanie podstawowych zasad d...  ...  Zweryfikowane publikacja badania lezacych u po...
    2    Sformulowanie koncepcji technologicznej lub pr...  ...  Udokumentowany opis aplikacji / koncepcji, kto...
    3    Przeprowadzanie eksperymentalnie i analityczni...  ...  Udokumentowane wyniki analityczne / eksperymen...
    4    Przeprowadzenie weryfikacji komponentow techno...  ...  Udokumentowane wyniki testow potwierdzajace zg...
    5    Przeprowadzenie weryfikacji komponentow techno...  ...  Udokumentowane wyniki testow potwierdzajace zg...
    6    Dokonanie demonstracji technologii w srodowisk...  ...  Udokumentowane wyniki testow potwierdzajace zg...
    7    Dokonanie demonstracji prototypu systemu w oto...  ...  Udokumentowane wyniki testow potwierdzajace zg...
    8    Zakonczenie badan i demonstracja ostatecznej f...  ...  Udokumentowane wyniki testow weryfikujacych pr...
    9    Weryfikacja technologii w srodowisku operacyjn...  ...            Udokumentowane wyniki operacyjne misji.
    <BLANKLINE>
    [9 rows x 4 columns]
"""


# Given
import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/xlsx/astro-trl.xlsx'
LETTERS_PLEN = {'ą': 'a', 'ć': 'c', 'ę': 'e',
                'ł': 'l', 'ń': 'n', 'ó': 'o',
                'ś': 's', 'ż': 'z', 'ź': 'z'}

result = ...


# Solution
LETTERS_PLEN.update({k.upper():v.upper()
                     for k,v in LETTERS_PLEN.items()})


def substitute(text):
    return ''.join(LETTERS_PLEN.get(x,x) for x in text)


df = pd.read_excel(io=DATA, sheet_name='Polish', header=1, index_col=0)
df = df.applymap(substitute)
df.columns = df.columns.map(substitute)
result = df
