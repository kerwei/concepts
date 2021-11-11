import itertools
import random

from typing import List


def re_merge_sort(seq: List) -> List:
    """
    Sorting by merge sort
    """
    n = len(seq)
    if n == 1:
        return seq
    elif n == 2:
        left,  right = seq

        return [left, right] if left <= right else [right, left]

    left = list(itertools.chain(re_merge_sort(seq[:(n//2 + 1)])))
    right = list(itertools.chain(re_merge_sort(seq[(n//2 + 1):])))

    res = [0] * n
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        res[k:] = right[j:]
    else:
        res[k:] = left[i:]

    return res


if __name__ == '__main__':
    length = 10
    seq = [random.randrange(1, 100) for _ in range(length)]
    print(seq)

    print(re_merge_sort(seq))