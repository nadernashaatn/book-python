Regexp Compile
==============


About
-----
* ``re.compile()``
* Used when pattern is reused (especially in the loop)


Examples
--------
Compiles at every loop iteration, and then matches:

.. code-block:: python

    import re


    PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'
    DATA = ['mark.watney@nasa.gov',
            'Mark.Watney@nasa.gov',
            '+mark.watney@nasa.gov',
            'mark.watney+@nasa.gov',
            'mark.watney+newsletter@nasa.gov',
            'mark.watney@.gov',
            '@nasa.gov',
            'mark.watney@nasa.g']

    for email in DATA:
        re.match(PATTERN, email)

Compiling before loop, hence matching only inside:

.. code-block:: python

    import re


    PATTERN = re.compile(r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$')
    DATA = ['mark.watney@nasa.gov',
            'Mark.Watney@nasa.gov',
            '+mark.watney@nasa.gov',
            'mark.watney+@nasa.gov',
            'mark.watney+newsletter@nasa.gov',
            'mark.watney@.gov',
            '@nasa.gov',
            'mark.watney@nasa.g']

    for email in DATA:
        PATTERN.match(email)
