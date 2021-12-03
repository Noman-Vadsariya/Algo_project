import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.cluster import clustering

def Local_Clustering(G):
    cluster = nx.clustering(G)
    sum = 0.0
    cnt = 0

    for key in cluster:
        sum += cluster[key]
        cnt += 1

    avg = sum/cnt

    print("Average Clustering {0:.3f}".format(avg))