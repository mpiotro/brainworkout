# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def solution(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


def calculate_prod(arr):
    product = 1
    for el in arr:
        product *= el
    return product


class TestDailyProblem2:
    def test_case_1(self):
        data = [1, 2, 3, 4, 5]
        result = solution(data)
        assert result == [120, 60, 40, 30, 24]

    def test_case_2(self):
        data = [3, 2, 1]
        result = solution(data)
        assert result == [2, 3, 6]

    def test_case_3(self):
        data = [3, 0, 4]
        result = solution(data)
        assert result == [0, 12, 0]

    def test_case_4(self):
        data = [3, 0, 4, 0]
        result = solution(data)
        assert result == [0, 0, 0, 0]

