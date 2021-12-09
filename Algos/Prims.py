from networkx.algorithms.shortest_paths import weighted
from .graph import Graph
import sys

class Prims:
    def __init__(self,G,src):
        self.G = G
        self.src = src
        self.parent = [None] * self.G.V
        self.val = [-sys.maxsize] * self.G.V
        self.PrimCost = 0

    def FindMax(self,val, vis, V):
        
        max = -sys.maxsize
        vertex = self.src

        for i in range(V):
            if not vis[i] and val[i] > max:
                max = val[i]
                vertex = i

        return vertex


    def Prims_MST(self):
        vis = [False] * self.G.V
        
        self.val[self.src] = 0
        self.parent[self.src] = -1

        for i in range(self.G.V):
            max = self.FindMax(self.val, vis, self.G.V)
            vis[max] = True

            tNode = self.G.graph[max]
            while tNode is not None:
                if not vis[tNode.vertex] and self.val[tNode.vertex] < tNode.weight:
                    self.val[tNode.vertex] = tNode.weight
                    self.parent[tNode.vertex] = max

                tNode = tNode.next

        mst_cost = 0 
        for i in range(0, self.G.V):
            print("{} -> {} cost => {}".format(self.parent[i], i, self.val[i]))
            mst_cost += self.val[i]
        
        self.PrimCost = mst_cost
        print("Minimum Cost {}".format(self.PrimCost))


# def Display_MST():

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

#     P = Prims(graph, 0)
#     P.Prims_MST()
#     P.MST()

