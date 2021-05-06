"""
* Assignment: Regexp Search Astronauts
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min
* References: First paragraph from Apollo 11 Wikipedia entry :cite:`RegexpWikipediaApollo11`

English:
    1. Use data from "Given" section (see below)
    2. Use `re.search()` to check if Astronaut first and last names are in the text
    3. Astronauts to find:
        a. Neil Armstrong
        b. Buzz Aldrin
        c. Michael Collins
        d. Jan Twardowski
        e. Mark Watney
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj `re.search()` do sprawdzenia czy imiona i nazwiska Astronautów występują w tekście
    3. Astronauci do znalezienia:
        a. Neil Armstrong
        b. Buzz Aldrin
        c. Michael Collins
        d. Jan Twardowski
        e. Mark Watney
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result['armstrong']
    <re.Match object; span=(80, 94), match='Neil Armstrong'>
    >>> result['aldrin']
    <re.Match object; span=(118, 129), match='Buzz Aldrin'>
    >>> result['collins']
    <re.Match object; span=(576, 591), match='Michael Collins'>
    >>> result['twardowski'] is None
    True
    >>> result['watney'] is None
    True
"""


# Given
import re


DATA = """Apollo 11 was the spaceflight that first landed humans on the Moon.
  Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed the American
  crew that landed the Apollo Lunar Module Eagle on July 20, 1969, at 20:17 UTC.
  Armstrong became the first person to step onto the lunar surface six hours and
  39 minutes later on July 21 at 02:56 UTC; Aldrin joined him 19 minutes later.
  They spent about two and a quarter hours together outside the spacecraft,
  and they collected 47.5 pounds (21.5 kg) of lunar material to bring back to Earth.
  Command module pilot Michael Collins flew the command module Columbia alone
  in lunar orbit while they were on the Moon's surface. Armstrong and Aldrin spent
  21 hours, 36 minutes on the lunar surface at a site they named Tranquility Base
  before lifting off to rejoin Columbia in lunar orbit."""

result = {
    'armstrong': ...,
    'aldrin': ...,
    'collins': ...,
    'twardowski': ...,
    'watney': ...,
}


# Solution
result = {
    'armstrong': re.search('Neil Armstrong', DATA),
    'aldrin': re.search('Buzz Aldrin', DATA),
    'collins': re.search('Michael Collins', DATA),
    'twardowski': re.search('Jan Twardowski', DATA),
    'watney': re.search('Mark Watney', DATA),
}
