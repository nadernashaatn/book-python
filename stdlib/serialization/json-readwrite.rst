JSON Read/Write
===============


Mapping to JSON
---------------
* ``json.dumps(DATA: dict) -> str``
* ``json.loads(DATA: str) -> dict``

Serializing mapping to JSON:

.. code-block:: python

    import json


    DATA = {'firstname': 'Mark',
            'lastname': 'Watney'}

    result = json.dumps(DATA)

    type(result)
    # <class 'str'>
    print(result)
    # {"firstname": "Mark", "lastname": "Watney"}

Deserializing mapping from JSON:

.. code-block:: python

    import json


    DATA = '{"firstname": "Mark", "lastname": "Watney"}'

    result = json.loads(DATA)

    type(result)
    # <class 'dict'>
    print(result)
    # {'firstname': 'Mark', 'lastname': 'Watney'}


Sequence to JSON
----------------
* ``json.dumps(data: Sequence[dict]) -> str``
* ``json.loads(data: str) -> list[dict]``

Serializing sequence to JSON:

.. code-block:: python

    import json


    DATA = [{'firstname': 'Melissa', 'lastname': 'Lewis'},
            {'firstname': 'Rick', 'lastname': 'Martinez'},
            {'firstname': 'Mark', 'lastname': 'Watney'}]

    result = json.dumps(DATA)

    type(result)
    # <class 'str'>
    print(result)
    # [{"firstname": "Melissa", "lastname": "Lewis"},
    #  {"firstname": "Rick", "lastname": "Martinez"},
    #  {"firstname": "Mark", "lastname": "Watney"}]

.. code-block:: python

    import json


    DATA = '[{"firstname": "Melissa", "lastname": "Lewis"}, {"firstname": "Rick", "lastname": "Martinez"}, {"firstname": "Mark", "lastname": "Watney"}]'

    result = json.loads(DATA)

    type(result)
    # <class 'list'>
    print(result)
    # [{'firstname': 'Melissa', 'lastname': 'Lewis'},
    #  {'firstname': 'Rick', 'lastname': 'Martinez'},
    #  {'firstname': 'Mark', 'lastname': 'Watney'}]


.. code-block:: python

    import json

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor')]

    json.dumps(DATA)
    # [["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"],
    #  [5.8, 2.7, 5.1, 1.9, "virginica"],
    #  [5.1, 3.5, 1.4, 0.2, "setosa"],
    #  [5.7, 2.8, 4.1, 1.3, "versicolor"]]

.. code-block:: python

    import json
    from pprint import pprint


    DATA = '[["Sepal length", "Sepal width", "Petal length", "Petal width", "Species"], [5.8, 2.7, 5.1, 1.9, "virginica"], [5.1, 3.5, 1.4, 0.2, "setosa"], [5.7, 2.8, 4.1, 1.3, "versicolor"]]'

    json.loads(DATA)
    # [['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'],
    #  [5.8, 2.7, 5.1, 1.9, 'virginica'],
    #  [5.1, 3.5, 1.4, 0.2, 'setosa'],
    #  [5.7, 2.8, 4.1, 1.3, 'versicolor']]


Write JSON File
---------------
* ``json.dump(data: dict, file: TextIOWrapper) -> None``
* file extension ``.json``

Serialize to JSON:

.. code-block:: python

    import json

    FILE = r'_temporary.json'

    DATA = {'firstname': 'Mark',
            'lastname': 'Watney'}

    with open(FILE, mode='w') as file:
        json.dump(DATA, file)


    print(open(FILE).read())
    # {"firstname": "Mark", "lastname": "Watney"}



Read JSON File
--------------
* ``json.load(file: TextIOWrapper) -> dict``
* file extension ``.json``

Serialize to JSON:

.. code-block:: python

    import json


    FILE = r'_temporary.json'
    DATA = '{"firstname": "Mark", "lastname": "Watney"}'
    open(FILE, mode='w').write(DATA)


    with open(FILE) as file:
        result = json.load(file)


    type(result)
    # <class 'dict'>
    print(result)
    # {'firstname': 'Mark', 'lastname': 'Watney'}


Assignments
-----------
.. literalinclude:: assignments/json_readwrite_a.py
    :caption: :download:`Solution <assignments/json_readwrite_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_readwrite_b.py
    :caption: :download:`Solution <assignments/json_readwrite_b.py>`
    :end-before: # Solution
