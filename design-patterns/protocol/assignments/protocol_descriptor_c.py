"""
* Assignment: Protocol Descriptor Inheritance
* Complexity: medium
* Lines of code: 25 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Define class `GeographicCoordinate`
    3. Use descriptors to check value boundaries
    5. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj klasę `GeographicCoordinate`
    3. Użyj deskryptory do sprawdzania wartości brzegowych
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> place1 = GeographicCoordinate(50, 120, 8000)
    >>> place1
    Latitude: 50, Longitude: 120, Elevation: 8000

    >>> place2 = GeographicCoordinate(22, 33, 44)
    >>> place2
    Latitude: 22, Longitude: 33, Elevation: 44

    >>> place1.latitude = 1
    >>> place1.longitude = 2
    >>> place1
    Latitude: 1, Longitude: 2, Elevation: 8000

    >>> place2
    Latitude: 22, Longitude: 33, Elevation: 44

    >>> GeographicCoordinate(90, 0, 0)
    Latitude: 90, Longitude: 0, Elevation: 0
    >>> GeographicCoordinate(-90, 0, 0)
    Latitude: -90, Longitude: 0, Elevation: 0
    >>> GeographicCoordinate(0, +180, 0)
    Latitude: 0, Longitude: 180, Elevation: 0
    >>> GeographicCoordinate(0, -180, 0)
    Latitude: 0, Longitude: -180, Elevation: 0
    >>> GeographicCoordinate(0, 0, +8848)
    Latitude: 0, Longitude: 0, Elevation: 8848
    >>> GeographicCoordinate(0, 0, -10994)
    Latitude: 0, Longitude: 0, Elevation: -10994

    >>> GeographicCoordinate(-91, 0, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(+91, 0, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, -181, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, +181, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, 0, -10995)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, 0, +8849)
    Traceback (most recent call last):
    ValueError: Out of bounds
"""


# Given
class GeographicCoordinate:
    def __str__(self):
        return f'Latitude: {self.latitude},' +\
               f'Longitude: {self.longitude},' +\
               f'Elevation: {self.elevation}'

    def __repr__(self):
        return self.__str__()


"""
latitude - min: -90.0, max: 90.0
longitude - min: -180.0, max: 180.0
elevation - min: -10994.0, max: 8848.0
"""


# Solution
from abc import ABCMeta, abstractproperty


class GEOProperty(metaclass=ABCMeta):
    _fieldname: str

    @abstractproperty
    def MIN(self) -> float:
        pass

    @abstractproperty
    def MAX(self) -> float:
        pass

    def __set_name__(self, owner, attrname):
        self._fieldname = f'__{attrname}'

    def __set__(self, instance, newvalue):
        if self.MIN <= newvalue <= self.MAX:
            setattr(instance, self._fieldname, newvalue)
        else:
            raise ValueError('Out of bounds')

    def __get__(self, instance, *args):
        return getattr(instance, self._fieldname)


class Latitude(GEOProperty):
    MIN: float = -90.0
    MAX: float = +90.0


class Longitude(GEOProperty):
    MIN: float = -180.0
    MAX: float = +180.0


class Elevation(GEOProperty):
    MIN: float = -10994.0
    MAX: float = +8848.0


class GeographicCoordinate:
    latitude = Latitude()
    longitude = Longitude()
    elevation = Elevation()
    __latitude: float
    __longitude: float
    __elevation: float

    def __init__(self, latitude, longitude, elevation):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def __str__(self):
        return f'Latitude: {self.latitude},' +\
               f'Longitude: {self.longitude},' +\
               f'Elevation: {self.elevation}'

    def __repr__(self):
        return self.__str__()
