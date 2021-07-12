class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(data, root=None):
    if root == None:
        return Node(data)
    if data <= root.data:
        print("Inserting {} {} of {}".format(data, 'left', root.data))
        root.left = insert(data, root.left)
    elif data > root.data:
        print("Inserting {} {} of {}".format(data, 'right', root.data))
        root.right = insert(data, root.right)
    return root

def bulk_insert(root, data_list):
    for data in data_list:
        insert(data, root)

def search(root, data):
    if root == None:
        print("{} Not Found".format(data))
        return False
    elif root.data == data:
        print("{} Found".format(data))
        return True
    elif data <= root.data:
        return search(root.left, data)
    elif data > root.data:
        return search(root.right, data)

def get_min(root):
    if root == None:
        return 'None'
    if root.left == None:
        return root
    return get_min(root.left)

def get_max(root):
    if root == None:
        return 'None'
    elif root.right == None:
        return root
    return get_max(root.right)

def get_height(root):
    if root == None:
        return 0
    return max(1 + get_height(root.left), 1 + get_height(root.right)) 
    
def delete(root, data):
    if root == None:
        return root
    if data < root.data:
        root.left = delete(root.left, data)
        # return root
    elif data > root.data:
        root.right = delete(root.right, data)
        # return root
    else:
        if root.left == None:
            print("Deleting {} Without left child or no child".format(root.data))
            temp = root.right
            root = None
            return temp
        if root.right == None:
            print("Deleting {} Without right child".format(root.data))
            temp = root.left
            root = None
            return temp
        else:
            temp = get_min(root.right)
            dummy_data = temp.data
            temp.data = root.data
            root.data = dummy_data
            root.right = delete(root.right, temp.data)
            # return root
    return root
            
def traversal_preorder(root):
    if root:
        print(root.data, end=" ")
        traversal_preorder(root.left)
        traversal_preorder(root.right)

def traversal_inorder(root):
    if root:
        traversal_inorder(root.left)
        print(root.data, end=" ")
        traversal_inorder(root.right)

def traversal_postorder(root):
    if root:
        traversal_postorder(root.left)
        traversal_postorder(root.right)
        print(root.data, end=" ")
        

if __name__ == '__main__':
    root = insert(30)
    insert(10, root)
    insert(20, root)
    insert(50, root)
    insert(30, root)
    insert(40, root)
    insert(25, root)
    insert(5, root)
    traversal_preorder(root)
    print()
    traversal_inorder(root)
    print()
    traversal_postorder(root)
    print()
    print("Height:", get_height(root))
    delete(root, 25)
    delete(root, 50)
    delete(root, 20)
    delete(root, 10)
    traversal_preorder(root)
    print()
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

    bulk_insert(root, [70, 55, 80, 23, 41])
    traversal_preorder(root)
    print()
    search(root, 70)
    search(root, 100)
    print("Min value:", get_min(root).data)
    print("Max Value:", get_max(root).data)
    delete(root, 80)
    traversal_preorder(root)
    print()
