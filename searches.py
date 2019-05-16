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
            return rindex + mid    # +1 for zero-indexed
        elif ele > arr[mid]:
            rindex += mid + 1
            arr = arr[mid+1:]
        else:
            arr = arr[:mid]

    return None


if __name__ == '__main__':
    arr = list(range(10))
    ele = 8

    print(binsearch(arr, ele))