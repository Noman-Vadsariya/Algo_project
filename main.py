import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import math
from tkhtmlview import HTMLLabel

# File import
from src.FileReader import ReadEngine
from Algos.graph import Graph
from Algos.Prims import Prims
from Algos.Djikstra import Djikstra
from Algos.Floyd import Floyd
from Algos.Bellman import Ford
from Algos.Kruskals import KruskalGraph
from Algos.cluster import Cluster
from src.MST_Graphs import MST_Graph


Algorithms = [
    "Prims Algorithm",
    "Kruskal Algorithm",
    "Borůvka's Algorithm",
    "Dijkstra Algorithm",
    "Bellman Ford Algorithm",
    "Floyd Warshall",
    "Clustering Coefficient Algorithm",
]
NoOfNodes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


class Application:
    def __init__(self,root=None):
        super().__init__()
        # root = tk.Tk()
        self.HomePage(root)
        # self.title("ALGORITHMS & VISUALIZATION")
        # self.create_IntroWidgets()

    def HomePage(self,root):
        HeadingLabel = HTMLLabel(root, html = "<h1>Hello world</h1>")
        # ImageLabel = HTMLLabel(root, html = "<img src='https://www.google.com/imgres?imgurl=http%3A%2F%2Fprod-upp-image-read.ft.com%2F5242668e-93e9-11e8-95f8-8640db9060a7&imgrefurl=https%3A%2F%2Fwww.ft.com%2Fcontent%2F879d96d6-93db-11e8-95f8-8640db9060a7&tbnid=OABTFIgXBbXntM&vet=12ahUKEwihyOvo_dD0AhXGgM4BHXdiCI4QMygJegUIARDfAQ..i&docid=GOTNM2RwZVrV_M&w=2048&h=1152&itg=1&q=algorithms&ved=2ahUKEwihyOvo_dD0AhXGgM4BHXdiCI4QMygJegUIARDfAQ>")
        # HeadingLabel.grid(pady = 20)
        # ImageLabel.grid()
        self.des


    def Graph(self):
        filename = "input" + self.genreCombo.get() + ".txt"
        print(filename)
        R = ReadEngine(filename)
        R.Display_Graph()

    def create_IntroWidgets(self):
        # root = tk.Tk()
        headingLabel = tk.Label(self, text="Graph Visualization", font="Roboto 12")
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        ttk.Separator(self, orient="horizontal").grid(
            row=1, column=0, columnspan=5, sticky="ew"
        )

        tk.Label(self, text="Select no of Nodes: ").grid(row=2, column=3, padx=(10, 0))
        self.genreCombo = ttk.Combobox(
            self, width=18, values=list(NoOfNodes), state="readonly"
        )
        self.genreCombo.set("10")
        # self.genreCombo.bind('<<ComboboxSelected>>', self.showsimplegraph)
        self.genreCombo.grid(row=2, column=4, padx=(0, 10))
        ttk.Separator(self, orient="horizontal").grid(
            row=3, column=0, columnspan=5, sticky="ew"
        )
        B = tk.Button(self, text="View Graph", bd="5", command=self.Graph)
        B1 = tk.Button(
            self,
            text="Illustrate Algorithms",
            bd="5",
            command=lambda: [self.createWidgets()],
        )
        B2 = tk.Button(self, text="Exit", bd="5", command=self.destroy)
        B.grid(row=4, column=0)
        B1.grid(row=4, column=1)
        B2.grid(row=4, column=2)

    def showResult(self):

        filename = "input" + self.genreComboNodes.get() + ".txt"
        print(filename)
        R = ReadEngine(filename)
        R.Initialize()
        # R.Display_Graph()

        G = Graph(R.Total_nodes)
        KG = KruskalGraph(R.Total_nodes)

        for u, v, w in R.graph:
            G.add_edge(u, v, w)
            KG.add_edge(u, v, w)

        Algo = self.genreComboAlgo.get()
        res=""

        if Algo == Algorithms[0]:
            P = Prims(G, R.src)
            P.Prims_MST()
            res = "Minimum Spanning Tree Cost = {}".format(round(P.PrimCost,2))
        if Algo == Algorithms[1]:
            KG.KruskalMST()
            print("Minimum Spanning Tree Cost = {}".format(round(KG.KruskalCost,2)))
            res = "Minimum Spanning Tree Cost = {}".format(round(KG.KruskalCost,2))
        if Algo == Algorithms[2]:
            KG.BoruvkaMST()
            print("Minimum Spanning Tree Cost = {}".format(KG.boruvkaCost))
            res = "Minimum Spanning Tree Cost = {}".format(round(KG.boruvkaCost,2))
        
        if Algo == Algorithms[3]:
            D = Djikstra(G, R.src)
            D.djikstra()
            res = "SOURCE = {}\n\nNode\t|Cost\n".format(D.src)
            for i in range(G.V):
                res += "{}\t|\t{}\n".format(i,D.dist[i])

        if Algo == Algorithms[4]:
            BF = Ford(G, R.src)
            BF.BellmanFord()
            
            res = "SOURCE = {}\n\nNode\t|\tCost\n".format(BF.src)
            for i in range(G.V):
                res += "{}\t|\t{}\n".format(i,round(BF.val[i],2))

        if Algo == Algorithms[5]:
            F = Floyd(G)
            F.FloydWarshall()
            
            res = "         "
            for i in range(G.V):
                res+= "{}       ".format(i)
            res+="\n"
            for i in range(G.V):
                res+= "{0:.2f}  ".format(i)
                for j in range(G.V):
                    res+= "{0:.2f}  ".format(F.dist[i][j])
                res+="\n"

        if Algo == Algorithms[6]:
            L = Cluster(R.G)
            L.Local_Clustering()
            print("Average Clustering {0:.3f}".format(L.avg))        

        if Algo == Algorithms[0] or Algo == Algorithms[1] or Algo == Algorithms[2] or Algo == Algorithms[3] or Algo==Algorithms[4]:
            if Algo == Algorithms[0]:
                obj = P
                index = 0
            elif Algo == Algorithms[1]:
                obj = KG
                index = 1
            elif Algo == Algorithms[2]:
                obj = KG
                index=2
            elif Algo == Algorithms[3]:
                obj = D
                index = 3
            elif Algo == Algorithms[4]:
                obj = BF
                index = 4

            graphBtn = tk.Button(self.newwindow, text="View MST", bd="5", command=lambda: self.showMST(R,obj,index))
            graphBtn.grid(row=9, column=0)

        self.resultLabel = tk.Label(
            self.newwindow, text=res , font="San-Serif",borderwidth=2,relief="solid"
        )
        self.resultLabel.grid(row=11, column=0, columnspan=5, padx=10, pady=10, sticky="w")

    def showMST(self,R,obj,index):
        mst = MST_Graph(R.Index,R.X_points,R.Y_points)
        if index==0:
            mst.Prims_MST(obj.parent,obj.val)
        elif index==1:
            mst.Other_MST(obj.KruskalMst)
        elif index == 2:
            mst.Other_MST(obj.BoruvkaMst)
        elif index == 3 or index==4:
            mst.Other_MST(obj.path)

    def createWidgets(self):
        self.newwindow = tk.Toplevel()
        
        # self.root.destroy();
        # self.protocol('newwindow', self.quit)
        # self.destroy()
        # self.destroy()
        headingLabel = tk.Label(
            self.newwindow, text="ALGORITHMS & VISUALIZATION", font="Roboto 12"
        )
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        ttk.Separator(self.newwindow, orient="horizontal").grid(
            row=1, column=0, columnspan=5, sticky="ew"
        )

        # day = tk.Frame(self)
        # tk.Label(day, text="_______").pack()

        # tk.Label(day, text="TODAY", font='Helvetica 10 underline').pack()
        # tk.Label(day, text="").pack()
        # day.grid(row=2, column=0, padx=10)

        tk.Label(self.newwindow, text="Algorithms: ").grid(row=2, column=1, padx=(10, 0))
        self.genreComboAlgo = ttk.Combobox(
            self.newwindow, width=28, values=list(Algorithms), state="readonly"
        )
        self.genreComboAlgo.set(Algorithms[0])
        self.genreComboAlgo.grid(row=2, column=2)

        tk.Label(self.newwindow, text="Select no of Nodes: ").grid(
            row=2, column=3, padx=(10, 0)
        )
        self.genreComboNodes = ttk.Combobox(
            self.newwindow, width=18, values=list(NoOfNodes), state="readonly"
        )
        self.genreComboNodes.set("10")
        self.genreComboNodes.grid(row=2, column=4, padx=(0, 10))

        result = tk.Button(self.newwindow, text="View Results", bd="5", command=self.showResult)
        result.grid(row=7, column=0)

        ttk.Separator(self.newwindow, orient="horizontal").grid(
            row=3, column=0, columnspan=5, sticky="ew"
        )


app = Application()
# root = 
app.mainloop()