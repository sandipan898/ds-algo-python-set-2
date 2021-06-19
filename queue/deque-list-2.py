class Deque:
    def __init__(self, max_size):
        self.data = [None]*max_size
        self.data_count = 0
        self.max_size = max_size
        self.front = -1
        self.rear = 0

    def is_empty(self):
        return self.data_count == 0
    
    def is_full(self):
        return self.data_count == self.max_size
    
    def add_rear(self, data):
        if self.is_full():
            print("Queue Overflow!")
            return False
        if self.front == -1:
            self.rear = self.front = 0
        elif self.rear == self.max_size - 1:
            self.rear = 0
        else:
            self.rear += 1
        print("Adding Rear", data, "at index", self.rear)
        self.data[self.rear] = data
        self.data_count += 1
        return True

    def add_front(self, data):
        if self.is_full():
            print("Queue Overflow!")
            return False

        if self.front == -1:
            self.rear = self.front = 0
        elif self.front == 0:
            self.front = self.max_size - 1
        else:
            self.front -= 1
        self.data[self.front] = data
        print("Adding Front", data, "at index", self.front)
        self.data_count += 1
        return True

    def remove_front(self):
        if self.is_empty():
            print("Queue Underflow!")
            return False
        data = self.data[self.front]
        print("Removing Front", data, "at index", self.front)
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front == self.max_size - 1:
            self.front = 0
        else:
            self.front += 1
        self.data_count -= 1
        return data

    def remove_rear(self):
        if self.is_empty():
            print("Queue Underflow!")
            return False

        data = self.data[self.rear]
        print("Removing Rear", data, "at index", self.rear)
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.max_size - 1
        else:
            self.rear -= 1
        self.data_count -= 1
        return data

    def __str__(self):
        if self.is_empty():
            return "\n<Queue Empty>\n"
        value = "\n" + "-"*self.data_count*4 + "\n"
        if self.rear >= self.front: 
            for i in range(self.front, self.rear+1):
                value += str(self.data[i]) + " | "
        else:
            for i in range(self.front, self.max_size):
                value += str(self.data[i]) + " | "
            for i in range(0, self.rear+1):
                value += str(self.data[i]) + " | "
        value += "\n" + "-"*self.data_count*4 + "\n"
        value += "Max Size of Queue: " + str(self.max_size) + " | Current Size of Stack: " + str(self.data_count)
        return value


dq = Deque(5)
print(dq)
dq.add_rear(8)
dq.add_rear(5)
dq.add_front(7)
dq.add_front(10)
print(dq)
dq.add_rear(11)
dq.remove_rear()
dq.remove_front()
dq.add_front(55)
dq.add_rear(45)
dq.add_rear(11)
print(dq)

# [8, 5, 11(r), 10(f), 7]
# [8, 5, 11(r), 10(f), 7]