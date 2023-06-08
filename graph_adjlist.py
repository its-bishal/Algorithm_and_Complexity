# here a graph is created using adjacency list method


class Graph:
    def __init__(self, dict_graph=None):
        if dict_graph is None:
            dict_graph = {}
        else:
            self.dict_graph = dict_graph

    
    def add_edge(self, vertex, edge):
        self.dict_graph[vertex].append(edge)


    #breadth first search method implementation for graph traversal
    def bfs_traversal(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            #this pop method pops the first element of the queue implemented as list
            deqd_vertex = queue.pop(0)
            print(deqd_vertex)

            for adj_vertex in self.dict_graph[deqd_vertex]:
                if adj_vertex not in visited:
                    visited.append(adj_vertex)
                    queue.append(adj_vertex)

    def dfs_traversal(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while stack:
            #this pop method removes the last element from the stack 
            pop_vertex = stack.pop()
            print(pop_vertex)

            for adj_vertex in self.dict_graph[pop_vertex]:
                if adj_vertex not in visited:
                    visited.append(adj_vertex)
                    stack.append(adj_vertex)


custom_dict = {
    'a' : ['b', 'c'],
    'b' : ['a', 'd', 'e'],
    'c' : ['a', 'e'],
    'd' : ['b', 'e', 'f'],
    'e' : ['d', 'f', 'c'],
    'f' : ['d', 'e']
}

graph = Graph(custom_dict)

# graph.add_edge('a','d')
# graph.add_edge('b','d')
# print(graph.dict_graph)

# graph.bfs_traversal('a')
graph.dfs_traversal('a')