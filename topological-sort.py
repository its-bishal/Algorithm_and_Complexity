# topological sort in graph

from collections import defaultdict


class Graph:

    def __init__(self, vertices_num):
        self.graph = defaultdict(list)
        self.vertices_num = vertices_num

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def topologicalsortutl(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalsortutl(i, visited, stack)
        
        stack.insert(0,v)

    def topologicalsort(self):
        stack = []
        visited = []

        for j in list(self.graph):
            if j not in visited:
                self.topologicalsortutl(j, visited, stack)

        print(stack)


customgraph = Graph(8)
customgraph.add_edge('A',"C")
customgraph.add_edge('C',"E")
customgraph.add_edge('E',"H")
customgraph.add_edge('E',"F")
customgraph.add_edge('F',"G")
customgraph.add_edge('B',"D")
customgraph.add_edge('B',"F")
customgraph.add_edge('D',"F")

customgraph.topologicalsort()