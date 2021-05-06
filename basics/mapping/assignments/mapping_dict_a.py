"""
* Assignment: Mapping Dict Define
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create `result: dict` representing input data
    2. Non-functional requirements:
        a. Assignmnet verifies creation of `dict()`
        b. Do not parse `DATA`, simply model `result` based on `DATA`
        c. Do not use `str.split()`, `slice`, `getitem`, `for`, `while` or any other control-flow statement
    3. Run doctests - all must succeed

Polish:
    1. Stwórz `result: dict` reprezentujący dane wejściowe
    2. Wymagania niefunkcjonalne:
        a. Zadanie sprawdza tworzenie `dict()`
        b. Nie parsuj `DATA`, po prostu zamodeluj `result` bazując na `DATA`
        c. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>
    >>> 'First Name' in result.keys()
    True
    >>> 'Last Name' in result.keys()
    True
    >>> 'Missions' in result.keys()
    True
    >>> result['First Name'] == 'Jan'
    True
    >>> result['Last Name'] == 'Twardowski'
    True
    >>> 'Apollo' in result['Missions']
    True
    >>> 'Artemis' in result['Missions']
    True
"""

DATA = """
    First Name: Jan
    Last Name: Twardowski
    Missions: Apollo, Artemis
"""

result = ...  # dict[str,str|list]: with First Name, Last Name and Missions as keys


# Solution
result = {
    'First Name': 'Jan',
    'Last Name': 'Twardowski',
    'Missions': ['Apollo', 'Artemis'],
}
