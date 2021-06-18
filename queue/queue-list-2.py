class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = []
    
    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow! Resize to enqueue more data!")
            return None
        self.data.append(data)
        print(data, "Enqueued!")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Can't dequeue data from empty queue!")
            return None
        value = self.data[0]
        del self.data[0]
        print(value, "Dequeued!")
        return value
    
    def is_empty(self):
        return True if len(self.data) == 0 else False
    
    def is_full(self):
        return True if len(self.data) == self.max_size else False

    def peek(self):
        return self.data[0]

    def resize(self, size):
        self.max_size = size
    
    def __str__(self):
        value = "\n---------\n"
        value += ' '.join(str(self.data[i]) for i  in range(0, len(self.data)))
        value += "\n---------\n"
        value += "Max Size of Queue: " + str(self.max_size) + " | Current Size of Stack: " + str(len(self.data))
        return value

    
sample_queue = Queue(5)
sample_queue.enqueue(12)
sample_queue.dequeue()
sample_queue.dequeue()
print(sample_queue)
sample_queue.enqueue(20)
sample_queue.enqueue(18)
sample_queue.enqueue(9)
sample_queue.enqueue(25)
sample_queue.enqueue(27)
sample_queue.enqueue(30)
print(sample_queue)
sample_queue.resize(10)
sample_queue.enqueue(43)
sample_queue.enqueue(57)
print(sample_queue)
sample_queue.is_full()
sample_queue.is_empty()
sample_queue.dequeue()
sample_queue.dequeue()
sample_queue.dequeue()
sample_queue.dequeue()
sample_queue.dequeue()
sample_queue.dequeue()
print(sample_queue)
