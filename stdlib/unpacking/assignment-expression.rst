Assignment Expression
=====================


Rationale
---------
* Since Python 3.8: :pep:`572` -- Assignment Expressions
* A.K.A. "the walrus operator"
* A.K.A. "Named Expressions"

During discussion of this PEP, the operator became informally known as "the walrus operator". The construct's formal name is "Assignment Expressions" (as per the PEP title), but they may also be referred to as "Named Expressions" (e.g. the CPython reference implementation uses that name internally). [#pep572]_


Syntax
------
.. code-block:: python

    (x := <VALUE>)


It's not substitution for equals:

>>> x = 1
>>>
>>> print(x)
1

>>> x := 1
Traceback (most recent call last):
SyntaxError: invalid syntax

>>> (x := 1)
1
>>>
>>> print(x)
1

>>> x = 1, 2
>>>
>>> print(x)
(1, 2)


>>> (x := 1, 2)
(1, 2)
>>>
>>> print(x)
1

>>> result = (x := 1, 2)
>>>
>>> print(result)
(1, 2)

>>> x = 0
>>> x += 1
>>>
>>> print(x)
1

>>> x = 0
>>> x +:= 1
Traceback (most recent call last):
SyntaxError: invalid syntax

>>> data = {}
>>> data['commander'] = 'Mark Watney'
>>>
>>> data = {}
>>> data['commander'] := 'Mark Watney'
Traceback (most recent call last):
SyntaxError: cannot use assignment expressions with subscript

.. figure:: img/unpacking-assignmentexpr-bdfl.png

    Guido van Rossum stepped down after accepting :pep:`572` -- Assignment Expressions


Example
-------

Reusing Results:

>>> def f(x):
...     return 1
>>>
>>>
>>> result = [f(x), f(x)+1, f(x)+2]
>>>
>>> result = [res := f(x), res+1, res+2]

Processing Steams in Chunks:

>>> # doctest: +SKIP
...
... file = open('_temporary.txt')
... chunk = file.read(8192)
...
... while chunk:
...     print(chunk)
...     chunk = file.read(8192)

>>> # doctest: +SKIP
...
... file = open('_temporary.txt')
...
... while chunk := file.read(8192):
...     print(chunk)


Checking Match
--------------
>>> import re
>>>
>>>
>>> DATA = 'mark.watney@nasa.gov'
>>> result = re.search(r'@nasa.gov', DATA)
>>>
>>> if result:
...     print(result)
<re.Match object; span=(11, 20), match='@nasa.gov'>

>>> import re
>>>
>>>
>>> DATA = 'mark.watney@nasa.gov'
>>>
>>> if (result := re.search(r'@nasa.gov', DATA)):
...     print(result)
<re.Match object; span=(11, 20), match='@nasa.gov'>


Patterns
--------
>>> import re
>>>
>>>
>>> data = 'mark.watney@nasa.gov'
>>> pattern = r'([a-z]+)\.([a-z]+)@nasa.gov'
>>>
>>> match = re.match(pattern, data)
>>> result = match.groups() if match else None
>>>
>>> print(result)
('mark', 'watney')

>>> import re
>>>
>>>
>>> data = 'mark.watney@nasa.gov'
>>> pattern = r'([a-z]+)\.([a-z]+)@nasa.gov'
>>>
>>> result = re.match(pattern, data).groups() if re.match(pattern, data) else None
>>>
>>> print(result)
('mark', 'watney')

>>> import re
>>>
>>>
>>> data = 'mark.watney@nasa.gov'
>>> pattern = r'([a-z]+)\.([a-z]+)@nasa.gov'
>>>
>>> result = x.groups() if (x := re.match(pattern, data)) else None
>>>
>>> print(result)
('mark', 'watney')


Comprehensions
--------------
>>> result = [x for x in range(0,10)]
>>> result = [x for x in range(0,10) if x%2 == 0]

>>> DATA = ['Jan Twardowski',
...         'Melissa Lewis',
...         'Mark Watney']
>>>
>>>
>>> result = [{'firstname': fullname.split()[0],
...            'lastname': fullname.split()[1]}
...           for fullname in DATA]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'Twardowski'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Mark', 'lastname': 'Watney'}]
>>>
>>> result = [{'firstname': name[0], 'lastname': name[1]}
...           for fullname in DATA
...           if (name := fullname.split())]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'Twardowski'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Mark', 'lastname': 'Watney'}]

Syntax:

.. code-block:: python

    result = [<RETURN>
              for <VARIABLE1> in <ITERABLE>
              if (<VARIABLE2> := <EXPR>)]

.. code-block:: python

    result = [<RETURN>
              for <VARIABLE1> in <ITERABLE>
              if (<VARIABLE2> := <EXPR>)
              and (<VARIABLE3> := <EXPR>)]

.. code-block:: python

    result = [<RETURN>
              for <VARIABLE1> in <ITERABLE>
              if (<VARIABLE2> := <EXPR>)
              and (<VARIABLE3> := <EXPR>)
              or (<VARIABLE4> := <EXPR>)]

>>> DATA = ['5.8,2.7,5.1,1.9,virginica',
...         '5.1,3.5,1.4,0.2,setosa',
...         '5.7,2.8,4.1,1.3,versicolor']
>>>
>>> result = []
>>>
>>> for line in DATA:
...     line = line.split(',')
...     result.append(line[0:4])
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[['5.8', '2.7', '5.1', '1.9'],
 ['5.1', '3.5', '1.4', '0.2'],
 ['5.7', '2.8', '4.1', '1.3']]
>>>
>>> result = [line.split(',')[0:4] for line in DATA]
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[['5.8', '2.7', '5.1', '1.9'],
 ['5.1', '3.5', '1.4', '0.2'],
 ['5.7', '2.8', '4.1', '1.3']]

>>> DATA = ['5.8,2.7,5.1,1.9,virginica',
...         '5.1,3.5,1.4,0.2,setosa',
...         '5.7,2.8,4.1,1.3,versicolor']
>>>
>>> result = []
>>>
>>> for line in DATA:
...     X = [float(x) for x in line.split(',')[0:4]]
...     result.append(X)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[[5.8, 2.7, 5.1, 1.9],
 [5.1, 3.5, 1.4, 0.2],
 [5.7, 2.8, 4.1, 1.3]]
>>>
>>> result = [[float(x) for x in line.split(',')[0:4]]
...           for line in DATA]
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[[5.8, 2.7, 5.1, 1.9],
 [5.1, 3.5, 1.4, 0.2],
 [5.7, 2.8, 4.1, 1.3]]
>>>
>>> result = [[float(x) for x in X]
...           for line in DATA
...           if (X := line.split(',')[0:4])]
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[[5.8, 2.7, 5.1, 1.9],
 [5.1, 3.5, 1.4, 0.2],
 [5.7, 2.8, 4.1, 1.3]]

>>> DATA = ['5.8,2.7,5.1,1.9,virginica',
...         '5.1,3.5,1.4,0.2,setosa',
...         '5.7,2.8,4.1,1.3,versicolor']
...
>>> result = [[float(x) for x in X] + [y]
...           for line in DATA
...           if (row := line.split(','))
...           and (X := row[0:4])
...           and (y := row[4])]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[[5.8, 2.7, 5.1, 1.9, 'virginica'],
 [5.1, 3.5, 1.4, 0.2, 'setosa'],
 [5.7, 2.8, 4.1, 1.3, 'versicolor']]


Use Case
--------
>>> DATA = [{'is_astronaut': True,  'name': 'JaN TwarDOwski'},
...         {'is_astronaut': True,  'name': 'Mark Jim WaTNey'},
...         {'is_astronaut': False, 'name': 'José Maria Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>>
>>> result = [{'firstname': person['name'].title().split()[0],
...            'lastname': person['name'].title().split()[-1]}
...           for person in DATA
...           if person['is_astronaut']]
>>>
>>> result = [{'firstname': name[0],
...            'lastname': name[-1]}
...           for person in DATA
...           if person['is_astronaut']
...           and (name := person['name'].title().split())]
>>>
>>> result = [{'firstname': fname,
...            'lastname': lname}
...           for person in DATA
...           if person['is_astronaut']
...           and (name := person['name'].title().split())
...           and (fname := name[0])
...           and (lname := name[-1])]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'Twardowski'},
 {'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'}]

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
>>>
>>>
>>> class Versicolor(Iris):
...     pass
>>>
>>> class Virginica(Iris):
...     pass
>>>
>>> class Setosa(Iris):
...     pass
>>>
>>>
>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> result = [cls(*features)
...           for *features, species in DATA[1:]
...           if (clsname := species.capitalize())
...           and (cls := globals()[clsname])]
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2),
 Versicolor(sepal_length=7.0, sepal_width=3.2, petal_length=4.7, petal_width=1.4)]


References
----------
.. [#pep572] Angelico, C. and Peters T. and van Rossum, G. PEP 572 -- Assignment Expressions. Python Software Foundation. Year: 2018. Retrieved: 2020-12-04. Url: https://www.python.org/dev/peps/pep-0572/#abstract


Assignments
-----------
.. literalinclude:: assignments/unpacking_assignmentexpr_a.py
    :caption: :download:`Solution <assignments/unpacking_assignmentexpr_a.py>`
    :end-before: # Solution
