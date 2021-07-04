from src.arrays.array_manipulation import array_manipulation


class TestArrayManipulation:
    def test_case_1(self):
        n = 10
        queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

        result = array_manipulation(n, queries)
        assert result == 10

    def test_case_2(self):
        n = 5
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

        result = array_manipulation(n, queries)
        assert result == 200

    def test_case_3(self):
        n = 20
        queries = [[1, 20, 10], [1, 5, 50], [5, 10, 100], [10, 19, 25], [20, 20, 500]]

        result = array_manipulation(n, queries)
        assert result == 510
