from graph import Graph


def FloydWarshall(G):
    dist = [[float("Inf") for i in range(G.V)] for j in range(G.V)]

    for i in range(G.V):
        dist[i][i] = 0
        temp = G.graph[i]
        while temp is not None:
            dist[i][temp.vertex] = temp.weight
            temp = temp.next

    for k in range(G.V):  # for considering each vertex as a source
        for i in range(G.V):
            for j in range(G.V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(G.V):
        for j in range(G.V):
            print("{}   ".format(dist[i][j]), end="")
        print()


if __name__ == "__main__":
    V = 9

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(1, 2, 8)
    graph.add_edge(7, 6, 1)
    graph.add_edge(2, 8, 2)
    graph.add_edge(8, 6, 6)
    graph.add_edge(7, 8, 7)
    graph.add_edge(2, 5, 4)
    graph.add_edge(2, 3, 7)
    graph.add_edge(3, 5, 14)
    graph.add_edge(6, 5, 2)
    graph.add_edge(5, 4, 10)
    graph.add_edge(3, 4, 9)

    graph.print_graph()

    FloydWarshall(graph)
