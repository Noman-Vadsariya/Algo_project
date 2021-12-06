from .graph import Graph

class Floyd:

    def __init__(self,G):
        self.G = G
        self.dist = [[float("Inf") for i in range(G.V)] for j in range(G.V)]

    def FloydWarshall(self):
        for i in range(self.G.V):
            self.dist[i][i] = 0
            temp = self.G.graph[i]
            while temp is not None:
                self.dist[i][temp.vertex] = temp.weight
                temp = temp.next

        for k in range(self.G.V):  # for considering each vertex as a source
            for i in range(self.G.V):
                for j in range(self.G.V):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]

        for i in range(self.G.V):
            for j in range(self.G.V):
                print("{}   ".format(self.dist[i][j]), end="")
            print()


# if __name__ == "__main__":
#     V = 9

#     # Create graph and edges
#     graph = Graph(V)
#     graph.add_edge(0, 1, 4)
#     graph.add_edge(0, 7, 8)
#     graph.add_edge(1, 7, 11)
#     graph.add_edge(1, 2, 8)
#     graph.add_edge(7, 6, 1)
#     graph.add_edge(2, 8, 2)
#     graph.add_edge(8, 6, 6)
#     graph.add_edge(7, 8, 7)
#     graph.add_edge(2, 5, 4)
#     graph.add_edge(2, 3, 7)
#     graph.add_edge(3, 5, 14)
#     graph.add_edge(6, 5, 2)
#     graph.add_edge(5, 4, 10)
#     graph.add_edge(3, 4, 9)

#     graph.print_graph()

#     FloydWarshall(graph)
