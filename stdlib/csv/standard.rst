CSV Standard
============


Rationale
---------
* CSV - Comma Separated Values
* CSV - Character Separated Values

CSV file with numeric values.:

.. code-block:: text

    5.4,3.9,1.3,0.4,0
    5.9,3.0,5.1,1.8,1
    6.0,3.4,4.5,1.6,2

CSV file with text values. First line is a header.:

.. code-block:: text

    "First Name", "Last Name"
    "Mark", "Watney"
    "Jan", "Twardowski"
    "Melissa", "Lewis"
    "Alex", "Vogel"

CSV file with mixed values (numeric and strings). First line is a header.:

.. code-block:: text

    sepal_length,sepal_width,petal_length,petal_width,species
    5.4,3.9,1.3,0.4,setosa
    5.9,3.0,5.1,1.8,virginica
    6.0,3.4,4.5,1.6,versicolor
    7.3,2.9,6.3,1.8,virginica
    5.6,2.5,3.9,1.1,versicolor
    5.4,3.9,1.3,0.4,setosa


Encoding
--------
* ``utf-8`` - international standard (should be always used!)
* ``iso-8859-1`` - ISO standard for Western Europe and USA
* ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
* ``cp1250`` or ``windows-1250`` - Polish encoding on Windows
* ``cp1251`` or ``windows-1251`` - Russian encoding on Windows
* ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
* ``ASCII`` - ASCII characters only

.. code-block:: python

    with open(FILE, encoding='utf-8') as file:
        ...


Quoting
-------
* ``csv.QUOTE_ALL`` (safest)
* ``csv.QUOTE_MINIMAL``
* ``csv.QUOTE_NONE``
* ``csv.QUOTE_NONNUMERIC``

``quoting=csv.QUOTE_ALL``:

.. code-block:: text

    "Sepal length","Sepal width","Petal length","Petal width","Species"
    "5.8","2.7","5.1","1.9","virginica"
    "5.1","3.5","1.4","0.2","setosa"
    "5.7","2.8","4.1","1.3","versicolor"

``quoting=csv.QUOTE_MINIMAL``:

.. code-block:: text

    Sepal length,Sepal width,Petal length,Petal width,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

``quoting=csv.QUOTE_NONE``:

.. code-block:: text

    Sepal length,Sepal width,Petal length,Petal width,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

``quoting=csv.QUOTE_NONNUMERIC``:

.. code-block:: text

    "Sepal length","Sepal width","Petal length","Petal width","Species"
    5.8,2.7,5.1,1.9,"virginica"
    5.1,3.5,1.4,0.2,"setosa"
    5.7,2.8,4.1,1.3,"versicolor"


Quotechar
---------
* ``"`` - quote char (best)
* ``'`` - apostrophe

``quotechar='"'``:

.. code-block:: text

    "Sepal length","Sepal width","Petal length","Petal width","Species"
    "5.8","2.7","5.1","1.9","virginica"
    "5.1","3.5","1.4","0.2","setosa"
    "5.7","2.8","4.1","1.3","versicolor"

``quotechar="'"``:

.. code-block:: text

    'Sepal length','Sepal width','Petal length','Petal width','Species'
    '5.8','2.7','5.1','1.9','virginica'
    '5.1','3.5','1.4','0.2','setosa'
    '5.7','2.8','4.1','1.3','versicolor'

``quotechar='|'``:

.. code-block:: text

    |Sepal length|,|Sepal width|,|Petal length|,|Petal width|,|Species|
    |5.8|,|2.7|,|5.1|,|1.9|,|virginica|
    |5.1|,|3.5|,|1.4|,|0.2|,|setosa|
    |5.7|,|2.8|,|4.1|,|1.3|,|versicolor|


``quotechar='/'``:

.. code-block:: text

    /Sepal length/,/Sepal width/,/Petal length/,/Petal width/,/Species/
    /5.8/,/2.7/,/5.1/,/1.9/,/virginica/
    /5.1/,/3.5/,/1.4/,/0.2/,/setosa/
    /5.7/,/2.8/,/4.1/,/1.3/,/versicolor/

Delimiter
---------
``delimiter=','``:

.. code-block:: text

    Sepal length,Sepal width,Petal length,Petal width,Species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor

``delimiter=';'``:

.. code-block:: text

    Sepal length;Sepal width;Petal length;Petal width;Species
    5.8;2.7;5.1;1.9;virginica
    5.1;3.5;1.4;0.2;setosa
    5.7;2.8;4.1;1.3;versicolor

``delimiter='|'``:

.. code-block:: text

    Sepal length|Sepal width|Petal length|Petal width|Species
    5.8|2.7|5.1|1.9|virginica
    5.1|3.5|1.4|0.2|setosa
    5.7|2.8|4.1|1.3|versicolor

``delimiter='\t'``:

.. code-block:: text

    Sepal length	Sepal width	Petal length	Petal width	Species
    5.8	2.7	5.1	1.9	virginica
    5.1	3.5	1.4	0.2	setosa
    5.7	2.8	4.1	1.3	versicolor


Lineterminator
--------------
* ``\r\n`` - New line on Windows
* ``\n`` - New line on ``*nix``
* ``*nix`` operating systems: Linux, macOS, BSD and other POSIX compliant OSes (excluding Windows)


Dialects
--------
.. code-block:: text

    1,2 and 2,5 -> 1,2;2,5  # delimiter=';'
    1.2 and 2.5 -> 1.2,2.5  # delimiter=','

.. code-block:: text

    1,2;2,5 -> 1 and 2; and 2 and 5  # delimiter=','
    1,2 -> 1,2;2,5  # delimiter=';'
    1.2,2.5 -> 1.2 and 2.5  # delimiter=','

.. code-block:: python

    import csv

    csv.list_dialects()
    # ['excel', 'excel-tab', 'unix']

* Microsoft Excel 2016 uses:

    * ``quotechar='"'``
    * ``delimiter=','``
    * ``lineterminator='\n'``
    * ``encoding='...'`` - depends on Windows version and settings typically ``windows-*``



Good Practices
--------------
* Always specify:

    * ``delimiter=','`` to  ``csv.DictReader()`` object
    * ``quotechar='"'`` to ``csv.DictReader()`` object
    * ``quoting=csv.QUOTE_ALL`` to ``csv.DictReader()`` object
    * ``lineterminator='\n'`` to ``csv.DictReader()`` object
    * ``encoding='utf-8'`` to ``open()`` function (especially when working with Microsoft Excel)

