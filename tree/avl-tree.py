class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data
        self.height = 1


class ALVTree:
    def get_height(self, root):
        if root is None:
            # print("0 height")
            return 0
        # print(root.data, root.height)
        return root.height
    
    def get_balance_factor(self, root):
        if root is None:
            # print("0 bf")
            return 0
        # print(root.data, root.height)
        return (self.get_height(root.left) - self.get_height(root.right))

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data > root.data:
            root.right = self.insert(root.right, data)
        else:
            root.left = self.insert(root.left, data)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        bf = self.get_balance_factor(root)
        # print(root.data, root.height, bf)
        
        if bf > 1:
            # Left Left Case
            print(bf, root.data)
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


if __name__ == '__main__':
    myTree = ALVTree()
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
    print("Preorder traversal of the",
        "constructed AVL tree is")
    myTree.traverse_preorder(root)
    print()