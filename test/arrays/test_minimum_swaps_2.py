from src.arrays.minimum_swaps_2 import minimum_swaps


class TestMinimumSwaps2:
    def test_case_1(self):
        arr = [7, 1, 3, 2, 4, 5, 6]

        result = minimum_swaps(arr)
        assert result == 5

    def test_case_2(self):
        arr = [4, 3, 1, 2]

        result = minimum_swaps(arr)
        assert result == 3

    def test_case_3(self):
        arr = [2, 3, 4, 1, 5]

        result = minimum_swaps(arr)
        assert result == 3
