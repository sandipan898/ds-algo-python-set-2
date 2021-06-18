class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    

class CircularQueueLL:
    def __init__(self):
        self.front = self.rear = None
        self.node_count = 0 
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.front == None:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            new_node.next = self.front
            self.rear = new_node
        self.node_count += 1
        print("Enqueue", data)
        return True
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow!")
            return None
        data = self.front.data
        print("Dequeue", data)
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.nxt = self.front
        self.node_count -= 1
        return data
    def __str__(self):
        if self.is_empty(): 
            return "<Queue Empty>" 
        else:
            ret_str = '\n' + '-'*self.node_count*4 + '\n'
            curr = self.front
            # while curr!=self.rear:
            for i in range(self.node_count):
                ret_str += str(curr.data) + " | "
                curr = curr.next
            # ret_str += str(curr.data)
            ret_str += "\n" + '-'*self.node_count*4 + '\n'
            ret_str += "Current Size: " + str(self.node_count)
            return ret_str
        
    def is_empty(self):
        if self.front is None:
            return True



c_queue = CircularQueueLL()
print(c_queue)
c_queue.enqueue(12)
c_queue.dequeue()
c_queue.dequeue()
print(c_queue)
c_queue.enqueue(20)
c_queue.enqueue(18)
c_queue.enqueue(9)
c_queue.enqueue(25)
c_queue.enqueue(27)
c_queue.enqueue(30)
print(c_queue)
# c_queue.resize(10)
c_queue.dequeue()
c_queue.dequeue()
c_queue.enqueue(43)
c_queue.enqueue(57)
print(c_queue)
# c_queue.is_full()
# c_queue.is_empty()
c_queue.dequeue()
c_queue.dequeue()
c_queue.dequeue()
c_queue.dequeue()
print(c_queue)
