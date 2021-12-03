from Algos.graph import Graph
from Algos.Prims import Prims
from Algos.Djikstra import Djikstra
from Algos.Floyd import FloydWarshall
from Algos.Bellman import BellmanFord
from Algos.Kruskals import KruskalGraph
from Algos.cluster import Local_Clustering

from src.FileReader import ReadEngine

R = ReadEngine('input10.txt')
R.Read_Coordinates()
R.Cleanse_Edges()
R.Insert_Nodes()
R.Insert_Edges()

G = Graph(R.Total_nodes)
KG = KruskalGraph(R.Total_nodes)

for u,v,w in R.graph:
    G.add_edge(u,v,w)
    KG.add_edge(u,v,w)

Prims(G,R.src)
print()
Djikstra(G,R.src)
print()
FloydWarshall(G)
print()
BellmanFord(G,R.src)
print()
KG.KruskalMST()
print()
KG.boruvkaMST()
print()
Local_Clustering(R.G)
