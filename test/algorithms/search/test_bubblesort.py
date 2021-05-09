from src.algorithms.search.bubblesort import bubble_sort


class TestBubbleSort:
    def test_bubble_sort_scenario_1(self):
        values = [14, 7, 9, 11, 2, 31, 15]
        result = bubble_sort(values)

        assert result == [2, 7, 9, 11, 14, 15, 31]
