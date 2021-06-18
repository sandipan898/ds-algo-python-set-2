class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(data, "Enqueued")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow!")
            return None
        value = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.front = self.rear = None
        print(value, "Deququed")
        return value

    def is_empty(self):
        return True if self.front == None else False
    
    def peek(self):
        return self.front.data
    
    def __str__(self):
        curr = self.front
        data_str = ""
        while curr != None:
            data_str += str(curr.data) + " | "
            curr = curr.next
        return data_str


sample_queue = Queue()
sample_queue.enqueue(12)
print(sample_queue)
sample_queue.dequeue()
sample_queue.dequeue()
print(sample_queue)
sample_queue.enqueue(15)
sample_queue.enqueue(19)
sample_queue.enqueue(23)
print(sample_queue)
sample_queue.enqueue(27)
sample_queue.enqueue(11)
print(sample_queue)
sample_queue.dequeue()
sample_queue.dequeue()
sample_queue.dequeue()
sample_queue.dequeue()
print(sample_queue)
