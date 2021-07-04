from typing import List


def rot_left(a: List[int], d: int):

    if d >= len(a):
        d = d % len(a)

    result = []

    for i in range(d, len(a)):
        result.append(a[i])

    for i in range(d):
        result.append(a[i])

    return result
