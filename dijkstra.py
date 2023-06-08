from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertex = set()
        self.edges = defaultdict(list)
        self.connection_value = {}

    def addvertex(self, value):
        self.vertex.add(value)

    def addEdge(self, fromVertex, toVertex, value):
        self.edges[fromVertex].append(toVertex)
        self.connection_value[(fromVertex, toVertex)] = value
    

def Dijkstra(graph, fromVertex):
    visited = {fromVertex:0}
    connection = defaultdict(list)

    vertices = set(graph.vertex)

    while vertices:
        minVertex = None

        for vertex in vertices:
            if vertex in visited:

                if minVertex is None:
                    minVertex = vertex

                elif visited[vertex] < visited[minVertex]:
                    minVertex = vertex
        
        if minVertex is None:
            break

        vertices.remove(minVertex)

        currentValue = visited[minVertex]

        # totalValue = connection[minVertex] + currentValue
        for edge in graph.edges[minVertex]:
            value = currentValue + graph.connection_value[(minVertex, edge)]
            if edge not in visited or value < visited[edge]:
                visited[edge] = value
                connection[edge].append(minVertex)
    
    return visited, connection


new = Graph()

new.addvertex(2)
new.addvertex(5)
new.addvertex(13)
new.addvertex(9)
new.addvertex(11)

new.addEdge(2,5,2)
new.addEdge(2,13,5)
new.addEdge(5,13,4)
new.addEdge(5,9,7)
new.addEdge(5,11,7)
new.addEdge(11,9,8)
new.addEdge(9,2,6)

dij = Dijkstra(new, 5)
print(dij)