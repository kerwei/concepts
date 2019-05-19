from operator import itemgetter
import random


# Binary search
def binsearch(arr, ele):
    if not arr:
        return None
    elif len(arr) == 1:
        return arr[0][0] if ele == arr[0][1] else None
    else:
        arr_tuple = [(i, a) for i, a in enumerate(arr)]
        arr = sorted(arr_tuple, key=itemgetter(1))

    while len(arr) > 0:
        mid = len(arr)//2
        if arr[mid][1] == ele:
            return arr[mid][0]
        elif ele > arr[mid][1]:
            arr = arr[mid+1:]
        else:
            arr = arr[:mid]

    return None

# Recursive version of the binary search
def rebinsearch(arr, ele, ridx=0):
    if not arr:
        return None
    elif len(arr) == 1:
        return ridx if ele == arr[0] else None
    else:
        arr = sorted(arr)
    
    mid = len(arr)//2
    if arr[mid] == ele:
        return ridx + mid
    elif arr[mid] < ele:
        return rebinsearch(arr[mid+1:], ele, ridx + mid + 1)
    else:
        return rebinsearch(arr[:mid], ele, ridx)


if __name__ == '__main__':
    random.seed(a=1)
    arr = list(random.choices(range(20), k=10))
    print(arr)
    ele = 8

    print(binsearch(arr, ele))