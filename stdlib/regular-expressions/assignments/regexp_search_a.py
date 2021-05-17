"""
* Assignment: Regexp Search Astronauts
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Use `re.search()` to check if Astronaut first and last names are in the text [1]
    2. Astronauts to find:
        a. Neil Armstrong
        b. Buzz Aldrin
        c. Michael Collins
        d. Jan Twardowski
        e. Mark Watney
    3. Run doctests - all must succeed

Polish:
    1. Użyj `re.search()` do sprawdzenia czy imiona i nazwiska Astronautów występują w tekście [1]
    2. Astronauci do znalezienia:
        a. Neil Armstrong
        b. Buzz Aldrin
        c. Michael Collins
        d. Jan Twardowski
        e. Mark Watney
    3. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Kennedy, J.F. Moon Speech - Rice Stadium,
        URL: http://er.jsc.nasa.gov/seh/ricetalk.htm
        Year: 2019
        Retreived: 2019-12-14

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result['Neil Armstrong']
    <re.Match object; span=(78, 92), match='Neil Armstrong'>
    >>> result['Buzz Aldrin']
    <re.Match object; span=(116, 127), match='Buzz Aldrin'>
    >>> result['Michael Collins']
    <re.Match object; span=(562, 577), match='Michael Collins'>
    >>> result['Jan Twardowski'] is None
    True
    >>> result['Mark Watney'] is None
    True
"""

import re


DATA = ("Apollo 11 was the spaceflight that first landed humans on the Moon. "
        "Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed "
        "the American crew that landed the Apollo Lunar Module Eagle on "
        "July 20, 1969, at 20:17 UTC. Armstrong became the first person to "
        "step onto the lunar surface six hours and 39 minutes later on "
        "July 21 at 02:56 UTC; Aldrin joined him 19 minutes later. They spent "
        "about two and a quarter hours together outside the spacecraft, "
        "and they collected 47.5 pounds (21.5 kg) of lunar material to bring "
        "back to Earth. Command module pilot Michael Collins flew the command "
        "module Columbia alone in lunar orbit while they were on the Moon's "
        "surface. Armstrong and Aldrin spent 21 hours, 36 minutes on the "
        "lunar surface at a site they named Tranquility Base before lifting "
        "off to rejoin Columbia in lunar orbit. ")

result = {
    'Neil Armstrong': ...,
    'Buzz Aldrin': ...,
    'Michael Collins': ...,
    'Jan Twardowski': ...,
    'Mark Watney': ...,
}


# Solution
result = {
    'Neil Armstrong': re.search('Neil Armstrong', DATA),
    'Buzz Aldrin': re.search('Buzz Aldrin', DATA),
    'Michael Collins': re.search('Michael Collins', DATA),
    'Jan Twardowski': re.search('Jan Twardowski', DATA),
    'Mark Watney': re.search('Mark Watney', DATA),
}
