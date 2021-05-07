"""
* Assignment: Regexp Match Git Flow
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Use regular expressions to validate Git branch names
    2. Check all given branch names (see input section)
    3. Branch names should comply with Git Flow convention:
        a. `release/major.minor` - major and minor are unsigned integers
        b. `feature/`, `bugfix/`, `hotfix/` - branch prefixes
        c. `prefix/ISSUEKEY-NUMBER-summary`
        d. `ISSUEKEY` - uppercase, only ASCII letters, minimum 2 characters, not longer than 10
        e. `NUMBER` - positive integer, maximal 5 digits
        f. `summary` - lowercase, ASCII letters and numbers, dashes instead whitespaces, not longer than 30
        g. `pull-request/NUMBER` - positive integer, maximal 5 digits
    4. Example of valid branches:
        a. `master`
        b. `develop`
        c. `release/1.0`
        d. `feature/ID-1337-some-new-feature`
        e. `bugfix/ID-1337-fixing-old-bug`
        f. `hotfix/ID-1337-bug-on-production`
        g. `pull-request/42`
    X. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych do walidacji nazwy gałęzi w Git
    2. Sprawdź wszystkie dane nazwy gałęzi (patrz sekcja input)
    3. Nazwy gałęzi powinny stosować się do konwencji Git Flow:
        a. `release/major.minor` - major i minor nieujemne liczby całkowite
        b. `feature/`, `bugfix/`, `hotfix/` - prefiks nazwy gałęzi
        c. `prefix/ISSUEKEY-NUMBER-summary`
        d. `ISSUEKEY` - duże litery, tylko litery ASCII, minimum 2 znaki, nie więcej niż 10
        e. `NUMBER` - dodatnia liczba całkowita, maksymalnie 5 cyfr
        f. `summary` - małe litery, litery ASCII i liczby, myślniki zamiast białych spacji, nie dłuższa niż 30
        g. `pull-request/NUMBER` - dodatnia liczba całkowita, maksymalnie 5 cyfr
    4. Przykład poprawnych gałęzi:
        a. `master`
        b. `develop`
        c. `release/1.0`
        d. `feature/ID-1337-some-new-feature`
        e. `bugfix/ID-1337-fixing-old-bug`
        f. `hotfix/ID-1337-bug-on-production`
        g. `pull-request/42`
    X. Uruchom doctesty - wszystkie muszą się powieść
"""


# Given
import re

result = ...


# Solution
