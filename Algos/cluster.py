import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.cluster import clustering

A = [0,0,1,1,7,2,8,7,2,2,3,6,5,3]
B = [1,7,7,2,6,8,6,8,5,3,5,5,4,4]
W = [4,8,11,8,1,2,6,7,4,7,14,2,10,9]

G=nx.Graph();

for i in range(len(A)):
    G.add_edge(A[i],B[i],weight=W[i])

# print(G.edges(data=True)) 

# plt.figure(figsize =(9, 9))
# nx.draw(G,with_labels=True,node_color='green')
# plt.show()

cluster = nx.clustering(G)
sum = 0.0
cnt = 0

for key in cluster:
    sum += cluster[key]
    cnt += 1

avg = sum/cnt

print("Average Clustering {0:.3f}".format(avg))