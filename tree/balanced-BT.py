class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_height(root):
    if root is None:
        return 0
    return max(find_height(root.left), find_height(root.right)) + 1

def is_balanced_tree(root):
    if root is None:
        return True
    left_height = find_height(root.left)
    right_height  = find_height(root.right)
    print("Node {} have Balance Factor of {}".format(root.data, left_height - right_height))
    if abs(left_height - right_height) > 1:
        return False
    return (is_balanced_tree(root.left) and is_balanced_tree(root.right))


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.left = Node(7)
    root.right.left.left = Node(8)
    root.right.left.right = Node(9)

    '''
        2
      /   \
     3     4
   /  \   /
  5    6 7
        / \
       8   9
    '''

    if is_balanced_tree(root):
        print("This is a Balanced Binary Tree!")
    else:
        print("This is Not a Balanced Binary Tree!")
