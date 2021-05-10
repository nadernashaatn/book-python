Datetime Format
===============


ISO Format
----------
Datetime formatting to ISO format:

.. code-block:: python

    from datetime import datetime


    dt = datetime(1969, 7, 21, 2, 56, 15)
    dt.isoformat()
    # 1969-07-21T02:56:15

Date formatting to ISO format:

.. code-block:: python

    from datetime import date


    d = date(1969, 7, 21)
    d.isoformat()
    # 1969-07-21


``f-string`` formatting
-----------------------
Datetime formatting as string with ``f'...'``:

.. code-block:: python

    from datetime import datetime


    gagarin = datetime(1961, 4, 12, 6, 7)
    print(f'Gagarin launched on {gagarin:%Y-%m-%d}')
    # Gagarin launched on 1961-04-12

Datetime formatting as string with ``f'...'``:

.. code-block:: python

    from datetime import datetime


    gagarin = datetime(1961, 4, 12, 6, 7)
    print(f'Gagarin launched on {gagarin:%Y-%m-%d %H:%M}')
    # Gagarin launched on 1961-04-12 06:07

Datetime formatting as string with ``f'...'``:

.. code-block:: python

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)
    format = '%Y-%m-%d %H:%M'

    print(f'Gagarin launched on {gagarin:{format}}')
    # Gagarin launched on 1961-04-12 06:07


Format to string
----------------
Datetime formatting as string with ``.strftime()``:

.. code-block:: python

    from datetime import datetime

    gagarin = datetime(1961, 4, 12, 6, 7)
    formatted = gagarin.strftime('%Y-%m-%d %H:%M')

    print(f'Gagarin launched on {formatted}')
    # Gagarin launched on 1961-04-12 06:07


Parameters
----------
.. csv-table:: Date and time parsing and formatting parameters
    :header-rows: 1
    :widths: 5,35,60
    :file: data/datetime-formatting.csv

.. todo:: Convert table into smaller parts, based on categories: months, day, hour etc.


Zero Padding
------------
* https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
* ``%-I`` or ``%_I`` on \*nix systems (macOS, BSD, Linux) to remove leading zero
* ``%#I`` on Windows to remove leading zero
* \*nix: ``%-d``, ``%-H``, ``%-I``, ``%-j``, ``%-m``, ``%-M``, ``%-S``, ``%-U``, ``%-w``, ``%-W``, ``%-y``, ``%-Y``
* Windows: ``%#d``, ``%#H``, ``%#I``, ``%#j``, ``%#m``, ``%#M``, ``%#S``, ``%#U``, ``%#w``, ``%#W``, ``%#y``, ``%#Y``

Almost any programming language has very similar date formatting parameters. There are only some minor differences like in JavaScript minutes are ``i``, not ``M``.



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
