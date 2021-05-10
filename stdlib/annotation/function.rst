Function Type Annotation
========================


Rationale
---------
* Before Python 3.9 you need ``from typing import List, Set, Tuple, Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections


Return
------
>>> def say_hello() -> str:
...     return 'My name... José Jiménez'


Parameters
----------
.. code-block:: python

    def add_numbers(a: int, b: int) -> int:
        return a + b

    add_numbers(1, 2)
    # 3


Union
-----
.. code-block:: python

    from typing import Union


    def add_numbers(a: Union[int,float], b: Union[int,float]) -> Union[int,float]:
        return a + b


    add_numbers(1, 2)       # 'Ok'
    add_numbers(1.5, 2.5)   # 'Ok'

.. code-block:: python

    from typing import Union

    Number = Union[int, float]

    def add_numbers(a: Number, b: Number) -> Number:
        return a + b

    add_numbers(1, 2)       # 'Ok'
    add_numbers(1.5, 2.5)   # 'Ok'

Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

.. code-block:: python
    :force:

    def add_numbers(a: int|float, b: int|float) -> int|float:
        return a + b


    add_numbers(1, 2)       # 'Ok'
    add_numbers(1.5, 2.5)   # 'Ok'


Optional
--------
.. code-block:: python

    from typing import Union


    def find(text: str, what: str) -> Union[int,None]:
        position = text.find(what)

        if position == -1:
            return None
        else:
            return position


    find('Python', 'o')      # 4
    find('Python', 'x')      # None

.. code-block:: python

    from typing import Optional


    def find(text: str, what: str) -> Optional[int]:
        position = text.find(what)

        if position == -1:
            return None
        else:
            return position


    find('Python', 'o')      # 4
    find('Python', 'x')      # None

Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y

.. code-block:: python
    :force:

    def find(text: str, what: str) -> int|None:
        position = text.find(what)

        if position == -1:
            return None
        else:
            return position


    find('Python', 'o')      # 4
    find('Python', 'x')      # None

Since Python 3.10: :pep:`645` -- Allow writing optional types as x?

.. code-block:: python
    :force:

    def find(text: str, what: str) -> int?:
        position = text.find(what)

        if position == -1:
            return None
        else:
            return position


    find('Python', 'o')      # 4
    find('Python', 'x')      # None


NoReturn
--------
.. code-block:: python

    from typing import NoReturn


    def stop() -> NoReturn:
        raise RuntimeError

.. code-block:: python

    from typing import Union, NoReturn


    def valid_email(email: str) -> Union[NoReturn, str]:
        if '@' in email:
            return email
        else:
            raise ValueError('Invalid Email')


    valid_email('mark.watney@nasa.gov')
    # 'mark.watney@nasa.gov'

    valid_email('mark.watney_at_nasa.gov')
    # Traceback (most recent call last):
    # ValueError: Invalid Email


Literal
-------
* Since Python 3.8: :pep:`586` -- Literal Types

.. code-block:: python

    from typing import Literal


    def open(filename: str, mode: Literal['r','w','a']) -> None:
        pass

    open('data.csv', mode='w')  # Ok
    open('data.csv', mode='r')  # Ok
    open('data.csv', mode='a')  # Ok
    open('data.csv', mode='x')  # Error


Annotations
-----------
.. code-block:: python

    def add(a: int, b: int) -> int:
        return a + b


    add.__annotations__
    # {'a': <class 'int'>,
    #  'b': <class 'int'>,
    #  'return': <class 'int'>}

Since Python 3.10: :pep:`563` -- Postponed Evaluation of Annotations

.. code-block:: python

    def add(a: int, b: int) -> int:
        return a + b


    add.__annotations__
    # {'a': 'int',
    #  'b': 'int',
    #  'return': 'int'}


Errors
------
* Python will execute without even warning
* Your IDE and ``mypy`` et. al. will yield errors

.. code-block:: python

    def add_numbers(a: int, b: int) -> int:
        return a + b


    add_numbers('Mark', 'Watney')
    # 'MarkWatney'


Good Engineering Practices
--------------------------
.. code-block:: python

    from typing import Union

    def add_numbers(a: Union[int,float],
                    b: Union[int,float]
                    ) -> Union[int,float]:
        return a + b

    add_numbers(1, 2)       # 'Ok'
    add_numbers(1.5, 2.5)   # 'Ok'


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`
