from src.algorithms.search.mergesort import merge_sort


class TestMergeSort:
    def test_empty_array(self):
        values = []
        merge_sort(values)

        assert values == []

    def test_scenario_1(self):
        values = [14, 7, 9, 11, 2, 31, 15]
        merge_sort(values)

        assert values == [2, 7, 9, 11, 14, 15, 31]

    def test_scenario_2(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        merge_sort(values)

        assert values == [1, 2, 3, 4, 5, 6, 7]

    def test_scenario_3(self):
        values = ["B", "b", "X", "a", "s"]
        merge_sort(values)

        assert values == ["B", "X", "a", "b", "s"]
