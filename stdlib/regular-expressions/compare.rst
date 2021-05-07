Regexp Compare
==============


Examples
--------
Comparison between ``re.match()``, ``re.search()`` and ``re.findall()``:

.. code-block:: python

    import re


    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    DATA = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'

    re.findall(PATTERN, DATA)           # ['MYPROJ-1337', 'MYPROJ-997']
    re.search(PATTERN, DATA).group()    # 'MYPROJ-1337'
    re.match(PATTERN, DATA)             # None
