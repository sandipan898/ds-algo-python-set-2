class Deque:
    def __init__(self, max_size):
        self.data = []
        self.data_count = 0
        self.max_size = max_size

    def is_empty(self):
        return self.data_count == 0
    
    def is_full(self):
        return self.data_count == self.max_size
    
    def add_rear(self, data):
        if self.is_full():
            print("Queue Overflow!")
            return False
        print("Adding Rear", data)
        self.data.append(data)
        self.data_count += 1
        return True

    def add_front(self, data):
        if self.is_full():
            print("Queue Overflow!")
            return False
        print("Adding Front", data)
        self.data.insert(0, data)
        self.data_count += 1
        return True

    def remove_front(self):
        if self.is_empty():
            print("Queue Underflow!")
            return False
        data = self.data.pop(0)
        print("Removing Front", data)
        self.data_count -= 1
        return data

    def remove_rear(self):
        if self.is_empty():
            print("Queue Underflow!")
            return False
        data = self.data.pop()
        print("Removing Front", data)
        self.data_count -= 1
        return data

    def __str__(self):
        if self.is_empty():
            return "\n<Queue Empty>\n"
        value = "\n" + "-"*self.data_count*4 + "\n"
        # value += ' '.join(str(d) for d in self.data)
        value += ' '.join(str(d) for d in self.data)
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
