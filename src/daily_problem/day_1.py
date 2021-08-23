# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


[3, 7, 10, 15]


def solution(numbers, k):
    merge_sort(numbers)

    left_index = 0
    right_index = len(numbers) - 1

    while left_index != right_index:
        s = numbers[left_index] + numbers[right_index]
        if s < k:
            left_index += 1
        elif s > k:
            right_index -= 1
        else:
            return True

    return False


def solution_2(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False


def merge_sort(arr: list):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":

    result = solution_2([10, 15, 3, 7], 17)
    assert result is True

    result = solution_2([3, 1, 11, 5, 1, 7], 13)
    assert result is False

    result = solution_2([1, 1, 1, 1], 2)
    assert result is True


