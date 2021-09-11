# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array. The array can contain
# duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

def solution(nums: list) -> int:
    if not nums:
        return 1

    for i, num in enumerate(nums):
        while i+1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v-1] = nums[v-1], nums[i]
            if nums[i] == nums[v-1]:
                break

    for i, num in enumerate(nums, 1):
        if i != num:
            return i
    return len(nums) + 1


if __name__ == "__main__":

    result = solution([3, 4, -1, 1])
    print(result)
    assert result == 2

    result = solution([1, 2, 0])
    assert result == 3

    result = solution([4, 1, 6, 3, 2])
    assert result == 5

    result = solution([4, 4, 6, 4, 2, 1])
    assert result == 3
