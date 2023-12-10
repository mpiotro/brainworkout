# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def solution(timetable: list):
    classrooms = 0
    timetable = sorted(timetable)
    return classrooms


if __name__ == "__main__":
    assert solution([]) == 0
    assert solution([(0, 50)]) == 1
    assert solution([(0, 50), (60, 150)]) == 2
    assert solution([(30, 75), (0, 50), (60, 150)]) == 2
    assert solution([(30, 75), (0, 50), (60, 150), (0, 50)]) == 3
    assert solution([(30, 75), (75, 150), (60, 140), (120, 180), (10, 20)]) == 4
