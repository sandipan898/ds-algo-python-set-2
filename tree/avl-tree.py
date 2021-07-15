import sys 

class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data
        self.height = 1


class AVLTree:
    def get_height(self, root):
        if root is None:
            return 0
        return root.height
    
    def get_balance_factor(self, root):
        if root is None:
            return 0
        return (self.get_height(root.left) - self.get_height(root.right))
    
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data > root.data:
            root.right = self.insert(root.right, data)
        else:
            root.left = self.insert(root.left, data)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        bf = self.get_balance_factor(root)
        
        if bf > 1:
            # Left Left Case
            if data < root.left.data:
                return self.rotate_right(root)
            
            # Left Right Case
            elif data > root.left.data:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        
        if bf < -1:
            # Right Left Rotate
            if data < root.right.data:
                root.right =  self.rotate_right(root.right)
                return self.rotate_left(root)
            
            # Right Right Case
            elif data > root.right.data:
                return self.rotate_left(root)
        return root

    def delete(self, root, data):
        if root is None:
            return None
        print(root.data)
        if data > root.data:
            root.right = self.delete(root.right, data)
        elif data < root.data:
            root.left = self.delete(root.left, data)
        
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

        print(root.data)

        min_node = self.get_min_value_node(root.right)
        root.data = min_node.data
        root.right = self.delete(root.right, min_node.data)
        print(root.data)

        if root is None:
            return None

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        bf = self.get_balance_factor(root)
        
        print(bf, root.data)
        if bf > 1:
            left_bf = self.get_balance_factor(root.left)
            # Left Left Case
            if self.get_balance_factor(root.left) >= 0:
                return self.rotate_right(root)
            # Left Right Case
            if self.get_balance_factor(root.left) < 0:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if bf < -1:
            right_bf = self.get_balance_factor(root.right)
            # Right Left Case
            if self.get_balance_factor(root.right) >= 0:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            # Right Right Case
            if self.get_balance_factor(root.right) < 0:
                return self.rotate_left(root)

        return root

    def rotate_left(self, root):
        temp = root.right
        T = temp.left
        temp.left = root
        root.right = T

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))
        return temp

    def rotate_right(self, root):
        temp = root.left
        T = temp.right
        temp.right = root
        root.left = T

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))
        return temp

    def traverse_preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ") 
        self.traverse_preorder(root.left)
        self.traverse_preorder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.data)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

if __name__ == '__main__':
    myTree = AVLTree()
    root = None
    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)
    
    """The constructed AVL Tree would be
             30
            /  \
          20   40
         /  \     \
        10  25    50

            10
              \
               20
                 \
                 30
    """
    
    # Preorder Traversal
    print("Preorder traversal of the constructed AVL tree is")
    myTree.traverse_preorder(root)
    print()

    myTree = AVLTree()
    root = None
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    
    for num in nums:
        root = myTree.insert(root, num)
    
    print("Preorder Traversal after insertion -")
    myTree.traverse_preorder(root)
    print()
    # myTree.printHelper(root, "", True)
    
    root = myTree.delete(root, 10)
    
    print("Preorder Traversal after deletion -")
    myTree.traverse_preorder(root)
    print()
    # myTree.printHelper(root, "", True)