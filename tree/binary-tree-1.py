class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.node_count = 0
    
    def traverse_preorder(self, root):
        if root == None:
            return
        print(root.data, end=" ")
        if root.left:
            self.traverse_preorder(root.left)
        if root.right:
            self.traverse_preorder(root.right)

    def traverse_inorder(self, root):
        if root:
            if root.left:
                self.traverse_inorder(root.left)
            print(root.data, end=" ")
            if root.right:
                self.traverse_inorder(root.right)
        
    def traverse_postorder(self, root): 
        if root:
            if root.left:
                self.traverse_inorder(root.left)
            if root.right:
                self.traverse_inorder(root.right)
            print(root.data, end=" ")

    def get_height(self, root):
        if root == None:
            return 0
        lheight = 1 + self.get_height(root.left)
        rheight = 1 + self.get_height(root.right)
        return max(lheight, rheight)

    def __str__(self, level=0):
        return str(self.root.data)


tree = BinaryTree()
tree.root = Node(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print("Height", tree.get_height(tree.root))
print("Preorder")
tree.traverse_preorder(tree.root)
print("\nInorder")
tree.traverse_inorder(tree.root)
print("\nPostorder")
tree.traverse_postorder(tree.root)
