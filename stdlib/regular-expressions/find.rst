Regexp Findall, Finditer
========================


About
-----
* ``re.findall()``
* ``re.finditer()``


Examples
--------
Usage of ``re.findall()`` and ``re.finditer()``:

.. code-block:: python

    import re


    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    DATA = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'

    re.findall(PATTERN, DATA)
    # ['MYPROJ-1337', 'MYPROJ-997']

Finding All Adverbs:

.. code-block:: python

    import re


    TEXT = 'He was carefully disguised but captured quickly by police.'
    ADVERBS = r'\w+ly'

    re.findall(ADVERBS, TEXT)
    # ['carefully', 'quickly']


Assignments
-----------
.. literalinclude:: assignments/regexp_find_a.py
    :caption: :download:`Solution <assignments/regexp_find_a.py>`
    :end-before: # Solution
