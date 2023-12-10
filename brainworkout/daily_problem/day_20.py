# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


class Node(object):
    def __init__(self, value: int, next_node: "Node" = None):
        self.next_node = next_node
        self.value = value


def solution(A: list, B: list):
    A_log = {}
    B_log = {}

    while A or B:
        if A:
            value = A.pop(0)
            if value not in A_log:
                A_log[value] = True

            if value in B_log:
                return value

        if B:
            value = B.pop(0)
            if value not in B_log:
                B_log[value] = True
            if value in A_log:
                return value

    return None


if __name__ == "__main__":
    A = [3, 7, 8, 10]
    B = [99, 1, 8, 10]

    print(solution(A, B))

    A = [12, 90, 19, 20, 21, 103, 233, 1, 4]
    B = [99, 1, 8, 10]

    print(solution(A, B))
