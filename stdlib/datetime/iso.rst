Datetime ISO Standard
=====================


Rationale
---------
* ISO 8601 is an International Standard [#wikiISO8601]_


Dates
-----
.. code-block:: text

    1961-04-12
    1969-07-21

Format ``date`` to string in ISO-8601 standard:

>>> from datetime import date
>>>
>>>
>>> d = date(1969, 7, 21)
>>> d.isoformat()
'1969-07-21'

Create ``date`` object from ISO-8601 formatted string:

>>> from datetime import date
>>>
>>> text = '1969-07-21'
>>> date.fromisoformat(text)
datetime.date(1969, 7, 21)


Time
----
* 24 hour clock
* ``00:00`` - midnight, at the beginning of a day
* ``24:00`` - midnight, at the end of a day (not recommended)
* ``2007-04-05T24:00`` is equal to ``2007-04-06T00:00``


Date and Time
-------------
* "T" separates date and time):

.. code-block:: text

    1961-04-12T06:07:00
    1961-04-12T06:07:00.123
    1961-04-12T06:07:00.123456


Format ``datetime`` to string in ISO-8601 standard:

>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>> dt.isoformat()
'1969-07-21T02:56:15'

Create ``datetime`` object from ISO-8601 formatted string:

>>> from datetime import datetime
>>>
>>>
>>> text = '1969-07-21T02:56:15'
>>> datetime.fromisoformat(text)
datetime.datetime(1969, 7, 21, 2, 56, 15)


Timezone
--------
* "Z" (Zulu) means UTC
* Time zone notation:

    * ``<time>UTC``
    * ``<time>Z``
    * ``<time>±hh:mm``
    * ``<time>±hhmm``
    * ``<time>±hh``

.. code-block:: text

    1961-04-12T06:07:00.123456Z
    1961-04-12T06:07:00.123456UTC

    1961-04-12T06:07:00.123456CEST
    1961-04-12T06:07:00.123456CET
    1961-04-12T06:07:00.123456+02:00
    1961-04-12T06:07:00.123456+0200
    1961-04-12T06:07:00.123456+02


Weekday
-------
* Note year/month changes during the week
* ``2009-W01`` - First week of 2009
* ``2009-W01-1`` - Monday 29 December 2008
* ``2009-W53-7`` - Sunday 3 January 2010
* ISO defines Monday as one

>>> from datetime import datetime
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>> dt.isoweekday()
1


Duration
--------
* Format: ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``
* ``P`` - placed at the start of the duration (period) representation
* ``Y`` - number of years
* ``M`` - number of months
* ``W`` - number of weeks
* ``D`` - number of days
* ``T`` - precedes the time components of the representation
* ``H`` - number of hours
* ``M`` - number of minutes
* ``S`` - number of seconds

.. code-block:: text

    P8Y3M8DT20H49M15S

    8 years
    3 months
    8 days
    20 hours
    49 minutes
    15 seconds



Assignments
-----------
.. literalinclude:: assignments/datetime_iso_a.py
    :caption: :download:`Solution <assignments/datetime_iso_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_iso_b.py
    :caption: :download:`Solution <assignments/datetime_iso_b.py>`
    :end-before: # Solution
