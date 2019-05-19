# Binary search
def binsearch(arr, ele):
    if not arr:
        return None
    elif len(arr) == 1:
        return 0 if ele == arr[0] else None
    else:
        arr = sorted(arr)

    rindex = 0

    while len(arr) > 0:
        mid = len(arr)//2
        if arr[mid] == ele:
            return rindex + mid
        elif ele > arr[mid]:
            rindex += mid + 1    # +1 for zero-indexed
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
    arr = list(range(10))
    ele = 8

    print(rebinsearch(arr, ele))