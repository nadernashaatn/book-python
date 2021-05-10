Datetime Standards
==================


Rationale
---------
* Date and time formats varies from country to country [#wikiDateTimeFormats]_


Date
----
Formal date format in USA :cite:`DateFormatUS`:

.. code-block:: text

    4/12/61
    April 12, 1961

Formal date format in Japan :cite:`DateFormatJapan`:

.. code-block:: text

    20/12/31

Formal date format in Germany:

.. code-block:: text

    12.04.1961

Date format in Poland:

.. code-block:: text

    12.4.1961
    12.04.1961

    12 IV 1961
    12.IV.1961

    12/4/1961
    12/04/1961

    12 kwietnia 1961
    12 kwiecień 1961

Which format is a formal standard in Poland? [#wikiISO8601]_


Time
----
24 and 12 hour clock:

    * What AM stands for?
    * What PM stands for?

    .. code-block:: text

        5:00 AM
        5:00 PM
        5:00
        17:00

Zero padded:

    .. code-block:: text

        2:53
        02:53
        02:53:0
        02:53:00

Noon and Midnight

    * Which time is a midnight?
    * Which time is a noon?
    * Confusion at noon and midnight [#wikiNoonMidnight]_
    * Is 12:00 a noon (in 24h format), or someone just simply forgot to put AM/PM?

.. code-block:: text

    12:00 am
    12:00 pm

    12:00
    24:00

    00:00
    0:00


Times after 24:00
-----------------
* Times after 24:00 [#wikiTimesAfter2400]_

.. code-block:: text

    23:59:59
    23:59:60

.. code-block:: text

    25:00
    27:45
    14:00-30:00


Military time
-------------
* Military time [#wikiMilitaryTime]_
* Military time zones [#wikiMilitaryTimezones]_

.. code-block:: text

    1200J
    1200Z


ISO 8601 Standard
-----------------
* ISO 8601 is an International Standard [#wikiISO8601]_

Dates:

.. code-block:: text

    1961-04-12
    1969-07-21

Date and time ("T" separates date and time):

.. code-block:: text

    1961-04-12T06:07:00
    1961-04-12T06:07:00.123
    1961-04-12T06:07:00.123456

Time zone notation ("Z" (Zulu) means UTC):

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

Noon and Midnight:

    * ``00:00`` - midnight, at the beginning of a day
    * ``24:00`` - midnight, at the end of a day (not recommended)
    * ``2007-04-05T24:00`` is equal to ``2007-04-06T00:00``

Weeks (Note year/month changes during the week):

    * ``2009-W01`` - First week of 2009
    * ``2009-W01-1`` - Monday 29 December 2008
    * ``2009-W53-7`` - Sunday 3 January 2010

Duration (Format: ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``)

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


References
----------
.. [#wikiDateTimeFormats] https://en.wikipedia.org/wiki/Date_format_by_country

.. [#wikiNoonMidnight] https://en.wikipedia.org/wiki/12-hour_clock#Confusion_at_noon_and_midnight

.. [#wikiTimesAfter2400] https://en.wikipedia.org/wiki/24-hour_clock#Times_after_24:00

.. [#wikiMilitaryTime] https://en.wikipedia.org/wiki/24-hour_clock#Military_time

.. [#wikiMilitaryTimezones] https://en.wikipedia.org/wiki/List_of_military_time_zones

.. [#wikiISO8601] https://en.wikipedia.org/wiki/ISO_8601
