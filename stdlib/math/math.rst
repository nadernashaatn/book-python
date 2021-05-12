Math Stdlib
===========


Constans
--------
* ``inf`` or ``Infinity``
* ``-inf`` or ``-Infinity``
* ``1e6`` or ``1e-4``


Functions
---------
* ``abs()``
* ``round()``
* ``pow()``
* ``sum()``
* ``min()``
* ``max()``
* ``divmod()``
* ``complex()``


``math``
--------

Constants
---------
.. code-block:: python

    import math

    math.pi         # The mathematical constant π = 3.141592…, to available precision.
    math.e          # The mathematical constant e = 2.718281…, to available precision.
    math.tau        # The mathematical constant τ = 6.283185…, to available precision.

Degree/Radians Conversion
-------------------------
.. code-block:: python

    import math

    math.degrees(x)     # Convert angle x from radians to degrees.
    math.radians(x)     # Convert angle x from degrees to radians.

Rounding to lower
-----------------
.. code-block:: python

    import math

    math.floor(3.14)                # 3
    math.floor(3.00000000000000)    # 3
    math.floor(3.00000000000001)    # 3
    math.floor(3.99999999999999)    # 3

Rounding to higher
------------------
.. code-block:: python

    import math

    math.ceil(3.14)                 # 4
    math.ceil(3.00000000000000)     # 3
    math.ceil(3.00000000000001)     # 4
    math.ceil(3.99999999999999)     # 4

Logarithms
----------
.. code-block:: python

    import math

    math.log(x)     # if base is not set, then ``e``
    math.log(x, base=2)
    math.log(x, base=10)
    math.log10()    # Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).
    math.log2(x)    # Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).

    math.exp(x)

Linear Algebra
--------------
.. code-block:: python

    import math

    math.sqrt(x)     # Return the square root of x.
    math.pow(x, y)   # Return x raised to the power y.

.. code-block:: python

    import math

    math.hypot(*coordinates)    # 2D, since Python 3.8 also multiple dimensions
    math.dist(p, q)             # Euclidean distance, since Python 3.8
    math.gcd(*integers)         # Greatest common divisor
    math.lcm(*integers)         # Least common multiple, since Python 3.9
    math.perm(n, k=None)        # Return the number of ways to choose k items from n items without repetition and with order.
    math.prod(iterable, *, start=1)  # Calculate the product of all the elements in the input iterable. The default start value for the product is 1., since Python 3.8
    math.remainder(x, y)        # Return the IEEE 754-style remainder of x with respect to y.

Trigonometry
------------
.. code-block:: python

    import math

    math.sin()
    math.cos()
    math.tan()

    math.asin(x)
    math.acos(x)
    math.atan(x)
    math.atan2(x)

Hyperbolic functions:

.. code-block:: python

    import math

    math.sinh()         # Return the hyperbolic sine of x.
    math.cosh()         # Return the hyperbolic cosine of x.
    math.tanh()         # Return the hyperbolic tangent of x.

    math.asinh(x)       # Return the inverse hyperbolic sine of x.
    math.acosh(x)       # Return the inverse hyperbolic cosine of x.
    math.atanh(x)       # Return the inverse hyperbolic tangent of x.

Infinity
--------
.. code-block:: python

    float('inf')                # inf
    float('-inf')               # -inf
    float('Infinity')           # inf
    float('-Infinity')          # -inf

.. code-block:: python

    from math import isinf

    isinf(float('inf'))         # True
    isinf(float('Infinity'))    # True
    isinf(float('-inf'))        # True
    isinf(float('-Infinity'))   # True

    isinf(1e308)                # False
    isinf(1e309)                # True

    isinf(1e-9999999999999999)  # False

Absolute value
--------------
.. code-block:: python

    abs(1)          # 1
    abs(-1)         # 1

    abs(1.2)        # 1.2
    abs(-1.2)       # 1.2

.. code-block:: python

    from math import fabs

    fabs(1)         # 1.0
    fabs(-1)        # 1.0

    fabs(1.2)       # 1.2
    fabs(-1.2)      # 1.2

.. code-block:: python

    from math import fabs

    vector = [1, 0, 1]

    abs(vector)
    # Traceback (most recent call last):
    # TypeError: bad operand type for abs(): 'list'

    fabs(vector)
    # Traceback (most recent call last):
    # TypeError: must be real number, not list

.. code-block:: python

    from math import sqrt


    def vector_abs(vector):
        return sqrt(sum(n**2 for n in vector))


    vector = [1, 0, 1]
    vector_abs(vector)
    # 1.4142135623730951

.. code-block:: python

    from math import sqrt


    class Vector:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def __abs__(self):
            return sqrt(self.x**2 + self.y**2 + self.z**2)


    vector = Vector(x=1, y=0, z=1)
    abs(vector)
    # 1.4142135623730951


Assignments
-----------
.. todo:: Convert assignments to literalinclude

Trigonometry
^^^^^^^^^^^^
* Assignment: Trigonometry
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Read input (angle in degrees) from user
    2. User will type ``int`` or ``float``
    3. Print all trigonometric functions (sin, cos, tg, ctg)
    4. If there is no value for this angle, raise an exception
    5. Run doctests - all must succeed

Polish:
    1. Program wczytuje od użytkownika wielkość kąta w stopniach
    2. Użytkownik zawsze podaje ``int`` albo ``float``
    3. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
    4. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta podnieś
       stosowny wyjątek
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * ``input('Type angle [deg]: ')``

Euclidean distance 2D
^^^^^^^^^^^^^^^^^^^^^
* Assignment: Euclidean distance 2D
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Given are two points ``A: tuple[int, int]`` and ``B: tuple[int, int]``
    2. Coordinates are in cartesian system
    3. Points ``A`` and ``B`` are in two dimensional space
    4. Calculate distance between points using Euclidean algorithm
    5. Run doctests - all must succeed

Polish:
    1. Dane są dwa punkty ``A: tuple[int, int]`` i ``B: tuple[int, int]``
    2. Koordynaty są w systemie kartezjańskim
    3. Punkty ``A`` i ``B`` są w dwuwymiarowej przestrzeni
    4. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    5. Uruchom doctesty - wszystkie muszą się powieść

.. code-block:: python

    def euclidean_distance(A, B):
        """
        >>> A = (1, 0)
        >>> B = (0, 1)
        >>> euclidean_distance(A, B)
        1.4142135623730951

        >>> euclidean_distance((0,0), (1,0))
        1.0

        >>> euclidean_distance((0,0), (1,1))
        1.4142135623730951

        >>> euclidean_distance((0,1), (1,1))
        1.0

        >>> euclidean_distance((0,10), (1,1))
        9.055385138137417
        """
        x1 = ...
        y1 = ...
        x2 = ...
        y2 = ...
        return ...

.. figure:: img/math-euclidean-distance.png

    Calculate Euclidean distance in Cartesian coordinate system

Hints:
    * :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2`

Euclidean distance ``n`` dimensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Assignment: Euclidean distance ``n`` dimensions
* Complexity: easy
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Given are two points ``A: Sequence[int]`` and ``B: Sequence[int]``
    3. Coordinates are in cartesian system
    4. Points ``A`` and ``B`` are in ``N``-dimensional space
    5. Points ``A` and ``B`` must be in the same space
    6. Calculate distance between points using Euclidean algorithm
    7. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dane są dwa punkty ``A: Sequence[int]`` i ``B: Sequence[int]``
    3. Koordynaty są w systemie kartezjańskim
    4. Punkty ``A`` i ``B`` są w ``N``-wymiarowej przestrzeni
    5. Punkty ``A`` i ``B`` muszą być w tej samej przestrzeni
    6. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    7. Uruchom doctesty - wszystkie muszą się powieść

Given:
    .. code-block:: python

        def euclidean_distance(A, B):
            """
            >>> A = (0,1,0,1)
            >>> B = (1,1,0,0)
            >>> euclidean_distance(A, B)
            1.4142135623730951

            >>> euclidean_distance((0,0,0), (0,0,0))
            0.0

            >>> euclidean_distance((0,0,0), (1,1,1))
            1.7320508075688772

            >>> euclidean_distance((0,1,0,1), (1,1,0,0))
            1.4142135623730951

            >>> euclidean_distance((0,0,1,0,1), (1,1,0,0,1))
            1.7320508075688772

            >>> euclidean_distance((0,0,1,0,1), (1,1))
            Traceback (most recent call last):
            ValueError: Points must be in the same dimensions
            """
            return ...

Hints:
    * :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + ... + (n_2 - n_1)^2}`
    * ``for n1, n2 in zip(A, B)``

Matrix multiplication
^^^^^^^^^^^^^^^^^^^^^
* Assignment: Matrix multiplication
* Complexity: hard
* Lines of code: 6 lines
* Time: 21 min

English:
    1. Use code from "Input" section (see below)
    2. Multiply matrices using nested ``for`` loops
    3. Run doctests - all must succeed

Polish:
    1. Użyj code z sekcji "Input" (patrz poniżej)
    2. Pomnóż macierze wykorzystując zagnieżdżone pętle ``for``
    3. Uruchom doctesty - wszystkie muszą się powieść

Given:
    .. code-block:: python

        def matrix_multiplication(A, B):
            """
            >>> A = [[1, 0], [0, 1]]
            >>> B = [[4, 1], [2, 2]]
            >>> matrix_multiplication(A, B)
            [[4, 1], [2, 2]]

            >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
            >>> B = [[4,1], [2,2], [5,1], [2,3]]
            >>> matrix_multiplication(A, B)
            [[9, 2], [7, 3], [21, 8], [28, 8]]
            """
            return

Hints:
    * Zero matrix
    * Three nested ``for`` loops

Triangle
^^^^^^^^
* Assignment: Triangle
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Calculate triangle area
    2. User will input base and height
    3. Input numbers will be only ``int`` and ``float``
    4. Run doctests - all must succeed

Polish:
    1. Obliczy pole trójkąta
    2. Użytkownik poda wysokość i długość podstawy
    3. Wprowadzone dane będą tylko ``int`` lub ``float``
    4. Uruchom doctesty - wszystkie muszą się powieść
