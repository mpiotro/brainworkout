# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def solution(timetable: list):

    if len(timetable) < 2:
        return len(timetable)

    my_dict = {}
    for start, end in timetable:
        if start in my_dict:
            my_dict[start] += 1
        else:
            my_dict[start] = 1

        if end in my_dict:
            my_dict[end] -= 1
        else:
            my_dict[end] = -1

    keys = sorted(my_dict.keys())

    classrooms = 0
    max_classrooms = 0
    for k in keys:
        classrooms += my_dict[k]
        if classrooms > max_classrooms:
            max_classrooms = classrooms

    return max_classrooms


if __name__ == "__main__":
    assert solution([]) == 0
    assert solution([(0, 50)]) == 1
    assert solution([(0, 50), (60, 150)]) == 1
    assert solution([(30, 75), (0, 50), (60, 150)]) == 2
    assert solution([(30, 75), (0, 50), (60, 150), (0, 50)]) == 3
    assert solution([(30, 75), (75, 150), (60, 140), (120, 180), (10, 20)]) == 3
