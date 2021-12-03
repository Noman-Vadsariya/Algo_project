# Weighted Node
class AdjNode:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.next = None
        self.weight = weight


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, src, dest, weight):

        # if there is a link between two nodes, then consider this as edge in undirected graph. 
        # If there are two directed link b/w edges, then consider the edge with minimum cost.
        
        if not self.findVertex(src, dest):

            node = AdjNode(dest, weight)
            node.next = self.graph[src]
            self.graph[src] = node

            node = AdjNode(src,weight)
            node.next = self.graph[dest]
            self.graph[dest] = node
        
        else:
            if self.graph[src].weight > weight:
                self.deleteEdge(src,dest)
                self.deleteEdge(dest,src)

                
                node = AdjNode(dest, weight)
                node.next = self.graph[src]
                self.graph[src] = node

                node = AdjNode(src,weight)
                node.next = self.graph[dest]
                self.graph[dest] = node


    def deleteEdge(self,s,d):
        temp = self.graph[s]
        
        if (temp is not None):
            if (temp.vertex == d):
                self.graph[s] = temp.next
                temp = None
                return

        while (temp is not None):
            if temp.vertex == d:
                break
            prev = temp
            temp=temp.next

        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None

    def findVertex(self, s, d):
        temp = self.graph[s]
        while temp:
            if temp.vertex == d:
                return True
            temp = temp.next

        return False

    # Print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}( {} )".format(temp.vertex, temp.weight), end="")
                temp = temp.next
            print(" \n")


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
