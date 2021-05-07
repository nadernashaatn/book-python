Regexp Split
============


About
-----
* ``re.split()``
* Split text by pattern


Examples
--------
Usage of ``re.split()``:

.. code-block:: python

    import re

    PATTERN = r'\s[a-z]{3}\s'
    DATA = 'Baked Beans And Spam'

    re.split(PATTERN, DATA, flags=re.IGNORECASE)
    # ['Baked Beans', 'Spam']

Making a Phonebook:

.. code-block:: python

    import re


    TEXT = """Jan Twardowski: 834.345.1254 Polish Space Agency

    Mark Watney: 892.345.3428 Johnson Space Center
    Matt Kowalski: 925.541.7625 Kennedy Space Center


    Melissa Lewis: 548.326.4584 Bajkonur, Kazakhstan"""

    entries = re.split('\n+', TEXT)
    print(entries)
    # [
    #   'Jan Twardowski: 834.345.1254 Polish Space Agency',
    #   'Mark Watney: 892.345.3428 Johnson Space Center',
    #   'Matt Kowalski: 925.541.7625 Kennedy Space Center',
    #   'Melissa Lewis: 548.326.4584 Bajkonur, Kazakhstan'
    # ]

    result = [re.split(':?\s', entry, maxsplit=3) for entry in entries]
    print(result)
    # [
    #   ['Jan', 'Twardowski', '834.345.1254', 'Polish Space Agency'],
    #   ['Mark', 'Watney', '892.345.3428', 'Johnson Space Center'],
    #   ['Matt', 'Kowalski', '925.541.7625', 'Kennedy Space Center'],
    #   ['Melissa', 'Lewis', '548.326.4584', 'Bajkonur, Kazakhstan']
    # ]

Assignments
-----------
.. literalinclude:: assignments/regexp_split_a.py
    :caption: :download:`Solution <assignments/regexp_split_a.py>`
    :end-before: # Solution
