"""
* Assignment: Decorator Function Astronauts
* Complexity: easy
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Modify decorator `check_astronauts`
    3. To answer if person is an astronaut check field:
        a. `is_astronaut` in `crew: list[dict]`
    4. Decorator will call function, only if all crew members are astronauts
    5. If any member is not an astronaut raise `PermissionError` and print
       his first name and last name
    6. Run doctests - all must succeed

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Zmodufikuj dekorator `check_astronauts`
    3. Aby odpowiedzieć czy osoba jest astronautą sprawdź pole:
        a. `is_astronaut` in `crew: list[dict]`
    4. Dekorator wywoła funkcję, tylko gdy wszyscy członkowie załogi są astronautami
    5. Jeżeli, jakikolwiek członek nie jest astronautą, podnieś wyjątek
       `PermissionError` i wypisz jego imię i nazwisko
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(check_astronauts)
    >>> assert isfunction(check_astronauts(lambda: None))

    >>> @check_astronauts
    ... def launch(crew):
    ...     crew = ', '.join(astro['name'] for astro in crew)
    ...     return f'Launching: {crew}'

    >>> launch(CREW_PRIMARY)
    'Launching: Jan Twardowski, Mark Watney, Melissa Lewis'

    >>> launch(CREW_BACKUP)
    Traceback (most recent call last):
    PermissionError: Alex Vogel is not an astronaut
"""


# Given
CREW_PRIMARY = [
    {'is_astronaut': True, 'name': 'Jan Twardowski'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': True, 'name': 'Melissa Lewis'}]

CREW_BACKUP = [
    {'is_astronaut': True, 'name': 'Melissa Lewis'},
    {'is_astronaut': True, 'name': 'Mark Watney'},
    {'is_astronaut': False, 'name': 'Alex Vogel'}]


def check_astronauts(func):
    def wrapper(crew):
        return func(crew)
    return wrapper


# Solution
def check_astronauts(func):
    def wrapper(crew):
        for member in crew:
            if not member['is_astronaut']:
                raise PermissionError(f'{member["name"]} is not an astronaut')
        return func(crew)
    return wrapper
