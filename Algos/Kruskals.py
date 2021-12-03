from collections import defaultdict


class Graph:

    def __init__(self, vertices):
	    self.V = vertices # No. of vertices
	    self.graph = [] # default dictionary
	    # to store graph

	# function to add an edge to graph
    def add_edge(self, u, v, w):

        for src,dest,weight in self.graph:
            if(u==dest and v==src and weight>w):
                self.graph.remove([src,dest,weight])
                self.graph.append([u, v, w])
                return
            elif (u==dest and v==src and weight<w):
                return

        self.graph.append([u, v, w])

    def printGraph(self):
        for u,v,w in self.graph:
            print("%d -- %d == %d" % (u, v, w)) 

	# A utility function to find set of an element i
	# (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

	# A function that does union of two sets of x and y
	# (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

		# Attach smaller rank tree under root of
		# high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

        # The main function to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):

        result = [] # This will store the resultant MST

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Step 1: Sort all the edges in
        # non-decreasing order of their
        # weight. If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't
            # cause cycle, include it in result
            # and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        minimumCost = 0
        print ("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)


if __name__ == "__main__":
    V = 9

    # Create graph and edges
    graph = Graph(V)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(0, 1, 4)
    graph.addEdge(1, 2, 8)
    graph.addEdge(7, 6, 1)
    graph.addEdge(2, 8, 2)
    graph.addEdge(8, 6, 6)
    graph.addEdge(7, 8, 7)
    graph.addEdge(2, 5, 4)
    graph.addEdge(2, 3, 7)
    graph.addEdge(3, 5, 14)
    graph.addEdge(6, 5, 2)
    graph.addEdge(5, 4, 10)
    graph.addEdge(3, 4, 9)

    graph.printGraph()
    graph.KruskalMST()
