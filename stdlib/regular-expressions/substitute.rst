Regexp Substitute
=================


About
-----
* ``re.sub()``
* Replace matched substring with text


Examples
--------
Usage of ``re.sub()``:

.. code-block:: python

    import re


    PATTERN = r'\s[a-z]{3}\s'
    DATA = 'Baked Beans And Spam'

    re.sub(PATTERN, ' & ', DATA, flags=re.IGNORECASE)
    # 'Baked Beans & Spam'

