"""
In this Tree, a node have both left and right child or no child
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def is_full(root):
    if root == None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left and root.right:
        return is_full(root.left) and is_full(root.right)
    return False


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.right.left = Node(5)

    if is_full(root):
        print("This is a Full Binary Tree!")
    else:
        print("This is a Not Full Binary Tree!")