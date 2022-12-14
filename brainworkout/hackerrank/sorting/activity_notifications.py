def activity_notification(expenditure, d):

    n = len(expenditure)

    if d >= n:
        return 0

    if d % 2:
        is_even = False
    else:
        is_even = True

    notifications = 0

    trailing = expenditure[:d]
    merge_sort(trailing)
    median = calculate_median(trailing, is_even)
    if expenditure[d] >= 2 * median:
        notifications = notifications + 1

    for i in range(d + 1, n):
        old_element = expenditure[i - d - 1]
        new_element = expenditure[i - 1]
        trailing.remove(old_element)

        added = False

        for i in range(d - 1):
            if new_element < trailing[i]:
                trailing.insert(i, new_element)
                added = True
                break
        if not added:
            trailing.append(new_element)

        median = calculate_median(trailing, is_even)

        if expenditure[d] >= 2 * median:
            notifications = notifications + 1

    return notifications


def calculate_median(arr: list, is_even: bool):
    if is_even:
        return arr[len(arr) // 2] + arr[len(arr) // 2 + 1] / 2
    else:
        return arr[len(arr) // 2]


def merge_sort(arr):
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

    return arr
