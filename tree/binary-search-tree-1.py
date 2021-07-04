class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.node_count = 0
    
    def insert(self, data):
        self.root = self.insert_node(self.root, data)
        
    def insert_node(self, root, data):
        if root == None:
            self.node_count += 1    
            return Node(data)
        elif data <= root.data:
            print("Inserting {} {} of {}".format(data, 'left', root.data))
            root.left = self.insert_node(root.left, data)
        elif data > root.data:
            print("Inserting {} {} of {}".format(data, 'right', root.data))
            root.right = self.insert_node(root.left, data)
        return root

    def traverse_preorder(self, root):
        if root is not None:
            print(root.data, end=' ')
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)
     
    def traverse_inorder(self, root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data, end=' ')
            self.traverse_inorder(root.right)
    
    def traverse_postorder(self, root):
        if root is not None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data, end=' ')


# def insert(root, data):
#     new_node = Node(data)
#     if root == None:
#         root = new_node
#         print(root.data)
#         return root
#     if data <= root.data:
#         root.left = insert(root.left, data)
#     elif data > root.data:
#         root.right = insert(root.left, data)
#     return root


if __name__ == '__main__':
    bst_tree = BST()
    bst_tree.insert(30)
    bst_tree.insert(10)
    bst_tree.insert(20)
    bst_tree.insert(50)
    bst_tree.insert(30)
    bst_tree.insert(40)
    bst_tree.insert(25)
    bst_tree.insert(5)
    print(bst_tree.root.data)
    bst_tree.traverse_preorder(bst_tree.root)
    print(bst_tree.node_count)
    