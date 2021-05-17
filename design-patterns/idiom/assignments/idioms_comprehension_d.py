"""
* Assignment: Idioms Comprehension Train/Test
* Complexity: medium
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Using List Comprehension split `DATA` into:
        a. `features_train: list[tuple]` - 60% of first features in `DATA`
        b. `features_test: list[tuple]` - 40% of last features in `DATA`
        c. `labels_train: list[str]` - 60% of first labels in `DATA`
        d. `labels_test: list[str]` - 40% of last labels in `DATA`
    2. In order to do so, calculate pivot point:
        a. length of `DATA` times given percent (60% = 0.6)
        b. remember, that slice indicies must be `int`, not `float`
        c. for example: if dataset has 10 rows, then 6 rows will be for training, and 4 rows for test
    3. Run doctests - all must succeed

Polish:
    1. Używając List Comprehension podziel `DATA` na:
        a. `features_train: list[tuple]` - 60% pierwszych features w `DATA`
        b. `features_test: list[tuple]` - 40% ostatnich features w `DATA`
        c. `labels_train: list[str]` - 60% pierwszych labels w `DATA`
        d. `labels_test: list[str]` - 40% ostatnich labels w `DATA`
    2. Aby to zrobić, wylicz punkt podziału:
        a. długość `DATA` razy zadany procent (60% = 0.6)
        b. pamiętaj, że indeksy slice muszą być `int` a nie `float`
        c. na przykład: if zbiór danych ma 10 wierszy, to 6 wierszy będzie do treningu, a 4 do testów
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(features_train) is list
    >>> assert type(features_test) is list
    >>> assert type(labels_train) is list
    >>> assert type(labels_test) is list
    >>> assert all(type(x) is tuple for x in features_train), 'features_train: expected type list[tuple]'
    >>> assert all(type(x) is tuple for x in features_test), 'features_test: expected type list[tuple]'
    >>> assert all(type(x) is str for x in labels_train)
    >>> assert all(type(x) is str for x in labels_test)
    >>> features_train  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2)]
    >>> features_test  # doctest: +NORMALIZE_WHITESPACE
    [(7.0, 3.2, 4.7, 1.4),
     (7.6, 3.0, 6.6, 2.1),
     (4.9, 3.0, 1.4, 0.2),
     (4.9, 2.5, 4.5, 1.7)]
    >>> labels_train
    ['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']
    >>> labels_test
    ['versicolor', 'virginica', 'setosa', 'virginica']
"""

DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.9, 2.5, 4.5, 1.7, 'virginica')]

features_train: list
features_test: list
labels_train: list
labels_test: list


# Solution
RATIO = 0.6
header, *data = DATA
pivot = int(len(data) * RATIO)
features_train = [tuple(X) for *X, y in data[:pivot]]
features_test = [tuple(X) for *X, y in data[pivot:]]
labels_train = [y for *X, y in data[:pivot]]
labels_test = [y for *X, y in data[pivot:]]

## Alternative Solution
# features = [tuple(measurements) for *measurements,_ in data]
# features_train = features[:pivot]
# features_test = features[pivot:]
#
# labels = [species for *_,species in data]
# labels_train = labels[:pivot]
# labels_test = labels[pivot:]


## Performance comparison
# In[1]: DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
#   ...:         (5.8, 2.7, 5.1, 1.9, 'virginica'),
#   ...:         (5.1, 3.5, 1.4, 0.2, 'setosa'),
#   ...:         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
#   ...:         (6.3, 2.9, 5.6, 1.8, 'virginica'),
#   ...:         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
#   ...:         (4.7, 3.2, 1.3, 0.2, 'setosa'),
#   ...:         (7.0, 3.2, 4.7, 1.4, 'versicolor'),
#   ...:         (7.6, 3.0, 6.6, 2.1, 'virginica'),
#   ...:         (4.9, 3.0, 1.4, 0.2, 'setosa'),
#   ...:         (4.9, 2.5, 4.5, 1.7, 'virginica')]
# In[2]:
# In[3]: RATIO = 0.6
# In[4]: header, *data = DATA
# In[5]: pivot = int(len(data) * RATIO)
# In[6]:
# In[7]: %%timeit -r 10 -n 10_000
#   ...: features = [tuple(X) for *X,y in data]
#   ...: features_train = features[:pivot]
#   ...: features_test = features[pivot:]
#   ...: labels = [y for *X,y in data]
#   ...: labels_train = labels[:pivot]
#   ...: labels_test = labels[pivot:]
# 5.59 µs ± 607 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# In[8]:
# In[9]: %%timeit -r 10 -n 10_000
#   ...: features_train: list = [tuple(X) for *X,y in data[:pivot]]
#   ...: features_test: list = [tuple(X) for *X,y in data[pivot:]]
#   ...: labels_train: list = [y for *X,y in data[:pivot]]
#   ...: labels_test: list = [y for *X,y in data[pivot:]]
# 5.81 µs ± 634 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
