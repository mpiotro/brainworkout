from src.arrays.left_rotation import rot_left


class TestLeftRotation:
    def test_case_1(self):
        a = [1, 2, 3, 4, 5]
        d = 2

        result = rot_left(a, d)
        assert result == [3, 4, 5, 1, 2]

    def test_case_2(self):
        a = [1, 2, 3, 4, 5]
        d = 0

        result = rot_left(a, d)
        assert result == [1, 2, 3, 4, 5]

    def test_case_3(self):
        a = [1, 2, 3, 4, 5]
        d = 23

        result = rot_left(a, d)
        assert result == [4, 5, 1, 2, 3]

    def test_case_4(self):
        a = [1]
        d = 23

        result = rot_left(a, d)
        assert result == [1]

    def test_case_4(self):
        a = [1, 1, 1, 1]
        d = 23

        result = rot_left(a, d)
        assert result == [1, 1, 1, 1]

    def test_case_5(self):
        a = [-1, 2, 2, 3, 4, 5, 6]
        d = 11

        result = rot_left(a, d)
        assert result == [4, 5, 6, -1, 2, 2, 3]
