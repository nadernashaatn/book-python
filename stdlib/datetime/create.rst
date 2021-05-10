Datetime Create
===============


Custom Date and Time
--------------------
Date:

>>> from datetime import date
>>>
>>>
>>> d = date(1969, 7, 21)
>>> print(d)
1969-07-21

Time:

>>> from datetime import time
>>>
>>>
>>> t = time(2, 56, 15)
>>> print(t)
02:56:15

Datetime:

>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>> print(dt)
1969-07-21 02:56:15


Empty Time
----------
>>> from datetime import time
>>>
>>>
>>> time()
datetime.time(0, 0)
>>> time(0, 0)
datetime.time(0, 0)
>>> time(0, 0, 0)
datetime.time(0, 0)
>>> time(12)
datetime.time(12, 0)
>>> time(12, 0)
datetime.time(12, 0)
>>> time(12, 0, 0)
datetime.time(12, 0)
>>> time(24, 0)
Traceback (most recent call last):
ValueError: hour must be in 0..23

>>> from datetime import datetime
>>>
>>>
>>> datetime(1969, 7, 21)
datetime.datetime(1969, 7, 21, 0, 0)


Attributes
----------
>>> from datetime import date
>>>
>>>
>>> d = date(1969, 7, 21)
>>>
>>> d.year
1969
>>> d.month
7
>>> d.day
21

>>> from datetime import time
>>>
>>>
>>> t = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> t.hour
2
>>> t.minute
56
>>> t.second
15
>>> t.microsecond
0

>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> dt.year
1969
>>> dt.month
7
>>> dt.day
21
>>> dt.hour
2
>>> dt.minute
56
>>> dt.second
15
>>> dt.microsecond
0


Current Date and Time
---------------------
Create ``date`` object with current date:

>>> from datetime import date
>>>
>>>
>>> today = date.today()

Create ``datetime`` object with current date and time:

>>> from datetime import datetime
>>>
>>>
>>> now = datetime.now()

There is no ``time.now()``


Combine
-------
Create ``datetime`` from ``date`` and ``time`` objects:

>>> from datetime import datetime, date, time
>>>
>>>
>>> d = date(1969, 7, 21)
>>> t = time(2, 56, 15)
>>>
>>> datetime(
...     year=d.year,
...     month=d.month,
...     day=d.day,
...     hour=t.hour,
...     minute=t.minute,
...     second=t.second)
datetime.datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> datetime(d.year, d.month, d.day, t.hour, t. minute, t.second)
datetime.datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> datetime.combine(d, t)
datetime.datetime(1969, 7, 21, 2, 56, 15)


Split
-----
>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>>
>>> dt.date()
datetime.date(1969, 7, 21)
>>>
>>> dt.time()
datetime.time(2, 56, 15)


Assignments
-----------
.. literalinclude:: assignments/datetime_create_a.py
    :caption: :download:`Solution <assignments/datetime_create_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_create_b.py
    :caption: :download:`Solution <assignments/datetime_create_b.py>`
    :end-before: # Solution
