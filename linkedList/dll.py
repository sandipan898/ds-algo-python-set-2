class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.node_count = 0
    
    def insert(self, data, pos=-1):
        new_node = Node(data)
        if self.head is None:
            print("Inserting {} as the First Node".format(data))
            self.head = new_node
            self.tail = new_node 

        elif (pos == 0):
            print("Inserting {} at the Beginning".format(data))
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        elif pos == -1 or self.node_count <= pos:
            print("Inserting {} at the End".format(data))
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        elif pos > 0:
            print("Inserting {} at Index {}".format(data, pos))
            curr = self.head
            while pos - 1 and curr:
                curr = curr.next
                pos -= 1
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
            temp.next = temp.prev = None
        elif pos == -1 or pos >= self.node_count:
            print("Deleting {} from the End!".format(self.tail.data))
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.next = None
            temp.prev = None
        elif pos > 0:
            curr = self.head
            i = pos
            while pos-1 and curr:
                curr = curr.next
                pos -= 1
            print("Deleting {} from Index {}".format(curr.next.data, i))
            curr.next = curr.next.next
            curr.next.prev = curr
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
        while curr!=self.tail.next:
            ret_str += str(curr.data) + "<-->"
            curr = curr.next
        ret_str += "\nTotal Nodes: " + str(self.node_count)
        ret_str += "\nHead Data: " + str(self.head.data) + " | Tail Data: " + str(self.tail.data) + "\n"
        return ret_str


if __name__ == '__main__':
    dll = DoublyLinkedList()
    print(dll)
    dll.insert(12)
    dll.insert(13)
    dll.insert(8, 0)
    dll.insert(7, 0)
    dll.insert(14, -1)
    dll.insert(10, 3)
    dll.insert(11, 4)
    dll.insert(14, -1)
    dll.insert(17, 10)
    print(dll)
    dll.delete()
    dll.delete(2)
    dll.delete(20)
    dll.delete(0)
    dll.delete(-1)
    print(dll)
    dll.insertJunk([33, 34, 35, 36, 37], 3)
    print(dll)
