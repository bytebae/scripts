from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_node(self, u, v):
        self.graph[u].append(v)

    def breadth_first_search(self, start): #start has to be a unique number
        visited = [False] * len(self.graph)
        queue = []

        queue.append(start)
        visited[start] = True
        
