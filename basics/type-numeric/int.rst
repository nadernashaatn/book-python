Numeric Int
===========


Definition
----------
Python 3 dynamically extends ``int`` when it's too big, hence there is no
maximal or minimal ``int`` value:

>>> data = 1337
>>> data = +1337
>>> data = -1337

You can use ``_`` for easier read especially with big numbers:

>>> million = 1000000
>>>
>>> print(million)
1000000

>>> million = 1_000_000
>>>
>>> print(million)
1000000


Type Casting
------------
Builtin function ``int()`` converts argument to ``int``:

>>> int(1)
1
>>> int(+1)
1
>>> int(-1)
-1

>>> int(1.337)
1
>>> int(+1.1337)
1
>>> int(-1.337)
-1

>>> int('1')
1
>>> int('+1')
1
>>> int('-1')
-1

Builtin function ``int()`` does not round numbers:

>>> int(1.001)
1
>>> int(1.999)
1

>>> int('1_000_000')
1000000

Builtin function ``int()`` fails when in argument there are parameters
other than a digit, ``+`` or ``-`` sign and ``_``

>>> int('1.337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '13.37'

>>> int('+1.337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '+13.37'

>>> int('-1.337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '-13.37'

>>> int('1,337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '13,37'

>>> int('+1,337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '+13,37'

>>> int('-1,337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '-13,37'


Binary
------
* Base 2
* Allowed: 0, 1
* Prefix: ``0b...``

>>> int('100', base=2)
4
>>> int('0b1000101', base=2)
69


Octal
-----
* Base 8
* Allowed: 0, 1, 2, 3, 4, 5, 6, 7
* Prefix: ``0o...``

>>> int('100', base=8)
64
>>> int('0o105', base=8)
69
>>> int('0o754', base=8)
492


Decimal
-------
* Base 10
* Allowed: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

>>> int('100', base=10)
100
>>> int('69', base=10)
69


Hexadecimal
-----------
* Base 16
* Allowed: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f, A, B, C, D, E, F
* Prefix: ``0x...``

>>> int('100', base=16)
256
>>> int('0x45', base=16)
69
>>> int('0x69', base=16)
105
>>> int('0x3C', base=16)
60


Type Checking
-------------
* ``type()`` - Returns type of an argument

>>> type(1)
<class 'int'>
>>> type(+1)
<class 'int'>
>>> type(-1)
<class 'int'>

>>> type(0)
<class 'int'>
>>> type(+0)
<class 'int'>
>>> type(-0)
<class 'int'>


Assignments
-----------
.. literalinclude:: assignments/type_int_a.py
    :caption: :download:`Solution <assignments/type_int_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_b.py
    :caption: :download:`Solution <assignments/type_int_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_c.py
    :caption: :download:`Solution <assignments/type_int_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_d.py
    :caption: :download:`Solution <assignments/type_int_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_e.py
    :caption: :download:`Solution <assignments/type_int_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_f.py
    :caption: :download:`Solution <assignments/type_int_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_g.py
    :caption: :download:`Solution <assignments/type_int_g.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_h.py
    :caption: :download:`Solution <assignments/type_int_h.py>`
    :end-before: # Solution
