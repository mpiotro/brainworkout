# An unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


class Node:
    def __init__(self, value: int, left: "Node" = None, right: "Node" = None):
        self.value = value
        self.right = right
        self.left = left


def unival_helper(root: Node):
    if root is None:
        return True, 0

    is_left_unival, left_count = unival_helper(root.left)
    is_right_unival, right_count = unival_helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.left.value != root.value:
            return False, total_count
        if root.right is not None and root.right.value != root.value:
            return False, total_count
        return True, total_count + 1
    return False, total_count


def count_unival_trees(root: Node):
    _, count = unival_helper(root)
    return count


if __name__ == "__main__":

    #    0
    #   / \
    #  1   0
    #     / \
    #    1   0
    #   / \
    #  1   1

    node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

    print(count_unival_trees(node))

    #    1
    #   / \
    #  1   1
    #     / \
    #    1   1
    #   / \   \
    #  1   1   1

    node = Node(1, Node(1), Node(1, Node(1, Node(1), Node(1)), Node(1, None, Node(1))))

    print(count_unival_trees(node))

    #    1
    #   / \
    #  0   1
    #     / \
    #    1   1
    #   / \   \
    #  1   1   0

    node = Node(1, Node(0), Node(1, Node(1, Node(1), Node(1)), Node(1, None, Node(0))))

    print(count_unival_trees(node))
