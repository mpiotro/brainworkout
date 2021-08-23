# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    if root is None:
        return '#'

    return f'{root.val} {serialize(root.left)} {serialize(root.right)}'


def deserialize(s: str):
    values = iter(s.split())

    def helper():
        v = next(values)
        if v == '#':
            return None
        n = Node(v)
        n.left = helper()
        n.right = helper()
        return n
    return helper()


if __name__ == "__main__":
    # node = Node('root', Node('left', Node('left.left')), Node('right'))
    node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))

    result = deserialize(serialize(node))

    assert deserialize(serialize(node)).left.left.val == 'left.left'
