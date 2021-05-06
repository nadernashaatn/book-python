"""
* Assignment: Protocol ContextManager File
* Complexity: easy
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `File` with parameter: `filename: str`
    3. `File` must implement Context Manager protocol
    4. `File` buffers lines added using `File.append(text: str)` method
    5. On `with` block exit `File` class creates, opens and write buffer to file
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz klasę `File` z parametrem: `filename: str`
    3. `File` ma implementować protokół Context Manager
    4. `File` buforuje linie dodawane za pomocą metody `File.append(text: str)`
    5. Na wyjściu z bloku `with` klasa `File` tworzy, otwiera i zapisuje bufor do pliku
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Append newline character (`\n`) before adding to buffer

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(File)
    >>> assert hasattr(File, 'append')
    >>> assert hasattr(File, '__enter__')
    >>> assert hasattr(File, '__exit__')
    >>> assert ismethod(File(None).append)
    >>> assert ismethod(File(None).__enter__)
    >>> assert ismethod(File(None).__exit__)

    >>> with File('_temporary.txt') as file:
    ...    file.append('One')
    ...    file.append('Two')

    >>> open('_temporary.txt').read()
    'One\\nTwo\\n'
    >>> from os import remove
    >>> remove('_temporary.txt')
"""


# Solution
class File:
    filename: str
    _content: list[str]

    def __init__(self, filename):
        self.filename = filename
        self._content = list()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        with open(self.filename, mode='w') as file:
            file.writelines(self._content)

    def append(self, line):
        self._content.append(line + '\n')
