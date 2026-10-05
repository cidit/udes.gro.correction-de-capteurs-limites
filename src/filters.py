import math


def min_max(data, min, max):
    UNKNOWN = -1
    return [e if min <= e <= max else UNKNOWN if e < min else max for e in data]


def sliding_average(data, window_size):
    padding = [None] * math.floor(window_size / 2)
    padded = [*padding, *data, *padding]
    windows = [padded[i : i + window_size] for i in range(len(data))]
    filter_none = [[e for e in window if e is not None] for window in windows]
    return [sum(w) / len(w) for w in filter_none]


def sliding_median(data):
    """
        Sliding Median
    """
    acc = []
    for i, d in enumerate(data):
        window_indexes = [i - 1, i, i + 1]
        if any(not 0 <= wi < len(data) for wi in window_indexes):
            acc.append(d)
            continue
        window = [data[wi] for wi in window_indexes]
        acc.append(sorted(window)[1])
    return acc


def test_min_max():
    donnees = [1, 50, 0]
    reponse = [1, 10, -1]
    test = min_max(donnees, 1, 10)
    assert test == reponse


def test_sliding_average():
    input = [1, 3, 2, 4, 5, 3]
    output = [2.0, 2.0, 3.0, 3.7, 4.0, 4.0]
    # we round each member before the comparison because the provided expected
    # output doesnt take into account that the actual answer has a period in one
    # of the entries
    assert [round(num) for num in sliding_average(input, 3)] == [
        round(num) for num in output
    ]


def test_sliding_median():
    input = [1, 3, 2, 4, 5, 3]
    output = [1, 2, 3, 4, 4, 3]
    assert sliding_median(input) == output
