Datetime Timezone
=================


Rationale
---------
* Always keep dates and times only in UTC (**important!**)
* Datetimes should be converted to local time only when displaying to user
* Computerphile Time & Time Zones :cite:`VideoComputerphileTimeZones`

Comparing datetime works only when all has the same timezone (UTC):

.. figure:: img/datetime-compare.png


Timezone Naive Datetimes
------------------------
>>> from datetime import datetime
>>>
>>>
>>> datetime(1957, 10, 4, 19, 28, 34)
datetime.datetime(1957, 10, 4, 19, 28, 34)
>>>
>>> datetime.now()  # doctest: +SKIP
datetime.datetime(1957, 10, 4, 19, 28, 34)


Timezone Aware Datetimes
------------------------
>>> from datetime import datetime, timezone
>>>
>>>
>>> datetime.now(timezone.utc)  # doctest: +SKIP
datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)
>>>
>>> datetime(1957, 10, 4, 19, 28, 34, tzinfo=timezone.utc)
datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)
>>>
>>> dt = datetime(1957, 10, 4, 19, 28, 34)
>>> dt.replace(tzinfo=timezone.utc)
datetime.datetime(1957, 10, 4, 19, 28, 34, tzinfo=datetime.timezone.utc)


UTCNow
------
* ``datetime.utcnow()`` produces timezone naive datetimes!

>>> from datetime import datetime, timezone
>>>
>>>
>>> datetime.utcnow()  # doctest: +SKIP
datetime.datetime(1957, 10, 4, 17, 28, 34)
>>>
>>> datetime.utcnow(tz=timezone.utc)
Traceback (most recent call last):
TypeError: datetime.utcnow() takes no keyword arguments
>>>
>>> datetime.utcnow(timezone.utc)
Traceback (most recent call last):
TypeError: datetime.utcnow() takes no arguments (1 given)


IANA Time Zone Database
-----------------------
* https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
* https://www.iana.org/time-zones

IANA 2017a timezone database [#IANA]_:

.. figure:: img/datetime-timezone-iana2017a.png


ZoneInfo
--------
* Since Python 3.9: :pep:`615` -- Support for the IANA Time Zone Database in the Standard Library
* https://docs.python.org/3/library/zoneinfo.html

>>> from zoneinfo import ZoneInfo
>>>
>>>
>>> utc = ZoneInfo('UTC')
>>> est = ZoneInfo('US/Eastern')
>>> cet = ZoneInfo('Europe/Warsaw')
>>> alm = ZoneInfo('Asia/Almaty')

Working with ``ZoneInfo`` objects:

>>> from zoneinfo import ZoneInfo
>>> from datetime import datetime, timedelta
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15, tzinfo=ZoneInfo('UTC'))
>>> print(dt)
1969-07-21 02:56:15+00:00
>>>
>>> dt += timedelta(days=7)
>>> print(dt)
1969-07-28 02:56:15+00:00

``ZoneInfo`` objects knows Daylight Saving Time:

>>> from zoneinfo import ZoneInfo
>>> from datetime import datetime, timedelta
>>>
>>>
>>> dt = datetime(2000, 1, 1, tzinfo=ZoneInfo('America/Los_Angeles'))  # Daylight saving time
>>> dt.tzname()
'PST'
>>> dt += timedelta(days=100)  # Standard time
>>> dt.tzname()
'PDT'


Pytz
----
``pytz`` brings the Olson tz database into Python:

>>> from pytz import timezone
>>>
>>>
>>> utc = timezone('UTC')
>>> est = timezone('US/Eastern')
>>> waw = timezone('Europe/Warsaw')
>>> alm = timezone('Asia/Almaty')

From naive to local time:

>>> from datetime import datetime
>>> from pytz import timezone
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>> dt = timezone('UTC').localize(dt)
>>> dt
datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=<UTC>)

From naive to local time:

>>> from datetime import datetime
>>> from pytz import timezone
>>>
>>>
>>> dt = datetime(1961, 4, 12, 6, 7)
>>> dt = timezone('Asia/Almaty').localize(dt)
>>> dt
datetime.datetime(1961, 4, 12, 6, 7, tzinfo=<DstTzInfo 'Asia/Almaty' +06+6:00:00 STD>)

From UTC to local time:

>>> from datetime import datetime
>>> from pytz import timezone
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15, tzinfo=timezone('UTC'))
>>> dt = dt.astimezone(timezone('Europe/Warsaw'))
>>> dt
datetime.datetime(1969, 7, 21, 3, 56, 15, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)

Between timezones:

>>> from datetime import datetime
>>> from pytz import timezone
>>>
>>>
>>> dt = datetime(1961, 4, 12, 6, 7, tzinfo=timezone('Asia/Almaty'))
>>> dt = dt.astimezone(timezone('Europe/Warsaw'))
>>> dt
datetime.datetime(1961, 4, 12, 1, 59, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)


Use Case
--------
Descriptor Timezone Converter:

>>> from dataclasses import dataclass
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
>>>
>>>
>>> class Timezone:
...     def __init__(self, name):
...         self.timezone = ZoneInfo(name)
...
...     def __get__(self, parent, *args):
...         return parent.utc.astimezone(self.timezone)
...
...     def __set__(self, parent, new_datetime):
...         parent.utc = new_datetime.astimezone(ZoneInfo('UTC'))
>>>
>>>
>>> @dataclass
>>> class Time:
...     utc = datetime.now(tz=ZoneInfo('UTC'))
...     warsaw = Timezone('Europe/Warsaw')
...     moscow = Timezone('Europe/Moscow')
...     est = Timezone('America/New_York')
...     pdt = Timezone('America/Los_Angeles')
>>>
>>>
>>> t = Time()
>>>
>>> t.moscow = datetime(1961, 4, 12, 9, 6, 59)  # Launch of a first man to space
>>> print(t.utc)
1961-04-12 08:06:59+00:00
>>> print(t.warsaw)
1961-04-12 09:06:59+01:00
>>> print(t.moscow)
1961-04-12 11:06:59+03:00
>>> print(t.est)
1961-04-12 03:06:59-05:00
>>> print(t.pdt)
1961-04-12 00:06:59-08:00
>>>
>>>
>>> t.warsaw = datetime(1969, 7, 21, 3, 56, 15) # First man set foot on a Moon
>>> print(t.utc)
1969-07-21 02:56:15+00:00
>>> print(t.warsaw)
1969-07-21 03:56:15+01:00
>>> print(t.moscow)
1969-07-21 05:56:15+03:00
>>> print(t.est)
1969-07-20 22:56:15-04:00
>>> print(t.pdt)
1969-07-20 19:56:15-07:00


Assignments
-----------
.. literalinclude:: assignments/datetime_timezone_a.py
    :caption: :download:`Solution <assignments/datetime_timezone_a.py>`
    :end-before: # Solution


References
----------
.. [#IANA] IANA. Time Zone Database. Year: 2017. Retrieved: 2019-08-05.
