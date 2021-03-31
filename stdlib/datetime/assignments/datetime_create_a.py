"""
* Assignment: Datetime Create Custom
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. First human (Yuri Gagarin) flown to space on
       April 12th, 1961 at 6:07 a.m. from Bajkonur Cosmodrome in Kazahstan
    2. Create `date` object representing date of the launch
    3. Create `time` object representing time of the launch
    4. Combine date and time into `datetime` object representing
       exact moment of the launch

Polish:
    1. Pierwszy człowiek (Juri Gagarin) poleciał w kosmos
       12 kwietnia 1961 roku o 6:07 rano z kosmodromu Bajkonur w Kazachstanie
    1. Stwórz obiekt `date` reprezentujący datę startu
    2. Stwórz obiekt `time` reprezentujący czas startu
    3. Połąćż datę i czas w obiekt `datetime` reprezentujący
       dokładny moment startu

Tests:
    >>> assert type(dt) is datetime, \
    'Variable `dt` has invalid type, must be a datetime'

    >>> assert type(d) is date, \
    'Variable `dt` has invalid type, must be a date'

    >>> assert type(t) is time, \
    'Variable `t` has invalid type, must be a time'

    >>> str(d)
    '1961-04-12'
    >>> str(t)
    '06:07:00'
    >>> str(dt)
    '1961-04-12 06:07:00'
"""


# Given
from datetime import datetime, date, time


d = ...  # date: representing April 12th, 1961 6:07 a.m.
t = ...  # time: representing April 12th, 1961 6:07 a.m.
dt = ...  # datetime: representing April 12th, 1961 6:07 a.m.


# Solution
d = date(1961, 4, 12)
t = time(6, 7)
dt = datetime.combine(d, t)