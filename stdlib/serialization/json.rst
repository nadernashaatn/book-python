Serialization JSON
==================


JSON Syntax
-----------
* JavaScript Object Notation
* JSON format is similar to ``dict`` notation in Python
* Differences:

    * Coma ``,`` is not allowed after the last element in list or object
    * Fields are enclosed only by double quote ``"`` character
    * ``true`` and ``false`` is always lower-cased
    * Instead of ``None`` there is ``null``
    * ``camelCase`` is convention, although ``snake_case`` is also valid

Example JSON file:

.. code-block:: json

    [{"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
     {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
     {"sepalLength": false, "sepalWidth": true, "petalLength": null, "petalWidth": 0.2, "species": null}]

JSON or Python ``list[dict]``?:

.. code-block:: python

    {'mission': 'Ares 3',
     'launch_date': datetime(2035, 6, 29, tzinfo=timezone.utc),
     'destination': 'Mars',
     'destination_landing': datetime(2035, 11, 7, tzinfo=timezone.utc),
     'destination_location': 'Acidalia Planitia',
     'crew': [{'astronaut': 'Melissa Lewis', 'date_of_birth': date(1995, 7, 15)},
              {'astronaut': 'Rick Martinez', 'date_of_birth': date(1996, 1, 21)},
              {'astronaut': 'Alex Vogel', 'date_of_birth': date(1994, 11, 15)},
              {'astronaut': 'Chris Beck', 'date_of_birth': date(1999, 8, 2)},
              {'astronaut': 'Beth Johansen', 'date_of_birth': date(2006, 5, 9)},
              {'astronaut': 'Mark Watney', 'date_of_birth': date(1994, 10, 12)}]}

JSON or Python ``list[dict]``?:

.. code-block:: json

    {"mission": "Ares 3",
     "launch_date": "2035-06-29T00:00:00+00:00",
     "destination": "Mars",
     "destination_landing": "2035-11-07T00:00:00+00:00",
     "destination_location": "Acidalia Planitia",
     "crew": [{"astronaut": "Melissa Lewis", "date_of_birth": "1995-07-15"},
              {"astronaut": "Rick Martinez", "date_of_birth": "1996-01-21"},
              {"astronaut": "Alex Vogel", "date_of_birth": "1994-11-15"},
              {"astronaut": "Chris Beck", "date_of_birth": "1999-08-02"},
              {"astronaut": "Beth Johansen", "date_of_birth": "2006-05-09"},
              {"astronaut": "Mark Watney", "date_of_birth": "1994-10-12"}]}

JSON or Python ``list[dict]``?:

.. code-block:: json

    [{"firstname": "Jan", "lastname": "Twardowski", "addresses": [
        {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "post_code": "31-008", "region": "Małopolskie", "country": "Poland"}]},

     {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
        {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

     {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550, "region": "California", "country": "USA"}]},

     {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": "", "city": "Космодро́м Байкону́р", "post_code": "", "region": "Кызылординская область", "country": "Қазақстан"},
        {"street": "", "city": "Звёздный городо́к", "post_code": 141160, "region": "Московская область", "country": "Россия"}]},

     {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},

     {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}]


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



Datetime to JSON
----------------
* problem with ``date``, ``datetime``, ``time``

Exception during encoding datetime:

.. code-block:: python

    from datetime import date
    import json

    DATA = {'firstname': 'Mark',
            'lastname': 'Watney',
            'date_of_birth': date(1994, 10, 12)}

    result = json.dumps(DATA)
    # Traceback (most recent call last):
    # TypeError: Object of type date is not JSON serializable

    from datetime import date
    import json

    DATA = {'firstname': 'Mark',
            'lastname': 'Watney',
            'date_of_birth': date(1994, 10, 12)}

.. code-block:: python

    from datetime import date
    import json

    DATA = {'firstname': 'Mark',
            'lastname': 'Watney',
            'date_of_birth': date(1994, 10, 12)}

    json.JSONEncoder.default = lambda self, date: date.isoformat()
    result = json.dumps(DATA)

    type(result)
    # <class 'str'>
    print(result)
    # {"firstname": "Mark", "lastname": "Watney", "date_of_birth": "1994-10-12"}

Encoder will be used, when standard procedure fails:

.. code-block:: python

    from datetime import date
    import json

    DATA = {'firstname': 'Mark',
            'lastname': 'Watney',
            'date_of_birth': date(1994, 10, 12),
            'first_mission': datetime(1969, 7, 21, 2, 56, 15)}


    class MyEncoder(json.JSONEncoder):
        def default(self, value):
            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%dT%H:%M:%S.%f+00:00')
            if isinstance(value, date):
                return value.strftime('%Y-%m-%d')


    result = json.dumps(DATA, cls=MyEncoder)

    type(result)
    # <class 'str'>
    print(result)
    # {"firstname": "Mark",
    #  "lastname": "Watney",
    #  "date_of_birth": "1994-10-12",
    #  "first_mission": "1969-07-21T02:56:15.000000+00:00"}


JSON to Datetime
----------------
Simple loading returns ``str`` not ``datetime`` or ``date``:

.. code-block:: python

    import json


    DATA = '{"firstname": "Mark", "lastname": "Watney", "date_of_birth": "1994-10-12"}'

    result = json.loads(DATA)
    print(result)
    # {'firstname': 'Mark',
    #  'lastname': 'Watney',
    #  'date_of_birth': '1994-10-12'}

Simple loading returns ``str`` not ``datetime`` or ``date``:

.. code-block:: python

    import json
    from datetime import date


    DATA = '{"firstname": "Mark", "lastname": "Watney", "date_of_birth": "1994-10-12"}'

    def mydecoder(data: dict) -> dict:
        for field, value in data.items():
            if field == 'date_of_birth':
                data[field] = date.fromisoformat(value)
        return data

    result = json.loads(DATA, object_hook=mydecoder)

    type(result)
    # <class 'dict'>
    print(result)
    # {'firstname': 'Mark', 'lastname': 'Watney', 'date_of_birth': datetime.date(1994, 10, 12)}

Decoding ``datetime`` and ``date``:

.. code-block:: python

    from datetime import datetime, timezone
    import json


    DATA = '{"name": "Jan Twardowski", "date": "1961-04-12", "datetime": "1969-07-21T02:56:15.000Z"}'


    class MyDecoder(json.JSONDecoder):
        def __init__(self):
            super().__init__(object_hook=self.default)

        def default(self, result: dict) -> dict:
            for field, value in result.items():
                if field in ['date', 'date_of_birth']:
                    value = datetime.strptime(value, '%Y-%m-%d').date()
                if field in ['datetime']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
                result[field] = value
            return result


    result = json.loads(DATA, cls=MyDecoder)
    pprint(result)
    # {'name': 'Jan Twardowski',
    #  'date': datetime.date(1961, 4, 12),
    #  'datetime': datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc)}

.. code-block:: python

    from datetime import datetime, date, timezone
    import json

    FILE = '_temporary.json'

    DATA = {'mission': 'Ares 3',
            'launch_date': datetime(2035, 6, 29, tzinfo=timezone.utc),
            'destination': 'Mars',
            'destination_landing': datetime(2035, 11, 7, tzinfo=timezone.utc),
            'destination_location': 'Acidalia Planitia',
            'crew': [{'astronaut': 'Melissa Lewis', 'date_of_birth': date(1995, 7, 15)},
                     {'astronaut': 'Rick Martinez', 'date_of_birth': date(1996, 1, 21)},
                     {'astronaut': 'Alex Vogel', 'date_of_birth': date(1994, 11, 15)},
                     {'astronaut': 'Chris Beck', 'date_of_birth': date(1999, 8, 2)},
                     {'astronaut': 'Beth Johansen', 'date_of_birth': date(2006, 5, 9)},
                     {'astronaut': 'Mark Watney', 'date_of_birth': date(1994, 10, 12)}]}


    class MyEncoder(json.JSONEncoder):
        def default(self, value: datetime) -> str:
            return value.isoformat()


    class MyDecoder(json.JSONDecoder):
        date_of_birth: date
        launch_date: datetime
        destination_landing: datetime

        def __init__(self) -> None:
            super().__init__(object_hook=lambda data: {
                    field: getattr(self, method)(value)
                    for field, value in data.items()
                    if (method := self.__annotations__.get(field, str).__name__)})

        def datetime(self, value: str) -> date:
            return datetime.fromisoformat(value)

        def date(self, value: str) -> date:
            return datetime.fromisoformat(value).date()

        def str(self, value: str) -> str:
            return value


    result = json.dumps(DATA, cls=MyEncoder)
    type(result)
    # <class 'str'>
    print(result)
    # {"mission": "Ares 3",
    #  "launch_date": "2035-06-29T00:00:00+00:00",
    #  "destination": "Mars",
    #  "destination_landing": "2035-11-07T00:00:00+00:00",
    #  "destination_location": "Acidalia Planitia",
    #  "crew": [{"astronaut": "Melissa Lewis", "date_of_birth": "1995-07-15"},
    #           {"astronaut": "Rick Martinez", "date_of_birth": "1996-01-21"},
    #           {"astronaut": "Alex Vogel", "date_of_birth": "1994-11-15"},
    #           {"astronaut": "Chris Beck", "date_of_birth": "1999-08-02"},
    #           {"astronaut": "Beth Johansen", "date_of_birth": "2006-05-09"},
    #           {"astronaut": "Mark Watney", "date_of_birth": "1994-10-12"}]}


    result = json.loads(result, cls=MyDecoder)
    type(result)
    # <class 'dict'>
    print(result)
    # {'mission': 'Ares 3',
    #  'launch_date': datetime.datetime(2035, 6, 29, 0, 0, tzinfo=datetime.timezone.utc),
    #  'destination': 'Mars',
    #  'destination_landing': datetime.datetime(2035, 11, 7, 0, 0, tzinfo=datetime.timezone.utc),
    #  'destination_location': 'Acidalia Planitia',
    #  'crew': [{'astronaut': 'Melissa Lewis', 'date_of_birth': datetime.date(1995, 7, 15)},
    #           {'astronaut': 'Rick Martinez', 'date_of_birth': datetime.date(1996, 1, 21)},
    #           {'astronaut': 'Alex Vogel', 'date_of_birth': datetime.date(1994, 11, 15)},
    #           {'astronaut': 'Chris Beck', 'date_of_birth': datetime.date(1999, 8, 2)},
    #           {'astronaut': 'Beth Johansen', 'date_of_birth': datetime.date(2006, 5, 9)},
    #           {'astronaut': 'Mark Watney', 'date_of_birth': datetime.date(1994, 10, 12)}]}


Python Object to JSON
---------------------
Encoding nested objects with relations to JSON:

.. code-block:: python

    import json
    from dataclasses import dataclass


    @dataclass
    class Mission:
        year: int
        name: str


    @dataclass
    class Astronaut:
        name: str
        missions: list[Mission]



    CREW = [
        Astronaut('Melissa Lewis', []),

        Astronaut('Mark Watney', missions=[
            Mission(2035, 'Ares 3')]),

        Astronaut('Jan Twardowski', missions=[
            Mission(1969, 'Apollo 18'),
            Mission(2024, 'Artemis 3')]),
    ]


    class MyEncoder(json.JSONEncoder):
        def default(self, obj):
            result = vars(obj)
            result['__type__'] = obj.__class__.__name__
            return result


    result = json.dumps(CREW, cls=MyEncoder, sort_keys=True, indent=2)
    print(type(result))
    # <class 'str'>
    print(result)
    # [
    #   {
    #     "__type__": "Astronaut",
    #     "missions": [],
    #     "name": "Melissa Lewis"
    #   },
    #   {
    #     "__type__": "Astronaut",
    #     "missions": [
    #       {
    #         "__type__": "Mission",
    #         "name": "Ares 3",
    #         "year": 2035
    #       }
    #     ],
    #     "name": "Mark Watney"
    #   },
    #   {
    #     "__type__": "Astronaut",
    #     "missions": [
    #       {
    #         "__type__": "Mission",
    #         "name": "Apollo 18",
    #         "year": 1969
    #       },
    #       {
    #         "__type__": "Mission",
    #         "name": "Artemis 3",
    #         "year": 2024
    #       }
    #     ],
    #     "name": "Jan Twardowski"
    #   }
    # ]


JSON to Python Object
---------------------
 Encoding nested objects with relations to JSON:

.. code-block:: python

    from dataclasses import dataclass
    import json


    DATA = """[
        {"__type__": "Astronaut", "name": "Melissa Lewis", "missions": []},
        {"__type__": "Astronaut", "name": "Mark Watney", "missions": [{"__type__": "Mission", "name": "Ares 3", "year": 2035}]},
        {"__type__": "Astronaut", "name": "Jan Twardowski", "missions": [
            {"__type__": "Mission", "name": "Apollo 18", "year": 1969},
            {"__type__": "Mission", "name": "Artemis 3", "year": 2024}]}]"""


    @dataclass
    class Mission:
        year: int
        name: str


    @dataclass
    class Astronaut:
        name: str
        missions: list[Mission]


    class MyDecoder(json.JSONDecoder):
        def __init__(self):
            super().__init__(object_hook=self.default)

        def default(self, obj):
            clsname = obj.pop('__type__')
            cls = globals()[class_name]
            return cls(**obj)


    result = json.loads(DATA, cls=MyDecoder)
    print(type(result))
    # <class 'list'>
    print(result)
    # [Astronaut(name='Melissa Lewis', missions=[]),
    #  Astronaut(name='Mark Watney', missions=[
    #       Mission(year=2035, name='Ares 3')]),
    #  Astronaut(name='Jan Twardowski', missions=[
    #       Mission(year=1969, name='Apollo 18'),
    #       Mission(year=2024, name='Artemis 3')])]



Pretty Printing JSON
--------------------
* JSON can be minified to save space for network transmission
* It is not very readable

Minified JSON file:

.. code-block:: console

    $ DATA='https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/iris.json'
    $ curl $DATA
    [{"sepalLength":5.1,"sepalWidth":3.5,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.9,"sepalWidth":3,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.7,"sepalWidth":3.2,"petalLength":1.3,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.6,"sepalWidth":3.1,"petalLength":1.5,"petalWidth":0.2,"species":"setosa"},{"sepalLength":5,"sepalWidth":3.6,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":5.4,"sepalWidth":3.9,"petalLength":1.7,"petalWidth":0.4,"species":"setosa"},{"sepalLength":4.6,"sepalWidth":3.4,"petalLength":1.4,"petalWidth":0.3,"species":"setosa"},{"sepalLength":5,"sepalWidth":3.4,"petalLength":1.5,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.4,"sepalWidth":2.9,"petalLength":1.4,"petalWidth":0.2,"species":"setosa"},{"sepalLength":4.9,"sepalWidth":3.1,"petalLength":1.5,"petalWidth":0.1,"species":"setosa"},{"sepalLength":7,"sepalWidth":3.2,"petalLength":4.7,"petalWidth":1.4,"species":"versicolor"},{"sepalLength":6.4,"sepalWidth":3.2,"petalLength":4.5,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":6.9,"sepalWidth":3.1,"petalLength":4.9,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":5.5,"sepalWidth":2.3,"petalLength":4,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":6.5,"sepalWidth":2.8,"petalLength":4.6,"petalWidth":1.5,"species":"versicolor"},{"sepalLength":5.7,"sepalWidth":2.8,"petalLength":4.5,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":6.3,"sepalWidth":3.3,"petalLength":4.7,"petalWidth":1.6,"species":"versicolor"},{"sepalLength":4.9,"sepalWidth":2.4,"petalLength":3.3,"petalWidth":1,"species":"versicolor"},{"sepalLength":6.6,"sepalWidth":2.9,"petalLength":4.6,"petalWidth":1.3,"species":"versicolor"},{"sepalLength":5.2,"sepalWidth":2.7,"petalLength":3.9,"petalWidth":1.4,"species":"versicolor"},{"sepalLength":6.3,"sepalWidth":3.3,"petalLength":6,"petalWidth":2.5,"species":"virginica"},{"sepalLength":5.8,"sepalWidth":2.7,"petalLength":5.1,"petalWidth":1.9,"species":"virginica"},{"sepalLength":7.1,"sepalWidth":3,"petalLength":5.9,"petalWidth":2.1,"species":"virginica"},{"sepalLength":6.3,"sepalWidth":2.9,"petalLength":5.6,"petalWidth":1.8,"species":"virginica"},{"sepalLength":6.5,"sepalWidth":3,"petalLength":5.8,"petalWidth":2.2,"species":"virginica"},{"sepalLength":7.6,"sepalWidth":3,"petalLength":6.6,"petalWidth":2.1,"species":"virginica"},{"sepalLength":4.9,"sepalWidth":2.5,"petalLength":4.5,"petalWidth":1.7,"species":"virginica"},{"sepalLength":7.3,"sepalWidth":2.9,"petalLength":6.3,"petalWidth":1.8,"species":"virginica"},{"sepalLength":6.7,"sepalWidth":2.5,"petalLength":5.8,"petalWidth":1.8,"species":"virginica"},{"sepalLength":7.2,"sepalWidth":3.6,"petalLength":6.1,"petalWidth":2.5,"species":"virginica"}]

Pretty Printing JSON:

.. code-block:: console

    $ DATA='https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/iris.json'
    $ curl $DATA |python -m json.tool
    [
        {
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "sepalLength": 5.1,
            "sepalWidth": 3.5,
            "species": "setosa"
        },
        {
            "petalLength": 1.4,
            "petalWidth": 0.2,
            "sepalLength": 4.9,
            "sepalWidth": 3,
            "species": "setosa"
        },
    ...

``json.tool`` checks JSON syntax validity:

.. code-block:: console

    $ echo '{"sepalLength":5.1,"sepalWidth":3.5,}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 37 (char 36)


Assignments
-----------
.. literalinclude:: assignments/serialization_json_a.py
    :caption: :download:`Solution <assignments/serialization_json_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/serialization_json_b.py
    :caption: :download:`Solution <assignments/serialization_json_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/serialization_json_c.py
    :caption: :download:`Solution <assignments/serialization_json_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/serialization_json_d.py
    :caption: :download:`Solution <assignments/serialization_json_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/serialization_json_e.py
    :caption: :download:`Solution <assignments/serialization_json_e.py>`
    :end-before: # Solution
