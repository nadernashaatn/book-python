Conditional Operator
====================


Equals
------
* ``==`` - ``eq`` (equals)

Comparing ``str``:

>>> 'Monty Python' == 'Python'
False
>>> 'Python' == 'Python'
True
>>> 'python' == 'Python'
False

Comparing ``tuple``:

>>> (1, 2, 3) == (1, 2)
False
>>> (1, 2) == (1, 2)
True
>>> (1, 2) == (2, 1)
False

Comparing ``list``:

>>> [1, 2, 3] == [1, 2]
False
>>> [1, 2] == [1, 2]
True
>>> [1, 2] == [2, 1]
False

Comparing ``set``:

>>> {1, 2, 3} == {1, 2}
False
>>> {1, 2} == {1, 2}
True
>>> {1, 2} == {2, 1}
True

>>> (1,2) == [1,2]
False
>>> (1,2) == {1,2}
False
>>> 1,2 == {1,2}
(1, False)


Not-Equals
----------
* ``!=`` - ``ne`` (not-equals)

Comparing ``str``:

>>> 'Monty Python' != 'Python'
True
>>> 'Python' != 'Python'
False
>>> 'python' != 'Python'
True

Comparing ``tuple``:

>>> (1, 2, 3) != (1, 2)
True

Comparing ``list``:

>>> [1, 2, 3] != [1, 2]
True

Comparing ``set``:

>>> {1, 2, 3} != {1, 2}
True


Greater Than
------------
* ``>`` - ``gt`` (greater than)
* Set uses ``>`` for ``set.issuperset()``

>>> 'a' > 'b'
False
>>> 'b' > 'a'
True

>>> 'abc' > 'ab'
True
>>> 'abc' > 'abc'
False
>>> 'abc' > 'abcd'
False

>>> 'def' > 'abc'
True
>>> 'abc' > 'xy'
False
>>> 'abc' > 'xyz'
False

>>> (3, 9) > (3, 8)
True
>>> (3, 8, 3) > (3, 7, 6)
True
>>> (3, 8) > (3, 9)
False

>>> (2, 7) > (3, 6)
False
>>> (3, 6) > (2, 7)
True

>>> [3, 9] > [3, 8]
True
>>> [3, 8, 3] > [3, 7, 6]
True
>>> [3, 8] > [3, 9]
False

>>> [2, 7] > [3, 6]
False
>>> [3, 6] > [2, 7]
True


Problems
--------
>>> 1, 2 == (1, 2)
(1, False)
>>> 1
1
>>> 2 == (1, 2)
False
>>> 1,     2==(1,2)
(1, False)

>>> (1, 2) == 1, 2
(False, 2)


Examples
--------
>>> import sys
>>>
>>> print(sys.version_info)
sys.version_info(major=3, minor=9, micro=5, releaselevel='final', serial=0)
>>>
>>> sys.version_info > (3, 8)
True
>>> sys.version_info > (3, 9)
True
>>> sys.version_info > (3, 10)
False
>>>
>>> sys.version_info > (3, 9, 0)
True
>>> sys.version_info > (3, 9, 3)
True
>>> sys.version_info >= (3, 9, 4)
True
>>> sys.version_info > (3, 9, 15)
False

>>> '3.8.0' > '3.9.0'
False
>>> '3.9.0' > '3.10.0'
True
>>> '3.09.0' > '3.10.0'
False

>>> myversion = '3.9.0'
>>> required = '3.7.0'
>>>
>>> myversion >= required
True

>>> myversion = '3.9.0'.split('.')
>>> required = '3.7.0'.split('.')
>>>
>>> myversion >= required
True


Operator Precedence
-------------------
.. csv-table:: Operator precedence
    :header-rows: 1
    :widths: 25, 75

    "Operator", "Description"
    "``lambda``", "Lambda expression"
    "``if``, ``elif``, ``else``", "Conditional expression"
    "``and``", "Boolean AND"
    "``or``", "Boolean OR"
    "``not x``", "Boolean NOT"
    "``in``, ``not in``, ``is``, ``is not``,

    ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``", "Comparisons, including membership tests and identity tests"
    "``|``", "Bitwise OR"
    "``^``", "Bitwise XOR"
    "``&``", "Bitwise AND"
    "``<<``, ``>>``", "Shifts"
    "``**``", "Exponentiation"
    "``*``, ``@``, ``/``, ``//``, ``%``", "Multiplication, matrix multiplication, division, floor division, remainder"
    "``+``, ``-``", "Addition and subtraction"
    "``+x``, ``-x``, ``~x``", "Positive, negative, bitwise NOT"
    "``await``", "Await expression"
    "``x[index]``, ``x[index:index]``,

    ``x(arguments...)``, ``x.attribute``", "Subscription, slicing, call, attribute reference"
    "``(expressions...)``, ``[expressions...]``,

    ``{key: value...}``, ``{expressions...}``", "Binding or tuple display, list display, dictionary display, set display"


Assignments
-----------
.. literalinclude:: assignments/conditional_operator_a.py
    :caption: :download:`Solution <assignments/conditional_operator_a.py>`
    :end-before: # Solution
