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



References
----------
.. [#wikiDateTimeFormats] https://en.wikipedia.org/wiki/Date_format_by_country

.. [#wikiNoonMidnight] https://en.wikipedia.org/wiki/12-hour_clock#Confusion_at_noon_and_midnight

.. [#wikiTimesAfter2400] https://en.wikipedia.org/wiki/24-hour_clock#Times_after_24:00

.. [#wikiMilitaryTime] https://en.wikipedia.org/wiki/24-hour_clock#Military_time

.. [#wikiMilitaryTimezones] https://en.wikipedia.org/wiki/List_of_military_time_zones

.. [#wikiISO8601] https://en.wikipedia.org/wiki/ISO_8601
