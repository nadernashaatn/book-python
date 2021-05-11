JSON Datetime
=============



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


Assignments
-----------
.. literalinclude:: assignments/json_datetime_a.py
    :caption: :download:`Solution <assignments/json_datetime_a.py>`
    :end-before: # Solution
