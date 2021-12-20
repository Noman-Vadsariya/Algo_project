import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.cluster import clustering

class Cluster:
    def __init__(self,G):
        self.G = G
        self.avg = 0

    def Local_Clustering(self):
        self.cluster = nx.clustering(self.G)
        sum = 0.0
        cnt = 0

        for key in self.cluster:
            sum += self.cluster[key]
            cnt += 1

        self.avg = sum/cnt