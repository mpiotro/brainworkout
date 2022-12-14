def minimum_swaps(arr):
    swaps = 0
    n = len(arr)

    for i in range(n):
        arr[i] = arr[i] - 1

    lookup = [0] * n
    for pos, val in enumerate(arr):
        lookup[val] = pos

    for i in range(n):
        if arr[i] != i:
            pos_ith_elem = lookup[i]
            arr[i], arr[pos_ith_elem] = arr[pos_ith_elem], arr[i]
            lookup[i] = i
            lookup[arr[pos_ith_elem]] = pos_ith_elem
            swaps = swaps + 1

    return swaps
