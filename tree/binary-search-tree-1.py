class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.node_count = 0
    
    def get_min_node(self, root):
        if root == None:
            return "None"
        if root.left == None:
            return root
        return self.get_min_node(root.left)
    
    def get_max_node(self, root):
        if root == None:
            return "None"
        if root.right == None:
            return root
        return self.get_max_node(root.right)
    
    def bulk_insert(self, data_list):
        for data in data_list:
            self.insert(data)
    
    def insert(self, data):
        self.root = self.insert_node(self.root, data)
        self.node_count += 1
        
    def delete(self, data):
        self.root = self.delete_node(self.root, data)
        self.node_count -= 1

    def insert_node(self, root, data):
        if root == None:    
            return Node(data)
        elif data <= root.data:
            print("Inserting {} {} of {}".format(data, 'left', root.data))
            root.left = self.insert_node(root.left, data)
        elif data > root.data:
            print("Inserting {} {} of {}".format(data, 'right', root.data))
            root.right = self.insert_node(root.right, data)
        return root

    def delete_node(self, root, data):
        if root == None:
            return None
        if data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left == None:
                print("Deleting {} Without left child or no child".format(root.data))
                temp = root.right
                root = None
                return temp
            elif root.right == None:
                print("Deleting {} Without right child".format(root.data))
                temp = root.left
                root = None
                return temp
            else:
                print(root.right.data)
                temp = self.get_min_node(root.right)
                dummy_data = temp.data
                temp.data = root.data
                root.data = dummy_data
                root.right = self.delete_node(root.right, temp.data)
        return root

    def search(self, data):
        return self.search_node(self.root, data)

    def search_node(self, root, data):
        if root == None:
            return None   
        elif root.data == data:
            return root
        elif root.data < data:
            return self.search_node(root.left, data)
        else:
            return self.search_node(root.right, data)

    def get_height(self):
        return self.get_node_height(self.root)
    
    def get_node_height(self, root):
        if root == None:
            return 0
        return max(1+self.get_node_height(root.left), 1+self.get_node_height(root.right))

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
    bst_tree.traverse_preorder(bst_tree.root)
    print()
    bst_tree.traverse_inorder(bst_tree.root)
    print()
    bst_tree.traverse_postorder(bst_tree.root)
    print()
    print("Height:", bst_tree.get_height())
    bst_tree.delete(25) 
    bst_tree.delete(50) 
    bst_tree.delete(20) 
    bst_tree.delete(10) 
    bst_tree.traverse_preorder(bst_tree.root)
    print()
    print("Node Count:", bst_tree.node_count)
    '''
            30
          /    \
        10      50
       / \     /
      5  20   40
           \
           30
          /
         25
    '''
    bst_tree.bulk_insert([70, 55, 80, 23, 41])
    bst_tree.traverse_preorder(bst_tree.root)
    print()
    bst_tree.search(70)
    bst_tree.search(100)
    print("Min value:", bst_tree.get_min_node(bst_tree.root).data)
    print("Max Value:", bst_tree.get_max_node(bst_tree.root).data)
    bst_tree.delete(80)
    bst_tree.traverse_preorder(bst_tree.root)
    print()
    print(bst_tree.root.data)