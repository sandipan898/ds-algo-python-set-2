class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_list = [None]*size
        self.visited = [False]*size
        self.queue = []

    def add_edge(self, u, v):
        dest = Node(v)
        if self.adj_list[u] == None:
            src = Node(u)
            src.next = dest
            self.adj_list[u] = src
        else:
            temp = self.adj_list[u]
            while temp.next:
                temp = temp.next
            temp.next = dest

        dest = Node(u)
        if self.adj_list[v] == None:
            src = Node(v)
            src.next = dest
            self.adj_list[v] = src
        else:
            temp = self.adj_list[v]
            while temp.next:
                temp = temp.next
            temp.next = dest
    
    def BFS(self, start):
        self.visited[start] = True
        self.queue.append(start)
        while len(self.queue) > 0:
            current_node = self.queue.pop(0)
            print(current_node, end=" ")
            temp = self.adj_list[current_node].next
            while temp:
                if not self.visited[temp.data]:
                    self.visited[temp.data] = True
                    self.queue.append(temp.data)
                temp = temp.next

    def display_list(self):
        for i in self.adj_list:
            temp = i
            while temp:
                print("{} --> ".format(temp.data), end="")
                temp = temp.next
            print()

if __name__ == '__main__':
    graph = Graph(7)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    graph.add_edge(2, 5)
    graph.add_edge(4, 6)
    # graph.add_edge(5, 6)
    graph.display_list()
    graph.BFS(1)
    print()