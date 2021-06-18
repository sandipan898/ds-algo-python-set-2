class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def is_empty(self):
        return True if self.top == None else False
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "Pushed!")
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            print("Can't POP data from an empty stack!")
            return None
        value = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(value, "Popped!")
        return value
    
    def peek(self):
        if self.is_empty():
            print("Can't PEEK data from an empty stack!")
            return None
        return self.top.data
    def get_size(self):
        return self.size
    
    def __str__(self):
        value = "\n---------\n"
        data_str = ""
        curr = self.top
        while curr!=None:
            data_str += str(curr.data) + "\n"
            curr = curr.next

        value += data_str
        value += "Current Size of Stack: " + str(self.size)
        value += "\n---------\n"
        return value


sample_stack = Stack()
sample_stack.pop()
sample_stack.push(12)
sample_stack.push(15)
sample_stack.push(18)
sample_stack.push(9)
print(sample_stack)
sample_stack.pop()
sample_stack.push(11)
sample_stack.push(21)
sample_stack.push(25)
sample_stack.push(32)
print(sample_stack)
sample_stack.pop()
sample_stack.pop()
sample_stack.pop()
print(sample_stack)
