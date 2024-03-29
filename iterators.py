import itertools
import random

from collections import deque
from operator import itemgetter


"""
Simple class to count from zero to N
"""
from typing import Any, Iterable, Iterator, List, Mapping, TypedDict


class count_to(object):
    def __init__(self, nber):
        if nber < 0:
            raise ValueError('count_to argument must be a positive integer')

        self.nber = nber

    def __iter__(self):
        return count_to_iter(self.nber)


class count_to_iter(object):
    def __init__(self, nber):
        self.stopat = nber
        self.current_nber = 0

    def __next__(self):
        if self.current_nber > self.stopat:
            raise StopIteration

        self.current_nber += 1

        return self.current_nber - 1


class DataRow(TypedDict):
    color: str
    item: str
    price: float
    unit: int


def aggregate_dict_by_key(data: Iterator[DataRow]) -> List[DataRow]:
    """
    Given a sequence of DataRow, compute the aggregates
    """
    key = itemgetter('color', 'item')
    grouped = itertools.groupby(sorted(data, key=key), key=key)

    results = []
    for (color, item), data in grouped:
        thisgrp = list(data)

        sumprice = sum(map(itemgetter('price'), thisgrp))
        sumunuit = sum(map(itemgetter('unit'), thisgrp))

        results += [DataRow(
            color = color,
            item = item,
            price = sumprice,
            unit = sumunuit
        )]

    return results


def moving_average(iterable: Iterable[int], n: int=3) -> Iterator[float]:
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    breakpoint()
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


if __name__ == '__main__':
    # for x in count_to(-1):
    #     print(x)

    length = 10
    # inputdata = (
    #     DataRow(
    #         color = color,
    #         item = item,
    #         price = price,
    #         unit = unit
    #     ) for color, item, price, unit in zip(
    #         itertools.cycle(['blue', 'red', 'yellow']),
    #         itertools.cycle(['circle', 'square']),
    #         (random.uniform(1.0, 100.0) for i in range(length)),
    #         (random.randrange(1, 5) for i in range(length)),
    # ))

    # print(aggregate_dict_by_key(inputdata))

    nbrs = [random.randrange(1,101) for _ in range(length)]
    print(nbrs)

    print([x for x in moving_average(nbrs)])