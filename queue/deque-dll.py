class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None


class Deque:
    def __init__(self):
        self.node_count = 0
        self.front = self.rear = None
    
    def insert_front(self, data):
        new_node = Node(data)
        print("Inserting Front", data)
        if new_node == None:
            print("Memory Overflow!")
            return False
        if self.front == None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.node_count += 1
        return True

    def insert_rear(self, data):
        new_node = Node(data)
        print("Inserting Rear", data)
        if new_node == None:
            print("Memory Overflow!")
            return False
        if self.front == None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.node_count += 1
        return True
    
    def remove_front(self):
        if self.is_empty():
            print("Queue Underflow!")
            return False
        temp = self.front
        data = temp.data
        print("Removing Front", data)
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        else:
            self.front.prev = None
        temp.next = None
        temp.prev = None
        self.node_count -= 1
        return True

    def remove_rear(self):
        if self.is_empty():
            print("Queue Underflow!")
            return False
        temp = self.rear
        data = temp.data
        print("Removing Rear", data)
        self.rear = self.rear.prev
        if self.rear == None:
            self.front = None
        else:
            self.rear.next = None
        temp.prev = None
        self.node_count -= 1
        return True

    def is_empty(self):
        return self.front is None

    def __str__(self):
        if self.is_empty():
            return "<Queue Empty>"
        curr = self.front
        ret_str = "\n" + "-"*self.node_count*4 + "\n"
        while curr:
            ret_str += str(curr.data) + " | "
            curr = curr.next
        ret_str += "\n" + "-"*self.node_count*4 + "\n"
        ret_str += "\nTotal Nodes: " + str(self.node_count)
        ret_str += "\nFront Data: " + str(self.front.data) + " | Rear Data: " + str(self.rear.data) + "\n"
        return ret_str


dq = Deque()
print(dq)
dq.insert_rear(8)
dq.insert_rear(5)
dq.insert_front(7)
dq.insert_front(10)
print(dq)
dq.insert_rear(11)
dq.remove_rear()
dq.remove_front()
dq.insert_front(55)
dq.insert_rear(45)
dq.insert_rear(11)
print(dq)
