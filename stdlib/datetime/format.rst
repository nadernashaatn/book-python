Datetime Format
===============


String Format Time
------------------
>>> from datetime import datetime
>>>
>>>
>>> gagarin = datetime(1961, 4, 12, 6, 7)
>>> formatted = gagarin.strftime('%Y-%m-%d %H:%M')
>>>
>>> print(f'Gagarin launched on {formatted}')
Gagarin launched on 1961-04-12 06:07


Format String
-------------
>>> from datetime import datetime
>>>
>>>
>>> gagarin = datetime(1961, 4, 12, 6, 7)
>>>
>>> print(f'Gagarin launched on {gagarin:%Y-%m-%d}')
Gagarin launched on 1961-04-12
>>>
>>> print(f'Gagarin launched on {gagarin:%Y-%m-%d %H:%M}')
Gagarin launched on 1961-04-12 06:07

>>> from datetime import datetime
>>>
>>>
>>> gagarin = datetime(1961, 4, 12, 6, 7)
>>> format = '%Y-%m-%d %H:%M'
>>>
>>> print(f'Gagarin launched on {gagarin:{format}}')
Gagarin launched on 1961-04-12 06:07


Parameters
----------
* Almost any programming language has very similar date formatting parameters
* Some minor differences like in JavaScript minutes are ``i``, not ``M``

.. csv-table:: Date and time parsing and formatting parameters
    :header-rows: 1
    :widths: 5,35,60
    :file: data/datetime-formatting.csv

.. todo:: Convert table into smaller parts, based on categories: months, day, hour etc.


Leading Zero
------------
* https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
* ``%-I`` or ``%_I`` on \*nix systems (macOS, BSD, Linux) to remove leading zero
* ``%#I`` on Windows to remove leading zero
* \*nix: ``%-d``, ``%-H``, ``%-I``, ``%-j``, ``%-m``, ``%-M``, ``%-S``, ``%-U``, ``%-w``, ``%-W``, ``%-y``, ``%-Y``
* Windows: ``%#d``, ``%#H``, ``%#I``, ``%#j``, ``%#m``, ``%#M``, ``%#S``, ``%#U``, ``%#w``, ``%#W``, ``%#y``, ``%#Y``


Assignments
-----------
.. literalinclude:: assignments/datetime_format_a.py
    :caption: :download:`Solution <assignments/datetime_format_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/datetime_format_b.py
    :caption: :download:`Solution <assignments/datetime_format_b.py>`
    :end-before: # Solution
