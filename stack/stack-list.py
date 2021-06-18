class Stack:
    def __init__(self, length):
        self.length = length
        self.size = 0
        self.data = []

    def push(self, value):
        if len(self.data) >= self.length:
            print("Stack is already filled! Resize the stack to Push more!")
            return None
        print(value, "Pushed")
        self.data.append(value)
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            print("Stack is Empty!")
            return None
        value = self.data[-1]
        del self.data[-1]
        print(value, "Popped")
        self.size -= 1
        return value
        # return self.data.pop()

    def is_empty(self):
        return True if len(self.data) == 0 else False
    
    def peek(self):
        if self.is_empty():
            print("Stack is Empty!")
            return None
        return self.data[-1]

    def resize(self, size):
        self.length = size
        if size < self.length:
            print("Resizing to a small length! All the remaining values will be deleted!")
            for i in range(self.length-size):
                self.pop()
    
    def __str__(self):
        value = "\n---------\n"
        value += '\n'.join(str(self.data[i]) for i  in range(len(self.data)-1, -1, -1))
        value += "\n---------\n"
        value += "Max Size of Stack: " + str(self.length) + " | Current Size of Stack: " + str(self.size)
        return value

sample_stack = Stack(7)
sample_stack.pop()
sample_stack.push(12)
sample_stack.push(15)
sample_stack.push(18)
sample_stack.push(9)
print(sample_stack)
sample_stack.push(11)
sample_stack.resize(10)
sample_stack.push(21)
sample_stack.push(25)
sample_stack.push(32)
print(sample_stack)
sample_stack.pop()
sample_stack.pop()
sample_stack.pop()
print(sample_stack)
