Datetime Parse
==============


Rationale
---------
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.


Parsing dates
-------------
Datetime parsing from string:

>>> from datetime import datetime
>>>
>>>
>>> sputnik = '4 October 1957, 19:28:34 [UTC]'
>>> datetime.strptime(sputnik, '%d %B %Y, %H:%M:%S [%Z]')
datetime.datetime(1957, 10, 4, 19, 28, 34)
>>>
>>> gagarin = '1961-04-12 06:07'
>>> datetime.strptime(gagarin, '%Y-%m-%d %H:%M')
datetime.datetime(1961, 4, 12, 6, 7)
>>>
>>> armstrong = 'Jul 21, 69 2:56:15'
>>> datetime.strptime(armstrong, '%b %d, %y %I:%M:%S')
datetime.datetime(1969, 7, 21, 2, 56, 15)

Use Case
--------
.. code-block:: python

    from datetime import datetime


    line = '1969-07-21T02:56:15.123 [WARNING] First step on the Moon'

    dt, lvl, msg = line.split(maxsplit=2)
    dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    lvl = lvl.strip('[]')

    print(dt)
    # 1969-07-21 02:56:15.123000

    print(lvl)
    # WARNING

    print(msg)
    # First step on the Moon


Parsing Parameters
------------------
.. csv-table:: Date and time parsing parameters
    :header-rows: 1
    :widths: 5,35,60
    :file: data/datetime-formatting.csv

.. todo:: Convert table into smaller parts, based on categories: months, day, hour etc.



Assignments
-----------
.. literalinclude:: assignments/datetime_parse_a.py
    :caption: :download:`Solution <assignments/datetime_parse_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_parse_b.py
    :caption: :download:`Solution <assignments/datetime_parse_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_parse_c.py
    :caption: :download:`Solution <assignments/datetime_parse_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_parse_d.py
    :caption: :download:`Solution <assignments/datetime_parse_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_parse_e.py
    :caption: :download:`Solution <assignments/datetime_parse_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_parse_f.py
    :caption: :download:`Solution <assignments/datetime_parse_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_parse_g.py
    :caption: :download:`Solution <assignments/datetime_parse_g.py>`
    :end-before: # Solution
