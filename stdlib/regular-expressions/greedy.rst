Regexp Non-Greedy
=================


About
-----
* Adding ``?`` after the qualifier makes it non-greedy
* Non-greedy - as few as possible
* Greedy - as many as possible

.. csv-table:: Regular Expression Greedy and Non-Greedy Qualifiers
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``?``", "zero or one (greedy)"
    "``*``", "zero or more (greedy)"
    "``+``", "one or more (greedy)"
    "``??``", "zero or one (non greedy)"
    "``*?``", "zero or more (non greedy)"
    "``+?``", "one or more (non greedy)"


Examples
--------
Usage of greedy and non-greedy search in ``re.findall()``:

.. code-block:: python

    import re

    TEXT = '<strong>Ehlo World</strong>'

    re.findall(r'<.*>', TEXT)         # ['<strong>Ehlo World</strong>']
    re.findall(r'<.*?>', TEXT)        # ['<strong>', '</strong>']

Usage of greedy and non-greedy search with groups:

.. code-block:: python

    re.findall(r'<(.*)>', TEXT)       # ['strong>Ehlo World</strong']
    re.findall(r'<(.*?)>', TEXT)      # ['strong', '/strong']
    re.findall(r'</?(.*?)>', TEXT)    # ['strong', 'strong']


Assignments
-----------
.. literalinclude:: assignments/regexp_greedy_a.py
    :caption: :download:`Solution <assignments/regexp_greedy_a.py>`
    :end-before: # Solution
