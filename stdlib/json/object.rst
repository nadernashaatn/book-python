JSON Object
===========


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


Assignments
-----------
.. literalinclude:: assignments/json_object_a.py
    :caption: :download:`Solution <assignments/json_object_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/json_object_b.py
    :caption: :download:`Solution <assignments/json_object_b.py>`
    :end-before: # Solution
