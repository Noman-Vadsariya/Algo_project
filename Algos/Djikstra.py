from .graph import Graph
import sys

class Djikstra:
    def __init__(self,G,src):
        self.dist = [float(sys.maxsize)] * G.V
        self.G = G
        self.src = src
        self.path = []

    def FindMin(self,val, vis, V):

        min = sys.maxsize
        vertex = 0

        for i in range(V):
            if not vis[i] and val[i] < min:
                min = val[i]
                vertex = i

        return vertex

    def djikstra(self):

        self.dist[self.src] = 0
        vis = [False] * self.G.V

        for cout in range(self.G.V):
            min = self.FindMin(self.dist, vis, self.G.V)

            vis[min] = True
            
            tNode = self.G.graph[min]
            while tNode is not None:
                if not vis[tNode.vertex] and self.dist[tNode.vertex] > self.dist[min] + tNode.weight:
                    self.dist[tNode.vertex] = self.dist[min] + tNode.weight
                    curr = tNode.vertex
                    w = tNode.weight
                    
                    for u,v,w in self.path:
                        if v==tNode.vertex:
                            self.path.remove([u,v,w])

                    self.path.append([min,tNode.vertex,tNode.weight])
                
                tNode=tNode.next
            
        for i in range(self.G.V):
            print("{}  => {}".format(i,self.dist[i]))

        print(self.path)

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

#     D = Djikstra(graph, 0)
#     D.djikstra()
