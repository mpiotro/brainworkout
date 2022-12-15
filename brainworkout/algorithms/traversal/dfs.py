class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def print_inorder(root):
    if root:
        # First recur on left child
        print_inorder(root.left)

        # then print the data of node
        print(root.value),

        # now recur on right child
        print_inorder(root.right)
