

import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, path):

        self.graph_data = pd.read_csv(path,sep=" ",names=['from','to','weight'])

        # fill for the missing weights 
        self.graph_data['weight'].fillna(1)
        self.graph = nx.from_pandas_edgelist(self.graph_data, 'from','to',['weight'])

        self.nodes_count = self.graph.number_of_nodes()
        self.edge_count = self.graph.number_of_edges()

        self.nodes = list(self.graph.nodes())
        self.edges = list(self.graph.edges())

        self.degrees = [degree[1] for degree in self.graph.degree]

    
    def clustering_coeff(self):
        coeff = []
        for node in self.graph.nodes():
            neighbors = list(self.graph.neighbors(node))
            nei_len = len(neighbors)
            subgraph = nx.subgraph(self.graph, neighbors)
            edge_num = subgraph.number_of_edges()
            count = 2 * edge_num / (nei_len*(nei_len-1)) \
                if nei_len > 1 else 0
            coeff.append(count)

        return np.average(coeff)
    
    def BFS(self, start_node):
        visited = [start_node]
        queue = [(start_node, 0)]
        max_distance = 0

        while queue:
            traversed, distance = queue.pop(0)
            max_distance = max(max_distance, distance)

            for neigh in self.graph.neighbors(traversed):
                if neigh not in visited:
                    visited.append(neigh)
                    queue.append((neigh, distance+1))

        return max_distance
    
    def diameter(self):
        diameter = 0
        for node in self.nodes:
            distance = self.BFS(start_node=node)
            diameter = max(diameter, distance)

        return diameter
    
    def read_graph(self):
        avg_degree = sum(self.degrees)/self.nodes_count
        density = 2*(self.edge_count)/(self.nodes_count*(self.nodes_count-1))\
            if self.nodes_count > 1 else 0
        
        if nx.is_connected(self.graph):
            diameter = self.diameter()
        else:
            diameter = '-'

        clustering_coeff = self.clustering_coeff()

        print(f'Number of nodes{self.nodes_count}')
        print(f'Number of edges {self.edge_count}')
        print(f'Average degree {avg_degree}')
        print(f'Density {density}')
        print(f'Diameter {diameter}')
        print(f'Clustering coefficient {clustering_coeff}')
        print(f'Connected {nx.is_connected(self.graph)}')

    def plot_graph(self):
        nx.draw_random(self.graph)
        plt.show()

    def plot_degree_distribution(self):
        degree_dis = dict()

        # count no of nodes with same degree
        for deg in self.degrees:
            if deg not in degree_dis:
                degree_dis[deg] = 1
            else:
                degree_dis[deg] += 1

        # normalilze the nodes
        degree_dis = { key: value / self.nodes_count
                      for (key, value) in degree_dis.items()}
        
        plt.bar(degree_dis.keys(), degree_dis.values())
        plt.title('Degree distribution for {self.name}')
        plt.xlabel('Degree')
        plt.ylabel('node fraction')
        plt.show()

# new_graph = Graph("labs/graphs/Cities.mtx")
# new_graph = Graph("labs/graphs/econ-mahindas.mtx")
# new_graph = Graph("labs/graphs/econ-poli.mtx")
# new_graph = Graph("labs/graphs/econ-psmigr1.mtx")
# new_graph = Graph("labs/graphs/ia-reality.mtx")
# new_graph = Graph("labs/graphs/bio-grid-human.edges")
new_graph = Graph("labs/graphs/bio-DM-CX.edges")


new_graph.read_graph()
new_graph.plot_graph()
new_graph.plot_degree_distribution()