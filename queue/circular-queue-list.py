class CircularQueue:
    def __init__(self, max_size) -> None: 
        self.rear = self.front = -1
        self.max_size = max_size
        self.queue = [None for i in range(max_size)]
        self.current_size = 0

    def enqueue(self, data):
        if (self.rear+1)%self.max_size == self.front:
            print("Queue Overflow!")
            return False
        
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
        elif self.rear == self.max_size - 1 and self.front != 0:
            self.rear = 0
        else:
            self.rear = (self.rear+1)%self.max_size
        
        print("Enqueue", data)
        self.queue[self.rear] = data
        self.current_size += 1
        return True

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow!")
            return None
        data = self.queue[self.front]
        print("Dequeue", data)
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.max_size - 1:
            self.front = 0
        else:
            self.front = self.front + 1
        
        self.current_size -= 1
        return data
    
    def __str__(self):
        ret_str = '\n' + '-'*self.max_size*4 + '\n'
        if self.front == -1:
            return "<Queue Empty>"
        elif self.rear >= self.front: 
            for i in range(self.front, self.rear+1):
                ret_str += str(self.queue[i]) + " | "
        else:
            for i in range(self.front, self.max_size):
                ret_str += str(self.queue[i]) + " | "
            for i in range(0, self.rear+1):
                ret_str += str(self.queue[i]) + " | "
        ret_str += "\n" + '-'*self.max_size*4 + '\n'
        ret_str += "Queue is Full" if (self.rear+1)%self.max_size == self.front else "Current Size: " + str(self.current_size)
        return ret_str


c_queue = CircularQueue(7)
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
