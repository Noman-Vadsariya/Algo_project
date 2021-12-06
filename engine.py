from Algos.graph import Graph
from Algos.Prims import Prims
from Algos.Djikstra import Djikstra
from Algos.Floyd import Floyd
from Algos.Bellman import Ford
from Algos.Kruskals import KruskalGraph
from Algos.cluster import Cluster
from src.MST_Graphs import MST_Graph

from src.FileReader import ReadEngine

R = ReadEngine('input10.txt')
R.Initialize()
# R.Display_Graph()

G = Graph(R.Total_nodes)
KG = KruskalGraph(R.Total_nodes)

for u,v,w in R.graph:
    G.add_edge(u,v,w)
    KG.add_edge(u,v,w)

# P = Prims(G,R.src)
# P.Prims_MST()
# KG.KruskalMST()
# KG.boruvkaMST()

# print()
D = Djikstra(G,R.src)
D.djikstra()

# print()
# FloydWarshall(G)
# print()
# BellmanFord(G,R.src)
# print()
# print()
# print()
# Local_Clustering(R.G)


# MST GRAPHS
# mst = MST_Graph(R.Index,R.X_points,R.Y_points)
# mst.Prims_MST(P.parent,P.val)
# mst.Other_MST(KG.KruskalMst)
# mst.Other_MST(KG.BoruvkaMst)
