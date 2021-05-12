Regexp Syntax
=============


Rationale
---------
* Regular Expressions are also known as ``regexp``, ``regex`` or ``re``
* Identifiers - what to find
* Qualifiers - range to find
* Quantifiers - how many occurrences of preceding qualifier or identifier

* Recall information about escape characters (``\n`` - newline)
* Recall information about raw strings ``r'...'``

    * ``'hello\nworld'`` - text ``hello`` and then ``world`` in a new line
    * ``'hello\\nworld'`` - text ``hello``, then ``\n`` and ``world``
    * ``r'hello\nworld'`` - text ``hello``, then ``\n`` and ``world``


Identifiers
-----------
Identifiers specifies what to find.
They are also called Character Classes.

Numeric:
    * ``\d`` - digit
    * ``\D`` - anything but digit

String:

    * ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
    * ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)

Whitespaces:

    * ``\s`` - whitespace (space, tab, newline, non-breaking space)
    * ``\S`` - anything but whitespace
    * ``\t`` - tab
    * ``\n`` - newline
    * ``\v`` - vertical space
    * ``\f`` - form feed

Anchors:

    * ``\b`` - word boundary
    * ``\B`` - anything but word boundary

Examples:

    * ``\babc\b`` - performs a "whole words only" search
    * ``\Babc\B`` - pattern is fully surrounded by word characters


Look Ahead and Look Behind
--------------------------
Syntax:

    * ``(?=)`` - Lookahead
    * ``(?<=)`` - Lookbehind
    * ``(?!foo)`` - Negative Lookahead
    * ``(?<!foo)`` - Negative Lookbehind
    * ``\K`` - Stop Look Behind

Example:

    * ``(?=foo)`` - asserts that what immediately follows the current position in the string is ``foo``
    * ``(?<=foo)`` - asserts that what immediately precedes the current position in the string is ``foo``
    * ``(?!foo)`` - Asserts that what immediately follows the current position in the string is not foo
    * ``(?<!foo)`` - Asserts that what immediately precedes the current position in the string is not foo
    * ``^\s+sh '\K.+(?=')`` - if line starts with ``sh`` at any indentation, then take the content of whats inside of apostrophes
    * ``d(?=r)`` - matches a ``d`` only if is followed by ``r``, but ``r`` will not be part of the overall regex match
    * ``(?<=r)d`` - matches a ``d`` only if is preceded by an ``r``, but ``r`` will not be part of the overall regex match


Qualifier
---------
Qualifier specifies range to find.

Ranges:

    * ``[a-z]`` - any lowercase ASCII letter from `a` to `z`
    * ``[A-Z]`` - any uppercase ASCII letter from `A` to `Z`
    * ``[0-9]`` - any digit from `0` to `9`
    * ``[a-zA-Z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
    * ``[a-zA-Z0-9]`` - any ASCII letter from `a` to `z` or from `A` to `Z` or digit from `0` to `9`
    * ``[abc]`` - letter `a` or `b` or `c`

Alternatives:

    * ``a|b`` - letter `a` or `b` (also works with expressions)
    * ``[a-z]|[0-9]`` - any lowercase ASCII letter from `a` to `z` or digit from `0` to `9`

Special:
    * ``?`` - any character
    * ``.`` - any character except a newline

Anchors:

    * ``^`` - start of a string (changes meaning with ``re.MULTILINE``)
    * ``$`` - end of a string (changes meaning with ``re.MULTILINE``)
    * ``\A`` - start of a string (doesn't change meaning with ``re.MULTILINE``)
    * ``\Z`` - end of a string (doesn't change meaning with ``re.MULTILINE``)
    * ``\G`` - beginning of string or end of previous match

Examples:

    * ``[d-m]`` - any lowercase letter from `d`  to `m`
    * ``[3-7]`` - any digit from `3` to `7`
    * ``[d-mK-P3-8]`` - any lowercase letter from `d` to `m` or uppercase letter from `K` to `P` or digit from `3` to `8`
    * ``[xz2]`` - `x` or `z` or `2`
    * ``x|z|2`` - `x` or `z` or `2`
    * ``d|x`` - `d` or `x`
    * ``[d-k]|[ABC]|[3-8]`` - any lowercase letter from `d` to `k` or uppercase `A`,`B` or `C` or digit from `3` to `8`
    * ``[A-Z][a-z]`` - any capital letter from `A` to `Z` immediately followed by lowercase letter from `a` to `z`
    * ``abc.e`` - text `abc` then any character followed by letter `e`


Negation
--------
Negation logically inverts qualifier.

Syntax:

    * ``[^...]`` - anything but

Example:

    * ``[^abc]`` - anything but letter `a` or `b` or `c`


Quantifier
----------
Quantifier specifies how many occurrences of preceding qualifier or identifier.

Greedy (prefer longest matches):

    * ``{n}`` - exactly `n` repetitions, prefer longer
    * ``{,n}`` - maximum `n` repetitions, prefer longer
    * ``{n,}`` - minimum `n` repetitions, prefer longer
    * ``{n,m}`` - minimum `n` repetitions, maximum `m` times, prefer longer
    * ``*`` - minimum 0 repetitions, no maximum, prefer longer
    * ``+`` - minimum 1 repetitions, no maximum, prefer longer
    * ``?`` - minimum 0 repetitions, maximum 1 repetitions, prefer longer

Lazy - non-greedy (prefer shortest matches):

    * ``{,n}?`` - maximum `n` repetitions, prefer shorter
    * ``{n,}?`` - minimum `n` repetitions, prefer shorter
    * ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, prefer shorter
    * ``*?`` - minimum 0 repetitions, no maximum, prefer shorter
    * ``+?`` - minimum 1 repetitions, no maximum, prefer shorter
    * ``??`` - minimum 0 repetitions, maximum 1 repetition, prefer shorter

Examples:

    * ``[0-9]{2}`` - exactly two digits from `0` to `9`
    * ``\d{2}`` - exactly two digits from `0` to `9`
    * ``[A-Z]{2,10}`` - two to ten uppercase letters from `A` to `Z`
    * ``[A-Z]{2-10}-[0-9]{,5}`` - two to ten uppercase letters from `A` to `Z` followed by dash (`-`) and at least five numbers
    * ``[a-z]+`` - at least one lowercase letter from `a` to `z`, but try to fit the longest match
    * ``\d+`` - number
    * ``\d+\.\d+`` - float


Groups
------
* Catch expression results
* Can be named or positional

Syntax:

    * ``()`` - matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
    * ``(...)`` - unnamed group
    * ``(?P<mygroup>...)`` - define named group `mygroup`
    * ``(?:...)`` - disable capturing group

Backreference:

    * ``(?P=name)``- backreferencing by group name
    * ``\number`` - backreferencing by group number

Examples:

    * ``(\w+)`` - word character (including unicode chars, numbers an underscores)
    * ``\d+(\.\d+)?`` - float with optional decimals
    * ``\d+(,\d+)?`` - number with coma (``,``) as  thousands separator
    * ``(?P<word>\w+)`` - name group `word` with ``\w+`` with at least one word character (including unicode chars, numbers an underscores)
    * ``(?P<tag><.*?>).+(?P=tag)`` - matches text inside of a ``<tag>`` (opening and closing tag is the same)
    * ``(.+) \1`` - matches ``the the`` or ``55 55``
    * ``(.+) \1`` - not matches ``thethe`` (note the space after the group)

Usage:

    >>> import re
    >>>
    >>>
    >>> DATA = 'My name... José Jiménez'
    >>> result = re.search(r'(?P<firstname>[A-Z]\w+) (?P<lastname>[A-Z]\w+)', DATA)
    >>>
    >>> result.groupdict()
    {'firstname': 'José', 'lastname': 'Jiménez'}
    >>> result.groups()
    ('José', 'Jiménez')
    >>> result[0]
    'José Jiménez'
    >>> result[1]
    'José'
    >>> result[2]
    'Jiménez'


Flags
-----
* ``a``, ``re.ASCII`` - make ``\w``, ``\W``, ``\b``, ``\B``, ``\d``, ``\D``, ``\s`` and ``\S`` perform ASCII-only matching instead of full Unicode matching
* ``i``, ``re.IGNORECASE`` - Case-insensitive (has Unicode support i.e. Ą and ą)
* ``L``, ``re.LOCALE`` - make ``\w``, ``\W``, ``\b``, ``\B`` and case-insensitive matching dependent on the current locale
* ``m``, ``re.MULTILINE`` - match can start in one line, and end in another: ``^`` - start of line, ``$`` - end of line
* ``s``, ``re.DOTALL`` - ``.`` matches also newlines (default newlines are not matched by ``.``)
* ``u``, ``re.UNICODE`` - turns on UNICODE mode
* ``x``, ``re.VERBOSE`` - ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``

>>> import re
>>>
>>> a = re.compile(r"""\d +  # the integral part
...                    \.    # the decimal point
...                    \d *  # some fractional digits""", re.VERBOSE)
>>>
>>> b = re.compile(r"\d+\.\d*")

The final piece of regex syntax that Python's regular expression engine offers is a means of setting the flags. Usually the flags are set by passing them as additional parameters when calling the re.compile() function, but sometimes it's more convenient to set them as part of the regex itself. The syntax is simply (?flags) where flags is one or more of the following:
If the flags are set this way, they should be put at the start of the regex; they match nothing, so their effect on the regex is only to set the flags.
The letters used for the flags are the same as the ones used by Perl's regex engine, which is why s is used for re.DOTALL and x is used for re.VERBOSE.
Source: [#Summerfield2008]_


Extensions
----------
* In other programming languages

* ``[:allnum:]`` == ``[a-zA-Z0-9]``
* ``[:alpha:]`` == ``[a-zA-Z]``
* ``[a-Z]`` == ``[a-zA-Z]``
* ``[a-9]`` == ``[a-zA-Z0-9]``
* ``$1`` == ``\1``


String
------
.. code-block:: python

    import string

    string.punctuation
    # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    string.whitespace
    # ' \t\n\r\x0b\x0c'

    string.ascii_lowercase
    # 'abcdefghijklmnopqrstuvwxyz'

    string.ascii_uppercase
    # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    string.ascii_letters
    # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    string.digits
    # '0123456789'

    string.hexdigits
    # '0123456789abcdefABCDEF'

    string.octdigits
    # '01234567'

    string.printable
    # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'


Examples
--------
* ISO Date: ``r'^\d{4}-\d{2}-\d{2}$'``
* US Long Date: ``r'^\w+ \d{2}, \d{4}$'``
* US Short Date: ``r'^\d{2}/\d{2}/\d{2}$'``
* Email [#rfc3696]_: ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'``


Visualization
-------------
* https://regexper.com/
* https://regex101.com/

.. figure:: img/regexp-visualization.png

    Visualization for pattern ``r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'`` [#rfc3696]_


Further Reading
---------------
* Kinsley, Harrison "Sentdex". Python 3 Programming Tutorial - Regular Expressions / Regex with re. Year: 2014. Retrieved: 2021-04-11. URL: https://www.youtube.com/watch?v=sZyAn2TW7GY
* https://www.rexegg.com/regex-trick-conditional-replacement.html
* https://www.rexegg.com/regex-lookarounds.html
* https://www.rexegg.com/regex-anchors.html#z

References
----------
.. [#rfc3696] Klensin, J. RFC-3696: Application Techniques for Checking and Transformation of Names. The Internet Society Network Working Group. Year: 2004. Retrieved: 2021-05-12. https://datatracker.ietf.org/doc/html/rfc3696#section-3

.. [#Summerfield2008] Summerfield, Mark. Programming in Python 3. Regular Expressions. Chapter: 12. Pages: 445-465. Year: 2008. Retrieved: 2021-04-11. Publisher: Addison-Wesley Professional. ISBN: 978-0-13-712929-4. URL: https://www.informit.com/articles/article.aspx?p=1278986
