"""
* Assignment: Mapping Dict Get
* Required: no
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Create translator of pilot's alphabet
    2. Each letter has it's phonetic counterpart
    3. Ask user to input letter
    4. User will always put only one capitalized letter or number
    5. Define `result: str` with phonetic letter pronunciation
    6. If user type character not existing in alphabet, print: "Pilots don't say that"
    7. Do not use `if`, `try`, and `except`
    8. `MagicMock` will simulate inputting a letter by user
    9. Use `input()` function as normal
    10. Run doctests - all must succeed

Polish:
    1. Stwórz tłumacza alfabetu pilotów
    2. Pojedynczym literom przyporządkuj ich fonetyczne odpowiedniki
    3. Poproś użytkownika o wprowadzenie litery
    4. Użytkownik zawsze poda tylko jedną dużą literę lub cyfrę
    5. Zdefiniuj `result: str` z fonetyczną wymową litery
    6. Jeżeli wpisał znak, który nie występuje w alfabecie, wypisz: "Pilots don't say that"
    7. Nie używaj `if`, `try` ani `except`
    8. `MagicMock` zasymuluje wpisanie litery przez użytkownika
    9. Skorzytaj z funkcji `input()` tak jak normalnie
    10. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result
    'Mike'
"""

# Simulate user input (for test automation)
from unittest.mock import MagicMock
input = MagicMock(side_effect=['M'])


ALPHABET = {
    'A': 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whisky',
    'X': 'X-Ray',
    'Z': 'Zulu',
}

letter = ...  # str: with letter from user
result = ...  # str: with converted letter to Pilot alphabet or "Pilots don't say that"

# Solution
letter = input('Type letter: ')
result = ALPHABET.get(letter, "Pilots don't say that")
