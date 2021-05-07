OOP Dataclass
=============


Rationale
---------
* Used for easier class definition
* Since Python 3.7: :pep:`557` -- Data Classes
* Backported to Python 3.6 via ``python3 -m pip install dataclasses``


Syntax
------
* This are not static fields!
* Dataclasses require Type Annotations

>>> class Point:
...     def __init__(self, x, y, z=0):
...         self.x = x
...         self.y = y
...         self.z = z

>>> from dataclasses import dataclass
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
...     z: int = 0


Example 1
---------
``class``:

>>> class Point:
...     def __init__(self, x, y, z=0):
...         self.x = x
...         self.y = y
...         self.z = z
>>>
>>>
>>> p0 = Point()
Traceback (most recent call last):
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>>
>>> p1 = Point(10)
Traceback (most recent call last):
TypeError: __init__() missing 1 required positional argument: 'y'
>>>
>>> p2 = Point(10, 20)
>>> p3 = Point(10, 20, 30)
>>> p4 = Point(10, 20, z=30)
>>> p5 = Point(10, 20, z=30)
>>> p6 = Point(x=10, y=20, z=30)

``dataclass``:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
...     z: int = 0
>>>
>>>
>>> p0 = Point()
Traceback (most recent call last):
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>>
>>> p1 = Point(10)
Traceback (most recent call last):
TypeError: __init__() missing 1 required positional argument: 'y'
>>>
>>> p2 = Point(10, 20)
>>> p3 = Point(10, 20, 30)
>>> p4 = Point(10, 20, z=30)
>>> p5 = Point(10, 20, z=30)
>>> p6 = Point(x=10, y=20, z=30)


Example 2
---------
``class``:

>>> class Astronaut:
...     firstname: str
...     lastname: str
...
...     def __init__(self, firstname: str, lastname: str, agency: str = 'POLSA'):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.agency = agency
>>>
>>>
>>> twardowski = Astronaut('Jan', 'Twardowski')
>>>
>>> print(twardowski.firstname)
Jan
>>> print(twardowski.lastname)
Twardowski
>>> print(twardowski.agency)
POLSA

``dataclass``:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     agency: str = 'POLSA'
>>>
>>>
>>> twardowski = Astronaut('Jan', 'Twardowski')
>>>
>>> print(twardowski.firstname)
Jan
>>> print(twardowski.lastname)
Twardowski
>>> print(twardowski.agency)
POLSA


Example 3
---------
>>> from dataclasses import dataclass
>>> from datetime import date
>>> from typing import Final, Optional
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     date_of_birth: date = date.today()
...     height: Optional[int] = None
...     friends: Optional[list['Astronaut']] = None
...     AGE_MIN: Final[int] = 27
...     AGE_MAX: Final[int] = 42
>>>
>>>
>>> Astronaut('Mark', 'Watney', date(1994, 10, 12))
Astronaut(firstname='Mark', lastname='Watney', date_of_birth=datetime.date(1994, 10, 12), height=None, friends=None, AGE_MIN=27, AGE_MAX=42)
>>>
>>> astro = Astronaut('Mark', 'Watney', date(1994, 10, 12), friends=[
...         Astronaut('Melissa', 'Lewis', date(1995, 7, 15)),
...         Astronaut('Rick', 'Martinez', date(1996, 1, 21)),
...         Astronaut('Beth', 'Johansen', date(2006, 5, 9)),
...         Astronaut('Chris', 'Beck', date(1999, 8, 2)),
...         Astronaut('Alex', 'Vogel', date(1994, 11, 15))])
>>>
>>> astro  # doctest: +NORMALIZE_WHITESPACE
Astronaut(firstname='Mark', lastname='Watney', date_of_birth=datetime.date(1994, 10, 12), height=None, friends=[Astronaut(firstname='Melissa', lastname='Lewis', date_of_birth=datetime.date(1995, 7, 15), height=None, friends=None, AGE_MIN=27, AGE_MAX=42), Astronaut(firstname='Rick', lastname='Martinez', date_of_birth=datetime.date(1996, 1, 21), height=None, friends=None, AGE_MIN=27, AGE_MAX=42), Astronaut(firstname='Beth', lastname='Johansen', date_of_birth=datetime.date(2006, 5, 9), height=None, friends=None, AGE_MIN=27, AGE_MAX=42), Astronaut(firstname='Chris', lastname='Beck', date_of_birth=datetime.date(1999, 8, 2), height=None, friends=None, AGE_MIN=27, AGE_MAX=42), Astronaut(firstname='Alex', lastname='Vogel', date_of_birth=datetime.date(1994, 11, 15), height=None, friends=None, AGE_MIN=27, AGE_MAX=42)], AGE_MIN=27, AGE_MAX=42)


Example 4
---------
``class``:

>>> from datetime import datetime
>>>
>>>
>>> class StarWarsMovie:
...     title: str
...     episode_id: int
...     opening_crawl: str
...     director: str
...     producer: str
...     release_date: datetime
...     characters: tuple[str]
...     planets: tuple[str]
...     starships: tuple[str]
...     vehicles: tuple[str]
...     species: tuple[str]
...     created: datetime
...     edited: datetime
...     url: str
...
...     def __init__(self, title: str, episode_id: int, opening_crawl: str,
...                  director: str, producer: str, release_date: datetime,
...                  characters: tuple[str], planets: tuple[str], starships: tuple[str],
...                  vehicles: tuple[str], species: tuple[str], created: datetime,
...                  edited: datetime, url: str):
...
...         self.title = title
...         self.episode_id = episode_id
...         self.opening_crawl= opening_crawl
...         self.director = director
...         self.producer = producer
...         self.release_date = release_date
...         self.characters = characters
...         self.planets = planets
...         self.starships = starships
...         self.vehicles = vehicles
...         self.species = species
...         self.created = created
...         self.edited = edited
...         self.url = url

``dataclass``:

>>> from dataclasses import dataclass
>>> from datetime import datetime
>>>
>>>
>>> @dataclass
... class StarWarsMovie:
...     title: str
...     episode_id: int
...     opening_crawl: str
...     director: str
...     producer: str
...     release_date: datetime
...     characters: tuple[str]
...     planets: tuple[str]
...     starships: tuple[str]
...     vehicles: tuple[str]
...     species: tuple[str]
...     created: datetime
...     edited: datetime
...     url: str


``__init__`` vs. ``__post_init__``
----------------------------------
``class``:

>>> class Kelvin:
...     def __init__(self, value):
...         if value < 0.0:
...             raise ValueError('Temperature must be greater than 0')
...         else:
...             self.value = value
>>>
>>>
>>> t = Kelvin(-1)
Traceback (most recent call last):
ValueError: Temperature must be greater than 0

``dataclass``:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Kelvin:
...     value: float = 0.0
...
...     def __post_init__(self):
...         if self.value < 0.0:
...             raise ValueError('Temperature must be greater than 0')
>>>
>>>
>>> t = Kelvin(-1)
Traceback (most recent call last):
ValueError: Temperature must be greater than 0

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     publicname: str = field(init=False)
...
...     def __post_init__(self):
...         self.publicname = f'{self.firstname} {self.lastname[0]}.'


Field Object
------------
* ``name`` - The name of the field.
* ``type`` - The type of the field.
* ``default`` - Default value
* ``default_factory`` - Field factory
* ``init``
* ``repr``
* ``hash``
* ``compare``
* ``metadata`` - This can be a mapping or ``None``. ``None`` is treated as an empty ``dict``. It is not used at all by Data Classes, and is provided as a third-party extension mechanism.

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     publicname: int = field(repr=False)
...     agency: int = field(repr=False, default='NASA')

>>> from __future__ import annotations
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass(frozen=True)
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     age: float
...     height: float = field(metadata={'unit': 'cm'})
...     weight: float = field(metadata={'unit': 'km'})
...     mission: list[Mission]
...     agency: str = field(default='NASA', metadata={'choices': ['NASA', 'ESA']})
...     friends: list[Astronaut] = field(default_factory=list)
...     country: str = 'USA'
...
...     def __post_init__(self):
...         if self.age > 65:
...             raise ValueError('Too old for an astronaut')
...
...     def say_hello(self):
...         print(f'Howdy, I am {self.firstname} {self.lastname}')
...
...
>>> astro = Astronaut('Mark', 'Watney',
...                   age=44,
...                   height=170,
...                   weight=75,
...                   mission=[Mission(2035, 'Ares 3')],
...                   friends=[],
...                   agency='NASA')
>>>
>>> astro
Astronaut(firstname='Mark', lastname='Watney', age=44, height=170, weight=75, mission=[Mission(year=2035, name='Ares 3')], agency='NASA', friends=[], country='USA')
>>>
>>> astro.__dataclass_fields__['agency'].metadata['choices']
['NASA', 'ESA']
>>> astro.__dataclass_fields__['height'].metadata['unit']
'cm'
>>> Astronaut.__dataclass_fields__['agency'].metadata['choices']
['NASA', 'ESA']


Mutable attributes
------------------
* problem with ``dict``, ``list``, ``set``
* You should not set mutable objects as a default function argument
* ``field()`` creates new empty ``list`` for each object
* It does not reuse pointer
* Discussion: https://github.com/ericvsmith/dataclasses/issues/3

.. warning:: Note, You should not set mutable objects as a default function argument. More information in `Argument Mutability`

    >>> class Astronaut:
    ...     def __init__(self, name, missions=[]):
    ...         self.name = name
    ...         self.missions = missions
    >>>
    >>>
    >>> watney = Astronaut('Mark Watney')
    >>> twardowski = Astronaut('Jan Twardowski')
    >>>
    >>> watney.missions.append('Ares 1')
    >>> watney.missions.append('Ares 2')
    >>> watney.missions.append('Ares 3')
    >>> watney.missions.append('Ares 4')
    >>> watney.missions.append('Ares 5')
    >>>
    >>> print('Watney:', watney.missions)
    Watney: ['Ares 1', 'Ares 2', 'Ares 3', 'Ares 4', 'Ares 5']
    >>>
    >>> print('Twardowski:', twardowski.missions)
    Twardowski: ['Ares 1', 'Ares 2', 'Ares 3', 'Ares 4', 'Ares 5']

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: dict[int,str] = field(default_factory=dict)
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')

>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Mission:
...     year: int
...     name: str
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...     missions: list[Mission] = field(default_factory=list)
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')


Dataclass parameters
--------------------
.. todo:: Table is more readable

        * ``init`` - Generate ``__init__()`` method (default ``True``)
        * ``repr`` - Generate ``__repr__()`` method (default ``True``)
        * ``eq`` - Generate ``__eq__()`` and ``__ne__()`` methods (default ``True``)
        * ``order`` - Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods (default ``False``)
        * ``unsafe_hash`` - if ``False``: the ``__hash__()`` method is generated according to how eq and frozen are set (default ``False``)
        * ``frozen`` - if ``True``: assigning to fields will generate an exception (default ``False``)

.. csv-table:: Dataclass options
    :header: "Option", "Default", "Description (if True)"
    :widths: 10, 10, 80

    "``init``", "``True``", "Generate ``__init__()`` method"
    "``repr``", "``True``", "Generate ``__repr__()`` method"
    "``eq``", "``True``", "Generate ``__eq__()`` and ``__ne__()`` methods"
    "``order``", "``False``", "Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods"
    "``unsafe_hash``", "``False``", "if False: the ``__hash__()`` method is generated according to how eq and frozen are set"
    "``frozen``", "``False``", "if ``True``: assigning to fields will generate an exception"


Init
----
* Generate ``__init__()`` method

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(init=False)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
Traceback (most recent call last):
TypeError: Point() takes no arguments


Repr
----
* ``repr=True`` by default
* Generate ``__repr__()`` for pretty printing

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(repr=True)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>>
>>> print(p)
Point(x=10, y=20)

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(repr=False)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>>
>>> print(p)  # doctest: +ELLIPSIS
<Point object at 0x...>


Frozen
------
* ``frozen=False`` by default
* Prevents object from modifications

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(frozen=True)
... class Point:
...     x: int
...     y: int
>>>
>>>
>>> p = Point(10, 20)
>>>
>>> p.x = 30
Traceback (most recent call last):
dataclasses.FrozenInstanceError: cannot assign to field 'x'


Eq
--
* ``eq=True`` by default
* when ``eq=False`` compare objects by ``id()`` not values
* when ``eq=True`` compare objects by value not ``id()``

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(eq=True)
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro1 = Astronaut('Mark', 'Watney')
>>> astro2 = Astronaut('Mark', 'Watney')
>>> astro3 = Astronaut('Jan', 'Twardowski')
>>>
>>> astro1 == astro1
True
>>> astro1 == astro2
True
>>> astro1 == astro3
False
>>>
>>> astro1 != astro1
False
>>> astro1 != astro2
False
>>> astro1 != astro3
True

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(eq=False)
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> astro1 = Astronaut('Mark', 'Watney')
>>> astro2 = Astronaut('Mark', 'Watney')
>>> astro3 = Astronaut('Jan', 'Twardowski')
>>>
>>> astro1 == astro1
True
>>> astro1 == astro2
False
>>> astro1 == astro3
False
>>>
>>> astro1 != astro1
False
>>> astro1 != astro2
True
>>> astro1 != astro3
True


Other flags
-----------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>> astro1 = Astronaut('Mark', 'Watney')
>>> astro2 = Astronaut('Mark', 'Watney')
>>> astro3 = Astronaut('Jan', 'Twardowski')


InitVar
-------
* Init-only fields are added as parameters to the generated ``__init__`` method, and are passed to the optional ``__post_init__`` method
* They are not otherwise used by Data Classes

>>> # doctest: +SKIP
... from dataclasses import dataclass, InitVar
...
...
... @dataclass
... class Astronaut:
...     fullname: InitVar[str] = None
...     _firstname: str = None
...     _lastname: str = None
...
...     def __post_init__(self, fullname: str):
...         fullname = fullname.split()
...         self._firstname = fullname[0]
...         self._lastname = fullname[1]
...
...
... astro = Astronaut('Mark Watney')
...
... print(astro._firstname)
Mark
... print(astro._lastname)
Watney


Inheritance
-----------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Person:
...     name: str
...     job: str = None
>>>
>>>
>>> @dataclass
... class Astronaut(Person):
...     job: str = 'Astronaut'
...     agency: str = 'NASA'
>>>
>>>

Will generate ``def __init__(self, name: str, job: str = 'Astronaut', agency: str = 'NASA')``


Helper functions
----------------
* ``fields(class_or_instance)`` - Returns a tuple of Field objects that define the fields for this Data Class. Accepts either a Data Class, or an instance of a Data Class. Raises ValueError if not passed a Data Class or instance of one. Does not return pseudo-fields which are ClassVar or InitVar.
* ``asdict(instance, *, dict_factory=dict)`` - Converts the Data Class instance to a dict (by using the factory function dict_factory)
* ``astuple(*, tuple_factory=tuple)`` - Converts the Data Class instance to a tuple (by using the factory function tuple_factory). Each Data Class is converted to a tuple of its field values. Data Classes, dicts, lists, and tuples are recursed into.
* ``make_dataclass(cls_name, fields, *, bases=(), namespace=None)`` - Creates a new Data Class with name cls_name, fields as defined in fields, base classes as given in bases, and initialized with a namespace as given in namespace.
* ``replace(instance, **changes)`` - Creates a new object of the same type of instance, replacing fields with values from changes. If instance is not a Data Class, raises TypeError. If values in changes do not specify fields, raises TypeError.
* ``is_dataclass(class_or_instance)`` - Returns True if its parameter is a dataclass or an instance of one, otherwise returns False.

>>> from dataclasses import dataclass, asdict, astuple
>>>
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
>>>
>>> @dataclass
... class Coordinates:
...     points: list[Point]
>>>
>>>
>>> p = Point(10, 20)
>>> c = Coordinates([Point(0, 0), Point(10, 4)])
>>>
>>> asdict(p)
{'x': 10, 'y': 20}
>>> asdict(c)
{'points': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}
>>>
>>> astuple(p)
(10, 20)
>>> astuple(c)
([(0, 0), (10, 4)],)


Under the hood
--------------
Your code:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class ShoppingCartItem:
...     name: str
...     unit_price: float
...     quantity: int = 0
...
...     def total_cost(self) -> float:
...         return self.unit_price * self.quantity

Dataclass will generate:

>>> class ShoppingCartItem:
...     name: str
...     unit_price: float
...     quantity: int
...
...     def total_cost(self) -> float:
...         return self.unit_price * self.quantity
...
...     ## All code below is added by dataclass
...
...     def __init__(self, name: str, unit_price: float, quantity: int = 0) -> None:
...         self.name = name
...         self.unit_price = unit_price
...         self.quantity = quantity
...
...     def __repr__(self):
...         return f'ShoppingCartItem(name={self.name!r}, unit_price={self.unit_price!r}, quantity={self.quantity!r})'
...
...     def __eq__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) == (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __ne__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) != (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __lt__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) < (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __le__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) <= (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __gt__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) > (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __ge__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) >= (other.name, other.unit_price, other.quantity)
...         return NotImplemented


Use Cases
---------
>>> from dataclasses import dataclass
>>>
>>>
>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
>>>
>>>
>>> flowers = list(Iris(*row) for row in DATA[1:])
>>> print(flowers)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
 Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
 Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
 Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
 Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
 Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa')]


Assignments
-----------
.. literalinclude:: assignments/oop_dataclass_a.py
    :caption: :download:`Solution <assignments/oop_dataclass_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_dataclass_b.py
    :caption: :download:`Solution <assignments/oop_dataclass_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_dataclass_c.py
    :caption: :download:`Solution <assignments/oop_dataclass_c.py>`
    :end-before: # Solution
