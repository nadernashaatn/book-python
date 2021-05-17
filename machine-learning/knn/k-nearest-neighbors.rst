K Nearest Neighbors
===================

.. todo:: Zrobić aby wykorzystywało szablon ``_template.rst``

Jak działa algorytm "K najbliższych sąsiadów"
-------------------------------------------------------------------------------
Algorytm polega na:

#. porównaniu wartości zmiennych objaśniających dla obserwacji :math:`C` z wartościami tych zmiennych dla każdej obserwacji w zbiorze uczącym.

#. wyborze :math:`k` (ustalona z góry liczba) najbliższych do :math:`C` obserwacji ze zbioru uczącego.

#. uśrednieniu wartości zmiennej objaśnianej dla wybranych obserwacji, w wyniku czego uzyskujemy prognozę.

.. figure:: img/k-nearest-neighbors-territory.png

    Predykcja obszaru przynależności w algorytmie "K najbliższych sąsiadów".


Przykład praktyczny
-------------------------------------------------------------------------------

Jak to działa na przykładzie Iris
---------------------------------
#. Mamy zbiór 150 obserwacji Iris
#. Wyobraź sobie, że mamy określić nową Iris, która jeszcze nie została zaobserwowana i opisana.
#. Wybieramy wartość :math:`k`
#. Poszukujemy :math:`k` obserwacji, które są najbliższe nieznanemu gatunkowi Iris.
#. Użyj najczęściej pojawiającej się wartości z ":math:`k` najbliższych sąsiadów" jako wartość dla nieznanego Iris.

    * tzn. jeżeli np. dla :math:`k=5` (czyli wśród 5 najbliższych Iris) było 3 Iris Setosa, i po jednym z innych gatunków
    * to naszemu nieznanemu gatunkowi przypiszemy Iris Setosa.

#. Najczęściej stosuje się algorytm Euklidesa do wyznaczania odległości, ale można również i inne algorytmy.


Wykorzystanie ``sklearn.neighbors.KNeighborsClassifier``
--------------------------------------------------------

.. code-block:: python

    from sklearn import datasets
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier


    iris = datasets.load_iris()

    # Split dataset into test and training set in half
    features_train, features_test, labels_train, labels_test = train_test_split(iris.data, iris.target, test_size=0.25)

    # Create classifier
    model = KNeighborsClassifier()

    # Train classifier using training data
    model.fit(features_train, labels_train)

    # Predict
    predictions = model.predict(features_test)

    # How accurate was classifier on testing set
    result = accuracy_score(labels_test, predictions)
    print(result)
    # Output: 0.947368421053

Because of some variation for each run, it might give different results.

Własna implementacja
--------------------
.. code-block:: python

    from scipy.spatial import distance
    from sklearn import datasets
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split


    class NearestNeighborClassifier:
        def fit(self, features, labels):
            self.features_train = features
            self.labels_train = labels

        def predict(self, features_test):
            predictions = []

            for row in features_test:
                label = self.closest(row)
                predictions.append(label)

            return predictions

        def closest(self, row):
            best_dist = distance.euclidean(row, self.features_train[0])
            best_index = 0

            for i in range(0, len(self.features_train)):
                dist = distance.euclidean(row, self.features_train[i])
                if dist < best_dist:
                    best_dist = dist
                    best_index = i

            return self.labels_train[best_index]


    iris = datasets.load_iris()

    # Split dataset into test and training set in half
    features_train, features_test, labels_train, labels_test = train_test_split(iris.data, iris.target, test_size=0.5)

    # Create classifier
    model = NearestNeighborClassifier()

    # Train classifier using training data
    model.fit(features_train, labels_train)

    # Predict
    predictions = model.predict(features_test)

    # How accurate was classifier on testing set
    result = accuracy_score(labels_test, predictions)
    print(result)
    # Output: 0.96


Because of some variation for each run, it might give different results.


Określanie przynależności do zbioru
-------------------------------------------------------------------------------

.. figure:: img/k-nearest-neighbors-membership.png

    Przynależność do zbioru

Wyznaczanie odległości
-------------------------------------------------------------------------------

.. figure:: img/k-nearest-neighbors-euclidean-distance.png

    Wyliczanie odległości w celu oszacowania przynależności do zbioru. Zwróć uwagę, że bez względu na ilość wymiarów wzór się niewiele różni.

Zalety i wady
-------------------------------------------------------------------------------

Zalety
------
* Relatywnie prosty
* Dobrze działa dla niektórych problemów

Wady
----
* Wolny i zasobożerny (musi iterować dla każdej predykcji)
* Brak możliwości ważenia features


Assignments
-------------------------------------------------------------------------------
.. todo:: Convert assignments to literalinclude

Pima Indians Diabetes problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Assignment: Pima Indians Diabetes problem
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Dla Pima Indians Diabetes wykonaj analizę algorytmem KNN z biblioteki ``sklearn``.
    2. Uruchom doctesty - wszystkie muszą się powieść

Płeć
^^^^
* Assignment: Płeć
* Complexity: easy
* Lines of code: 15 lines
* Time: 13 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Napisz własną implementacje k Nearest Neighbors, która dla danych:

        .. csv-table::
            :header: "Gender", "Height", "Weight", "Foot Size"

            male,6.00,180,12
            male,5.92,190,11
            male,5.58,170,12
            male,5.92,165,10
            female,5.00,100,6
            female,5.50,150,8
            female,5.42,130,7
            female,5.75,150,9

    2. Odpowie na pytanie jaką płeć ma osoba o parametrach:

        a. Height: 6
        b. Weight: 130
        c. Foot Size: 8

    3. Jaki jest najlepszy parametr :math:`k` dla tego zadania?
    4. Która z cech ma największy wpływ?
    5. Czy algorytm lepiej działa z:

        a. normalizacją i skalowaniem?
        b. bez normalizacji i skalowania?
        c. tylko z normalizacją?
        d. tylko skalowaniem?

    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * ``preprocessing.LabelEncoder()``
    * ``ExtraTreesClassifier()`` i ``.feature_importances_``
    * ``preprocessing.normalize(features)``
    * ``preprocessing.scale(features)``
