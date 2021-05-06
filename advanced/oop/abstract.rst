Abstract Class
==============


Rationale
---------
* Since Python 3.0: :pep:`3119` -- Introducing Abstract Base Classes
* Cannot instantiate
* Possible to indicate which method must be implemented by child
* Inheriting class must implement all methods
* Some methods can have implementation

.. glossary::

    abstract class
        Class which can only be inherited, not instantiated

    abstract method
        Method must be implemented in a subclass

    abstract static method
        Static method which must be implemented in a subclass


Syntax
------
* New class ``ABC`` has ``ABCMeta`` as its meta class.
* Using ``ABC`` as a base class has essentially the same effect as specifying ``metaclass=abc.ABCMeta``, but is simpler to type and easier to read.
* ``abc.ABC`` basically just an extra layer over ``metaclass=abc.ABCMeta``
* ``abc.ABC`` implicitly defines the metaclass for you

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class MyClass(metaclass=ABCMeta):

        @abstractmethod
        def mymethod(self):
            pass


Abstract Method
---------------
.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class Astronaut(metaclass=ABCMeta):
        @abstractmethod
        def say_hello(self):
            pass


    astro = Astronaut()
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello

.. code-block:: python

    from abc import ABC, abstractmethod


    class Astronaut(ABC):
        @abstractmethod
        def say_hello(self):
            pass


    astro = Astronaut()
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Astronaut with abstract method say_hello


Abstract Property
-----------------
* ``abc.abstractproperty`` is deprecated since Python 3.3
* Use ``property`` with ``abc.abstractmethod`` instead

.. code-block:: python

    from abc import ABCMeta, abstractproperty


    class Monster(metaclass=ABCMeta):
        @abstractproperty
        def DAMAGE(self) -> int:
            pass

    class Dragon(Monster):
        DAMAGE: int = 10


    d = Dragon()

    print('no errors')
    # no errors

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class Monster(metaclass=ABCMeta):
        @property
        @abstractmethod
        def DAMAGE(self) -> int:
            pass


    class Dragon(Monster):
        DAMAGE: int = 10


    d = Dragon()

    print('no errors')
    # no errors

Common Problems
---------------
In order to use Abstract Base Class you must create abstract method. Otherwise it won't prevent from instantiating:

.. code-block:: python

    from abc import ABCMeta


    class Astronaut(metaclass=ABCMeta):
        pass


    astro = Astronaut()   # It will not raise an error, because there are no abstractmethods

    print('no errors')
    # no errors

Must implement all abstract methods:

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class Human(metaclass=ABCMeta):
        @abstractmethod
        def get_name(self):
            pass

        @abstractmethod
        def set_name(self):
            pass


    class Astronaut(Human):
        pass

    astro = Astronaut()  # None abstractmethod is implemented in child class
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Astronaut with abstract methods get_name, set_name

All abstract methods must be implemented in child class:

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class Human(metaclass=ABCMeta):
        @abstractmethod
        def get_name(self):
            pass

        @abstractmethod
        def set_name(self):
            pass


    class Astronaut(Human):
        def get_name(self):
            return 'Mark Watney'


    astro = Astronaut()  # There are abstractmethods without implementation
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Astronaut with abstract method set_name

Problem - Child class has no abstract attribute (using ``abstractproperty``):

.. code-block:: python

    from abc import ABCMeta, abstractproperty


    class Monster(metaclass=ABCMeta):
        @abstractproperty
        def DAMAGE(self) -> int:
            pass

    class Dragon(Monster):
        pass


    d = Dragon()
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Dragon with abstract method DAMAGE

Problem - Child class has no abstract attribute (using ``property`` and ``abstractmethod``):

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class Monster(metaclass=ABCMeta):
        @property
        @abstractmethod
        def DAMAGE(self) -> int:
            pass

    class Dragon(Monster):
        pass


    d = Dragon()
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Dragon with abstract method DAMAGE

Problem - Despite having defined property, the order of decorators (``abstractmethod`` and ``property`` is invalid). Should be reversed: first ``@property`` then ``@abstractmethod``:

.. code-block:: python

    from abc import ABCMeta, abstractmethod


    class Monster(metaclass=ABCMeta):
        @abstractmethod
        @property
        def DAMAGE(self) -> int:
            pass


    class Dragon(Monster):
        DAMAGE: int = 10


    d = Dragon()
    # Traceback (most recent call last):
    # AttributeError: attribute '__isabstractmethod__' of 'property' objects is not writable


``abc`` is common name and it is very easy to create file, variable lub module with the same name as the library, hence overwrite it. In case of error. Check all entries in ``sys.path`` or ``sys.modules['abc']`` to find what is overwriting it:

.. code-block:: python

    from pprint import pprint
    import sys


    sys.modules['abc']
    # <module 'abc' from '/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/abc.py'>

    pprint(sys.path)
    # ['/Applications/PyCharm 2021.1 EAP.app/Contents/plugins/python/helpers/pydev',
    #  '/Users/watney/book-python',
    #  '/Applications/PyCharm 2021.1 EAP.app/Contents/plugins/python/helpers/pycharm_display',
    #  '/Applications/PyCharm 2021.1 EAP.app/Contents/plugins/python/helpers/third_party/thriftpy',
    #  '/Applications/PyCharm 2021.1 EAP.app/Contents/plugins/python/helpers/pydev',
    #  '/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
    #  '/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
    #  '/usr/local/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',
    #  '/Users/watney/.virtualenvs/python-3.9/lib/python3.9/site-packages',
    #  '/Applications/PyCharm 2021.1 EAP.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend',
    #  '/Users/watney/book-python',
    #  '/Users/watney/book-python/_tmp']


Use Cases
---------
Abstract Class:

.. code-block:: python

    from abc import ABC, abstractmethod


    class Document(ABC):
        def __init__(self, file):
            with open(file, mode='rb') as file:
                self.file = file
                self.content = file.read()

        @abstractmethod
        def display(self):
            pass


    class PDFDocument(Document):
        def display(self):
            # display self.content as PDF Document

    class WordDocument(Document):
        def display(self):
            # display self.content as Word Document


    file1 = PDFDocument('filename.pdf')
    file1.display()

    file2 = Document('filename.txt')
    # Traceback (most recent call last):
    # TypeError: Can't instantiate abstract class Document with abstract method display


Further Reading
---------------
* https://docs.python.org/dev/library/collections.abc.html#collections-abstract-base-classes


Assignments
-----------
.. literalinclude:: assignments/oop_abstract_a.py
    :caption: :download:`Solution <assignments/oop_abstract_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_b.py
    :caption: :download:`Solution <assignments/oop_abstract_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_c.py
    :caption: :download:`Solution <assignments/oop_abstract_b.py>`
    :end-before: # Solution
