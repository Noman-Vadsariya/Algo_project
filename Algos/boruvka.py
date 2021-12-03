from collections import defaultdict

class Graph:

	def __init__(self,vertices):
		self.V= vertices 
		self.graph = [] 
		

	# function to add an edge to graph
	def add_edge(self,u,v,w):
		for src,dest,weight in self.graph:
			if(u==dest and v==src and weight>w):
				self.graph.remove([src,dest,weight])
				self.graph.append([u, v, w])
				return
			elif (u==dest and v==src and weight<w):
				return

		self.graph.append([u, v, w])

	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else :
			parent[yroot] = xroot
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's algorithm
	def boruvkaMST(self):
		parent = []; rank = [];

		cheapest =[]
		result = []

		numTrees = self.V
		MSTweight = 0

		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)
			cheapest =[-1] * self.V

		while numTrees > 1:

			for i in range(len(self.graph)):

				u,v,w = self.graph[i]
				set1 = self.find(parent, u)
				set2 = self.find(parent ,v)

				if set1 != set2:	
					
					if cheapest[set1] == -1 or cheapest[set1][2] > w :
						cheapest[set1] = [u,v,w]

					if cheapest[set2] == -1 or cheapest[set2][2] > w :
						cheapest[set2] = [u,v,w]

			# Consider the above picked cheapest edges and add them
			# to MST
			for node in range(self.V):

				#Check if cheapest for current set exists
				if cheapest[node] != -1:
					u,v,w = cheapest[node]
					set1 = self.find(parent, u)
					set2 = self.find(parent ,v)

					if set1 != set2 :
						MSTweight += w
						self.union(parent, rank, set1, set2)
						result.append([u,v,w])
						print ("Edge %d-%d with weight %d included in MST" % (u,v,w))
						numTrees = numTrees - 1
			
			#reset cheapest array
			cheapest =[-1] * self.V

			
		print ("Weight of MST is %d" % MSTweight)
		print(result)
							

if __name__ == "__main__":
	V = 9

	# Create graph and edges
	graph = Graph(V)
	graph.addEdge(0, 1, 4)
	graph.addEdge(0, 7, 8)
	graph.addEdge(1, 7, 11)
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

	# graph.print_graph()

	graph.boruvkaMST()
#This code is contributed by Neelam Yadav
