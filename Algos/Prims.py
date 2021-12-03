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


def Prims(G, s):

    val = [sys.maxsize] * G.V
    vis = [False] * G.V
    p = [None] * G.V

    val[s] = 0
    p[s] = -1

    for i in range(G.V):
        min = FindMin(val, vis, G.V)
        vis[min] = True

        tNode = G.graph[min]
        while tNode is not None:
            if not vis[tNode.vertex] and val[tNode.vertex] > tNode.weight:
                val[tNode.vertex] = tNode.weight
                p[tNode.vertex] = min

            tNode = tNode.next

    for i in range(1, G.V):
        print("{} -> {} cost => {}".format(p[i], i, val[i]))
        val[0] += val[i]

    print("Minimum Cost {}".format(val[0]))


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

#     Prims(graph, 0)

