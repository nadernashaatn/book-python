Regexp Match
============


About
-----
* ``re.match()``
* Checks exact match
* Checking if user input is correct (email, url, NIP, VAT ID, PESEL)


Examples
--------
Usage of ``re.match()``:

.. code-block:: python

    import re


    def is_valid_email(email: str) -> bool:
        PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'

        if re.match(PATTERN, email):
            return True
        else:
            return False


    is_valid_email('mark.watney@nasa.gov')     # True
    is_valid_email('mark.watney@nasa.g')       # False


Good Engineering Practices
--------------------------
* Doctests

.. code-block:: python

    import re

    email = r'^(?P<username>[a-z][a-z0-9._-]*)@(?P<domain>([a-z0-9-.]+)+)\.(?P<tld>[a-z]{2,10})$'

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

.. code-block:: python

    import re

    username = r'[a-z][a-z0-9._-]*'
    domain   = r'([a-z0-9-.]+)+'
    tld      = r'[a-z]{2,10}'
    email    = f'{username}@{domain}.{tld}'

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

.. code-block:: python

    import re

    username = r'^(?P<username>[a-z][a-z0-9._-]*)'
    domain   = r'(?P<domain>([a-z0-9-.]+)+)'
    tld      = r'(?P<tld>[a-z]{2,10})'
    email    = f'^{username}@{domain}.{tld}$'

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

.. code-block:: python

    import re

    username = r'[a-z][a-z0-9._-]*'
    domain   = r'([a-z0-9-.]+)+'
    tld      = r'[a-z]{2,10}'
    email    = f'^(?P<username>{username})@(?P<domain>{domain}).(?P<tld>{tld})$'

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

.. code-block:: python

    import re

    username = r'[a-z][a-z0-9._-]*'
    domain   = r'([a-z0-9-.]+)+'
    tld      = r'[a-z]{2,10}'
    email    = f'^(?P<username>{username})@(?P<domain>{domain}).(?P<tld>{tld})$'

    pattern = re.compile(email, flags=re.IGNORECASE)

    def is_valid(data):
        if re.match(pattern, data):
            return True
        else:
            return False

Doctests:

.. code-block:: python

    """
    >>> is_valid_email('mark.watney@nasa.gov')
    True
    >>> is_valid_email('Mark.Watney@nasa.gov')
    True
    >>> is_valid_email('+mark.watney@nasa.gov')
    False
    >>> is_valid_email('mark.watney+@nasa.gov')
    True
    >>> is_valid_email('mark.watney+newsletter@nasa.gov')
    True
    >>> is_valid_email('mark.watney@.gov')
    False
    >>> is_valid_email('@nasa.gov')
    False
    >>> is_valid_email('mark.watney@nasa.g')
    False
    """

    import re


    def is_valid_email(email: str) -> bool:
        """Function check email address against Regular Expression"""
        PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'

        if re.match(PATTERN, email):
            return True
        else:
            return False

.. code-block:: python

    """
    >>> is_valid('3ares@nasa.gov')
    False
    >>> is_valid('ares3@nasa.gov')
    True
    >>> is_valid('a3@nasa.gov')
    True
    >>> is_valid('3@nasa.gov')
    False
    >>> is_valid('m@nasa.gov')
    True
    >>> is_valid('m.watney@nasa.gov')
    True
    >>> is_valid('m_watney@nasa.gov')
    True
    >>> is_valid('m-watney@nasa.gov')
    True
    >>> is_valid('mark.watney@nasa.gov')
    True
    >>> is_valid('markwatney@nasa.gov')
    True
    >>> is_valid('jan.twardowski@polsa.gov.pl')
    True
    >>> is_valid('jan.twardowski@polsa24.gov.pl')
    True
    """

    import re

    username = r'^(?P<username>[a-z][a-z0-9._-]*)'
    domain   = r'(?P<domain>([a-z0-9-.]+)+)'
    tld      = r'(?P<tld>[a-z]{2,10})'
    email    = f'^{username}@{domain}.{tld}$'
    pattern = re.compile(email, flags=re.IGNORECASE)


    def is_valid(data):
        if pattern.match(data):
            return True
        else:
            return False


Assignments
-----------
.. literalinclude:: assignments/regexp_match_a.py
    :caption: :download:`Solution <assignments/regexp_match_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/regexp_match_b.py
    :caption: :download:`Solution <assignments/regexp_match_b.py>`
    :end-before: # Solution
