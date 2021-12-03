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

    def Insert_Nodes(self):
        for i in self.Index:
            self.G.add_node(self.Index[i],pos=(self.X_points[i],self.Y_points[i]))
    
    def Insert_Edges(self):
        for u,v,w in self.graph:
            self.G.add_edge(u,v,weight=w)

    def Display_Graph(self):
        # plt.plot(self.X_points,self.Y_points,color='g')
        plt.figure(figsize=(200,100),dpi=80)
        plt.axis('on')
        nx.draw_networkx(self.G,with_labels=True,node_color='green')
        plt.show()

# if __name__ == '__main__':
#     F = FileHandling('input100.txt')
#     F.Read_Coordinates()
#     F.Cleanse_Edges()
#     F.Insert_Nodes()
#     F.Insert_Edges()
#     F.Display_Graph();