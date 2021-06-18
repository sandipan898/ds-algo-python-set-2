class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = Node


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0
    
    def insert(self, data, pos=-1):
        # print(pos)
        new_node = Node(data)
        if self.head == None:
            print("Inserting {} as the First Node".format(data))
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
            self.head.prev = self.head
        
        elif pos == 0:
            print("Inserting {} at the Beginning".format(data))
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        elif pos == -1 or pos >= self.node_count:
            print("Inserting {} at the End".format(data))
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        
        elif pos > 0:
            print("Inserting {} at Index {}".format(data, pos))
            curr = self.head
            while pos - 1 and curr:
                pos -= 1
                curr = curr.next
            new_node.prev = curr
            new_node.next = curr.next
            curr.next.prev = new_node
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
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            temp.next = None
            temp.prev = None
        
        elif pos == -1 or pos >= self.node_count:
            print("Deleting {} from the End!".format(self.tail.data))
            temp = self.tail.prev
            temp.next = self.head
            self.head.prev = temp
            self.tail.next = None
            self.tail.prev = None
            self.tail = temp

        elif pos > 0:
            curr = self.head
            i = pos
            while pos-1 and curr:
                curr = curr.next
                pos -= 1
            print("Deleting {} from Index {}".format(curr.next.data, i))
            temp = curr.next
            curr.next = temp.next
            temp.next.prev = curr
            temp.next = None
            temp.prev = None

        else:
            print("Invalid Position entered")
            return False
        self.node_count -= 1
        return True

    def insertJunk(self, data_list, pos=-1): #[1, 2, 3, 4] 12345<-->6<-->7<-->12348<-->1234
        if pos >= 0:
            for data in data_list[::-1]:
                self.insert(data, pos)
        elif pos == -1:
            for data in data_list:
                self.insert(data, pos)

    def __str__(self):
        if self.node_count == 0:
            return "<Empty List>"
        curr = self.head
        ret_str = '\n'
        while curr!=self.tail:
            ret_str += str(curr.data) + "<-->"
            curr = curr.next
        ret_str += str(self.tail.data) + "<-->"
        ret_str += "\nTotal Nodes: " + str(self.node_count)
        ret_str += "\nHead Data: " + str(self.head.data) + " | Tail Data: " + str(self.tail.data) + "\n"
        return ret_str


if __name__ == '__main__':
    dcll = DoublyCircularLinkedList()
    print(dcll)
    dcll.insert(12)
    dcll.insert(13)
    dcll.insert(8, 0)
    dcll.insert(7, 0)
    dcll.insert(14, -1)
    dcll.insert(10, 3)
    dcll.insert(11, 4)
    dcll.insert(14, -1)
    dcll.insert(17, 10)
    print(dcll)
    dcll.delete()
    dcll.delete(2)
    dcll.delete(20)
    dcll.delete(0)
    dcll.delete(-1)
    print(dcll)
    dcll.insertJunk([33, 34, 35, 36, 37], 3)
    print(dcll)
