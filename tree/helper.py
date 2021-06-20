    # def inirialize(self, data):
    #     new_node = Node(data)
    #     self.root = new_node
    #     return self.root
        
    # def insert_left(self, root, data):
    #     print(root)
    #     new_node = Node(data)
    #     if root == None:
    #         print("Insert as Root", data)
    #         root = new_node
    #         self.node_count += 1
    #         return True

    #     if root.left:
    #         print("Insert {} as Left of{}".format(data, self.root.data))
    #         root.left = new_node
    #     elif root.right:
    #         print("Insert {} as Right of{}".format(data, self.root.data))
    #         root.right = new_node
    #     else:
    #         self.insert_left(root.left, data)
    #     self.node_count += 1
    #     return True

    # def insert_left(self, root, data):
    #     new_node = Node(data)
    #     if root == None:
    #         print("Insert as Root", data)
    #         root = new_node
    #         self.node_count += 1
    #         return True

    #     if root.left:
    #         print("Insert {} as Left of{}".format(data, self.root.data))
    #         root.left = new_node
    #     elif root.right:
    #         print("Insert {} as Right of{}".format(data, self.root.data))
    #         root.right = new_node
    #     else:
    #         self.insert_left(root.left, data)
    #     self.node_count += 1
    #     return True

    # def insert_right(self, root, data):
    #     new_node = Node(data)
    #     if self.root == None:
    #         print("Insert as Root", data)
    #         root = new_node
    #         self.node_count += 1
    #         return True

    #     if self.root.right:
    #         print("Insert {} as Right of{}".format(data, self.root.data))
    #         self.root.left = new_node
    #     elif self.root.left:
    #         print("Insert {} as Left of{}".format(data, self.root.data))
    #         self.root.left = new_node
    #     else:
    #         self.insert_right(root.right, data)
    #     self.node_count += 1
    #     return True

    # def insert(self, root):
    #     data = input("Enter data(-1 to put NULL): ")
    #     new_node = Node(data)
        

# def insert_left(BnTree, data):
#     print(BnTree)
#     new_node = Node(data)
#     if BnTree.root == None:
#         print("Insert as Root", data)
#         BnTree.root = new_node
#         BnTree.node_count += 1
#         return True

#     if BnTree.root.left:
#         print("Insert {} as Left of{}".format(data, BnTree.root.data))
#         root.left = new_node
#     elif BnTree.root.right:
#         print("Insert {} as Right of{}".format(data, BnTree.root.data))
#         root.right = new_node
#     else:
#         insert_left(BnTree.root.left, data)
#     BnTree.node_count += 1
#     return True



# def create(self):
#     data = input("Enter data (-1 to NULL): ")
#     if (data == str(-1)):
#         return None 
#     new_node = Node(data)
#     self.root = new_node
#     # if self.root == None:
#     #     self.root = new_node
        
#     print("Left child of", data)
#     self.root.left = self.create()

#     print("Right child of", data)
#     self.root.right = self.create()
#     return self.root