class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Graph:
    def __init__(self, size):
        self.size = size
        self.vertex_list = [None]*self.size
    
    def add_edge(self, u, v):
        dest = Node(v)
        if self.vertex_list[u] == None: # If the node is not in our Adj list
            src = Node(u)
            src.next = dest
            self.vertex_list[u] = src
        else: 
            temp = self.vertex_list[u]
            while temp.next != None:
                temp = temp.next
            temp.next = dest
        
        src = Node(u)
        if self.vertex_list[v] == None: # If the node is not in our Adj list
            dest = Node(v)
            dest.next = src
            self.vertex_list[v] = dest
        else:
            temp = self.vertex_list[v]
            while temp.next != None:
                temp = temp.next
            temp.next = src
    
    # def add_edge(self, s, d):
    #     node = Node(d)
    #     node.next = self.vertex_list[s]
    #     self.vertex_list[s] = node

    #     node = Node(s)
    #     node.next = self.vertex_list[d]
    #     self.vertex_list[d] = node

    def print_graph(self):
        print("\nN")
        for i in range(self.size):
            temp = self.vertex_list[i]
            while temp:
                print("{} --> ".format(temp.data), end="")
                temp = temp.next
            print()

if __name__ == "__main__":
    V = 5
    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_graph()
