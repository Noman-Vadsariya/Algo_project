from .graph import Graph
import sys


def FindMin(val, vis, V):

    min = sys.maxsize
    vertex = 0

    for i in range(V):
        if not vis[i] and val[i] < min:
            min = val[i]
            vertex = i

    return vertex

def Djikstra(G,src):

    dist = [sys.maxsize] * G.V
    dist[src] = 0
    vis = [False] * G.V

    for cout in range(G.V):
        min = FindMin(dist, vis, G.V)

        vis[min] = True
        
        tNode = G.graph[min]
        while tNode is not None:
            if not vis[tNode.vertex] and dist[tNode.vertex] > dist[min] + tNode.weight:
                    dist[tNode.vertex] = dist[min] + tNode.weight
            
            tNode=tNode.next

    for i in range(G.V):
        print("{}  => {}".format(i,dist[i]))

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

#     Djikstra(graph, 0)
