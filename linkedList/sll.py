class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0

    def insert(self, data, pos=-1):
        new_node = Node(data)
        if self.head == None:
            print("Inserting First node:", data)
            self.head = new_node
            self.tail = new_node
        elif pos == 0:
            print("Inserting at Beginning:", data)
            new_node.next = self.head
            self.head = new_node
        elif pos == -1 or self.nodeCount() <= pos:
            print("Inserting at End:", data)
            self.tail.next = new_node
            self.tail = new_node
        else:
            print("Inserting at Index:", pos, data)
            curr = self.head
            while pos-1: # 1-->2-->new-->3-->4-->N
                curr = curr.next
                pos -= 1
            new_node.next = curr.next
            curr.next = new_node
        self.node_count += 1
        return True

    def insertJunk(self, data_list, pos=-1):
        print("inserting Junk")
        index = 0
        if pos == -1:
            for data in data_list:
                self.insert(data, -1)
        else:
            for data in data_list[::-1]: # [23, 25, 21, 28, 34] 1-->2-->3 23 25 21 28 34-->4-->5-->6-->N
                if pos == 0:
                    self.insert(data, 0)
                else:
                    self.insert(data, pos)
                    index += 1
        return True

    def nodeCount(self):
        return self.node_count
    
    def delete(self, pos):
        if self.nodeCount() == 0:
            print("List is already Empty!")
            return False
        if pos == 0:
            print("Deleting from Beginning:", self.head.data)
            self.head = self.head.next
        elif pos == -1 or self.nodeCount() <= pos:
            print("Deleting from End!", self.tail.data)
            curr = self.head
            while curr.next!=self.tail:
                curr = curr.next
            self.tail = curr
            self.tail.next = None
        else:
            print("Deleting from Index", pos if self.nodeCount() > pos else "End")
            curr = self.head
            while pos-1: # 1-->2-->4-->N
                curr = curr.next
                pos -= 1
            curr.next = curr.next.next
        self.node_count -= 1
        return True
    
    def deleteLL(self):
        self.head = None
        self.tail = None

    def findMax(self):
        if self.node_count <= 0:
            return None
        curr = self.head
        max_val = self.head.data
        while curr:
            if curr.data > max_val:
                max_val = curr.data
            curr = curr.next
        return max_val
    
    def findMin(self):
        if self.node_count <= 0:
            return None
        curr = self.head
        min_val = self.head.data
        while curr:
            if curr.data < min_val:
                min_val = curr.data
            curr = curr.next
        return min_val
    
    def search(self, data):
        curr = self.head
        index = []
        pos = 0
        while curr:
            if curr.data == data:
                index.append(pos+1)
            pos += 1
            curr = curr.next
        return index if index else None

    def reverseLL(self):
        curr = self.head
        data_list = []
        while curr:
            data_list.append(curr.data) 
            curr = curr.next
        self.deleteLL()
        self.insertJunk(data_list[::-1], 0)

    def __str__(self):
        curr = self.head
        ll_str = ""
        while curr:
            ll_str += str(curr.data) + "-->"
            curr = curr.next
        return ll_str


sampleSLL = SinglyLinkedList()
sampleSLL.insert(12)
sampleSLL.insert(15, 0)
sampleSLL.insert(13, 1)
sampleSLL.insert(17, -1)
print(sampleSLL)
sampleSLL.delete(2)
sampleSLL.delete(0)
print(sampleSLL)
sampleSLL.insertJunk([23, 25, 21, 28, 34], 3)
print(sampleSLL)
sampleSLL.delete(-1)
sampleSLL.delete(0)
print(sampleSLL)
print(sampleSLL.findMin())
print(sampleSLL.findMax())
sampleSLL.reverseLL()
print(sampleSLL)
