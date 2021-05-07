Regexp Search
=============


About
-----
* ``re.search()``
* Searches if pattern contains a string


Examples
--------
Usage of ``re.search()``:

.. code-block:: python

    import re


    def contains(pattern, text)
        if re.search(pattern, text):
            return True
        else:
            return False


    COMMIT_MESSAGE = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'
    JIRA_ISSUEKEY = r'[A-Z]{2,10}-[0-9]{1,6}'
    REDMINE_NUMBER = r'#[0-9]+'

    contains(JIRA_ISSUEKEY, COMMIT_MESSAGE)      # True
    contains(REDMINE_NUMBER, COMMIT_MESSAGE)     # False


Assignments
-----------
.. literalinclude:: assignments/regexp_search_a.py
    :caption: :download:`Solution <assignments/regexp_search_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/regexp_search_b.py
    :caption: :download:`Solution <assignments/regexp_search_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/regexp_search_c.py
    :caption: :download:`Solution <assignments/regexp_search_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/regexp_search_d.py
    :caption: :download:`Solution <assignments/regexp_search_d.py>`
    :end-before: # Solution
