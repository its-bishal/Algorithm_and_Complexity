# a breadth first search for single source shortest path problem

class Graph:

    def __init__(self, g_dict=None):
        if g_dict is None:
            g_dict = {}
        self.g_dict = g_dict

    def bfs(self, start, end):
        queue = []
        queue.append([start])

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            
            for adjacent in self.g_dict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


new_graph = {
    'a': ['b', 'c'],
    'b': ['d', 'g'],
    'c': ['d', 'e'],
    'd': ['g', 'f'],
    'e': ['f'],
    'f': ['h', 'i'],
    'g': ['h'],
    'h': ['i'],
}

new = Graph(new_graph)
print(new.bfs('a', 'i'))

