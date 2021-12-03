from .graph import Graph

def BellmanFord(G, src):
    val = [float("Inf")]*G.V;

    val[src] = 0;

    for k in range(G.V-1):  #each node will be relaxed vertex-1 times
        for i in range(G.V): #all the vertexes will be relaxed
            temp = G.graph[i];
            
            while (temp is not None):
                if (val[temp.vertex] > val[i] + temp.vertex):
                    val[temp.vertex] = val[i] + temp.weight;
                temp = temp.next;

    for i in range(G.V):
        print("{} => {}".format(i,val[i]))

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

#     BellmanFord(graph, 0)
