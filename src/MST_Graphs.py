import networkx as nx
import matplotlib.pyplot as plt

class MST_Graph:
    def __init__(self,Index,X_points,Y_Points):
        self.X_points = X_points
        self.Y_points = Y_Points
        self.Index = Index

    def Prims_MST(self,parent,cost):
        g = nx.Graph()
        
        for i in self.Index:
            g.add_node(self.Index[i],pos=(self.X_points[i],self.Y_points[i]))

        for i in range(0,len(self.Index)):
            if parent[i]!=-1:
                g.add_edge(parent[i],i,weight=cost[i])

        pos=nx.get_node_attributes(g,'pos')
        nx.draw_networkx(g,pos)
        labels = nx.get_edge_attributes(g,'weight')
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()

    def Other_MST(self,mst):
        g = nx.Graph()
        
        for i in self.Index:
            g.add_node(self.Index[i],pos=(self.X_points[i],self.Y_points[i]))

        for u,v,w in mst:
            g.add_edge(u,v,weight=w)

        plt.figure(figsize=(300,150),dpi=80)
        pos=nx.get_node_attributes(g,'pos')
        nx.draw_networkx(g,pos)
        labels = nx.get_edge_attributes(g,'weight')
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()

    def MST_SRC_DEST(self,src,dest,parent,cost):
        g = nx.Graph()
        print(parent)       
        print(cost)

        g = nx.Graph()
        
        for i in self.Index:
            g.add_node(self.Index[i],pos=(self.X_points[i],self.Y_points[i]))

        test = []
        while True:
            if(parent[dest]==-1):
                break

            u = parent[dest]
            v = dest
            w = cost[dest]
            g.add_edge(u,v,weight=w)
            test.append([u,v,w])
            dest = u        

        plt.figure('Resultant Graph',figsize=(300,150),dpi=80)
        pos=nx.get_node_attributes(g,'pos')
        nx.draw_networkx(g,pos)
        labels = nx.get_edge_attributes(g,'weight')
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()
