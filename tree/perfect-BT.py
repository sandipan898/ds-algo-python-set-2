"""
A perfect binary tree is a type of binary tree in which every internal node has exactly 
two child nodes and all the leaf nodes are at the same level.
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def find_height(root):
    if root == None:
        return 0
    return max(find_height(root.left)+1, find_height(root.right)+1)


def is_perfect_tree(root, height, level=0):
    if root == None:
        return True
    if root.left == root.right == None:
        return height == level+1
    if root.left and root.right:
        return is_perfect_tree(root.left, height, level+1) and is_perfect_tree(root.right, height, level+1)
    return False


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.left = Node(7)
    root.right.right = Node(8)

    if is_perfect_tree(root, find_height(root)):
        print("This is a Perfect Binary Tree!")
    else:
        print("This is a Not Perfect Binary Tree!")
