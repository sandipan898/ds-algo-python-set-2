class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0

    def insert(self, data, pos=-1):
        new_node = Node(data)
        if self.head == None:
            print("Inserting {} as the First Node".format(data))
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        elif pos == 0:
            print("Inserting {} at the Beginning".format(data))
            self.tail.next = new_node
            new_node.next = self.head
            self.head = self.tail.next
        elif pos == -1 or self.node_count <= pos:
            print("Inserting {} at the End".format(data))
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        elif pos > 0:
            print("Inserting {} at Index {}".format(data, pos))
            curr = self.head.next
            while pos-2 and curr!=self.head:
                pos -= 1
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        else:
            print("Invalid Position entered")
            return False
        self.node_count += 1
        return True

    def delete(self, pos=-1):
        if self.head == None:
            print("List is already empty!")
        elif pos == 0:
            print("Deleting {} from the Beginning!".format(self.head.data))
            self.tail.next = self.head.next
            self.head.next = None 
            self.head = self.tail.next
            if self.head is None:
                self.tail = None
        elif pos == -1 or pos >= self.node_count:
            print("Deleting {} from the End!".format(self.tail.data))
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            curr.next = self.tail.next
            self.tail = curr
        elif pos > 0:
            curr = self.head
            i = pos
            while pos-1 and curr:
                curr = curr.next
                pos -= 1
            print("Deleting {} from Index {}".format(curr.next.data, i))
            curr.next = curr.next.next
        else:
            print("Invalid Position entered")
            return False
        self.node_count -= 1
        return True
    
    def insertJunk(self, data_list, pos=-1):
        if pos >= 0:
            for data in data_list[::-1]:
                self.insert(data, pos)
        elif pos == -1:
            for data in data_list:
                self.insert(data, pos)

    def __str__(self):
        if self.node_count == 0:
            return "<Empty List>"
        ret_str = "-->" + str(self.head.data) + "-->"
        curr = self.head.next
        while curr!=self.head:
            ret_str += str(curr.data) + "-->"
            curr = curr.next
        ret_str += "\nTotal Nodes: " + str(self.node_count)
        ret_str += "\nHead Data: " + str(self.head.data) + " | Tail Data: " + str(self.tail.data) + "\n"
        return ret_str


if __name__ == '__main__':
    cll = CircularLinkedList()
    print(cll)
    cll.insert(12)
    cll.insert(13)
    cll.insert(8, 0)
    cll.insert(7, 0)
    cll.insert(14, -1)
    cll.insert(10, 3)
    cll.insert(11, 4)
    cll.insert(14, -1)
    cll.insert(17, 10)
    print(cll)
    cll.delete()
    cll.delete(2)
    cll.delete(20)
    cll.delete(0)
    cll.delete(-1)
    print(cll)
    cll.insertJunk([33, 34, 35, 36, 37], 3)
    print(cll)
