from src.sorting.activity_notifications import activity_notification, merge_sort


class TestActivityNotifications:
    def test_case_1(self):
        notifications = activity_notification([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)

        # [2, 2, 3, 3, 4]
        # [2, 3, 3, 4, 6]
        # [2, 3, 4, 6, 8]
        # [2, 3, 4, 6, 8]

        assert notifications == 2

    def test_case_2(self):
        notifications = activity_notification([10, 20, 30, 40, 50], 3)
        assert notifications == 1
