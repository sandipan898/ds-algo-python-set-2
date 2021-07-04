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
        self.insert_node(self.root, data)
        
    def insert_node(self, root, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            self.node_count += 1    
            return
        elif data <= self.root.data:
            self.root.left = self.insert_node(self.root.left, data)
        elif data > self.root.data:
            self.root.right = self.insert_node(self.root.left, data)
        self.node_count += 1

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


def insert(root, data):
    new_node = Node(data)
    if root == None:
        root = new_node
        print(root.data)
        return root
    if data <= root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.left, data)
    return root


if __name__ == '__main__':
    bst_tree = BST()
    bst_tree.root = insert(bst_tree.root, 30)
    insert(bst_tree.root, 10)
    insert(bst_tree.root, 20)
    insert(bst_tree.root, 50)
    insert(bst_tree.root, 30)
    insert(bst_tree.root, 40)
    insert(bst_tree.root, 25)
    insert(bst_tree.root, 5)
    print(bst_tree.root.data)
    bst_tree.traverse_preorder(bst_tree.root)
    print(bst_tree.node_count)