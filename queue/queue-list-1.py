class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [None]*(max_size+1)
        self.front = -1
        self.rear = -1
    
    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow! Resize to enqueue more data!")
            return None
        if self.front == -1:
            self.front = 0
        self.rear += 1            
        self.data[self.rear] = data
        print(data, "Enqueued!")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Can't dequeue data from empty queue!")
            return None
        value = self.data[self.front]
        self.data[self.front] = None
        # del self.data[self.front]
        # if self.front == self.rear:
        #     self.front = self.rear = -1
        # else:
        #     self.front += 1
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1
        print(value, "Dequeued!")
        return value
    
    def is_empty(self):
        # return True if len(self.data) == 0 else False
        return True if self.front == -1 else False
    
    def is_full(self):
        # return True if self.rear >= self.max_size-1 else False
        return True if self.front == 0 and self.rear == self.max_size-1 else False

    def peek(self):
        return self.data[self.front]

    def resize(self, size):
        self.data.extend([None]*(size-self.max_size))
        self.max_size = size
        # print(self.data)
        # if size < self.max_size:
        #     print("Resizing to a small length! All the remaining values will be deleted!")
        #     for i in range(self.max_size-size):
        #         self.pop()
    
    def __str__(self):
        value = "\n---------\n"
        value += ' '.join(str(self.data[i]) for i  in range(self.front, self.rear+1))
        value += "\n---------\n"
        value += "Max Size of Queue: " + str(self.max_size) + " | Current Size of Stack: " + str(self.rear - self.front+1)
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
