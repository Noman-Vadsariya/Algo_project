import re
from matplotlib import scale
from matplotlib.markers import MarkerStyle
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.shortest_paths import weighted

class ReadEngine:
    filename = 'benchmark/';
    Total_nodes = 0;
    Index = [];
    X_points = [];
    Y_points = [];
     
    def __init__(self, filename):
        self.filename = self.filename + filename;
        self.G = nx.Graph()
        self.graph = []
        self.altGraph = [] 
        self.src = None
        # print(filename);
        # print(self.filename);
     
    def Read_Coordinates(self):
        with open(self.filename, 'r') as f:
            f.readline();
            f.readline();
            self.Total_nodes = int(f.readline());
            f.readline();
            print('Total Nodes: ',self.Total_nodes)
            for i in range(int(self.Total_nodes)):
                line = f.readline()
                # print(lines)
                split_string = line.split();
                # print(split_string)
                self.Index.append(int (split_string[0]));
                self. X_points.append(float(split_string[1])*10);
                self.Y_points.append(float(split_string[2])*10);
            
            f.readline()
            
            for i in range(int(self.Total_nodes)):
                line = f.readline()
                split = line.split()
                # print(split_string)
                
                # print(int(split[0]))
                j=1
                while j<len(split):
                    # print(int(split[j]),end=" ")
                    u = (int(split[0]))
                    v = (int(split[j]))
                    j+=2
                    # print(float(split[j])/10000000,end="    ")
                    w = (float(split[j])/10000000)
                    j+=2                    

                    self.graph.append([u,v,w])
                    w = round(1/w,4)
                    self.altGraph.append([u,v,w]) #for bellman ford and Floyd Warshall
                # print()

            f.readline()

            self.src = int(f.readline())
            # print(self.src)


    def Cleanse_Edges(self):
        # if there is a link between two nodes, then consider this as edge in undirected graph. 
        # If there are two directed link b/w edges, then consider the edge with minimum cost.
        # If source==dest cost=0

        for u,v,w in self.graph:
            if u == v:
                self.graph.remove([u,v,w])
                w = round(1/w,4)
                self.altGraph.remove([u,v,w])

    def Insert_Nodes(self):
        for i in self.Index:
            self.G.add_node(self.Index[i],pos=(self.X_points[i],self.Y_points[i]))
    
    def Insert_Edges(self):
        for u,v,w in self.graph:
            self.G.add_edge(u,v,weight=w)

    def Initialize(self):
        self.X_points.clear()
        self.Y_points.clear()
        self.Index.clear()
        self.G = nx.Graph()
        self.graph.clear()
        self.src = None

        self.Read_Coordinates()
        self.Insert_Nodes()
        self.Cleanse_Edges()
        self.Insert_Edges()
        
    def Display_Graph(self):
                
        self.X_points.clear()
        self.Y_points.clear()
        self.Index.clear()
        self.G = nx.Graph()
        self.graph.clear()
        self.src = None

        self.Read_Coordinates()
        self.Insert_Nodes()
        self.Cleanse_Edges()
        self.Insert_Edges()
        
        # plt.figure()
        plt.figure('Figure-{} Nodes'.format(self.Total_nodes),figsize=(300,150),dpi=80)

        pos=nx.get_node_attributes(self.G,'pos')
        nx.draw_networkx(self.G,pos)
        labels = nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx_edge_labels(self.G,pos,edge_labels=labels)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()