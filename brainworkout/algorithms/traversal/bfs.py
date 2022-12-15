class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree(root):
    if root is None:
        return

    queue = [root]

    while len(queue) > 0:

        print(queue[0].value)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
