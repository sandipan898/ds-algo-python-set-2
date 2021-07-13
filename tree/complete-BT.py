"""
A complete binary tree is a binary tree in which all the levels are completely 
filled except possibly the lowest one, which is filled from the left.
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + count_nodes(root.right))


def is_complete_tree(root, index, node_count):
    if root is None:
        return True
    if index >= node_count:
        return False
    return (is_complete_tree(root.left, 2*index+1, node_count) and is_complete_tree(root.right, 2*index+2, node_count))


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    # root.left.right = Node(6)
    root.right.left = Node(7)
    root.right.right = Node(8)

    if is_complete_tree(root, 0, count_nodes(root)):
        print("This is a Complete Binary Tree!")
    else:
        print("This is Not a Complete Binary Tree!")