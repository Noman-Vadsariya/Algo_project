from os import stat
from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser

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

bgColor = '#396EB0'
fgColor = '#FFA400'

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
    def __init__(self,master=None):
        super().__init__()
        self.master = master
        self.HomePage(master)
        self.resultLabel = None

    def callback(self, url):
        webbrowser.open_new(url)

    def HomePage(self,root):
        
        #Heading & Text Labels
        MainHeadingLabel = tk.Label(root,text="Graph Analysis & Simulator",bg=bgColor, fg=fgColor,font=('TimesNew Roman bold',30,'bold', 'underline')).pack(pady=20);
        DescriptionHeadingLabel = tk.Label(root, text="Project-Description: ", bg=bgColor ,fg=fgColor, font=('TimesNew Roman bold',18,'bold', 'underline'),anchor='w').pack(fill='both');
        DescriptionTextLabel = tk.Label(root, text="'Graphs are a widely used model to describe structural relations. They are built of nodes, which are connected by edges (both directed or undirected). This Graph Simulator simulates different graph algorithms including Maximum Spanning Tree Algorithm, Shortest Path Algorithm and Local Node Clustering Algorithms on a benchmark having graphs with increasing no of nodes. The simulator also provides graphing utility to visualize input and resultant graphs.'", bg=bgColor ,fg=fgColor, font = ('TimesNew Roman bold',14,'bold'),wraplengt=1000).pack(pady=20);
        AlgorithmsHeadingLabel = tk.Label(root, text= "Algorithms:",bg=bgColor, fg=fgColor, font=('TimesNew Roman bold',16,'bold', 'underline'),anchor='w').pack(fill='both') 
        AlgorithmsTextLabel = tk.Label(root, text="The Algorithms that could be used in analysis of graph are:", bg=bgColor, fg=fgColor, font = ('TimesNew Roman bold',12,'bold'),anchor='w').pack(pady=20,ipadx=20);
        
        #HyperLinks
        #1
        PrimsLabel = tk.Label(root, text="• Prim's Algorithm",bg=bgColor, fg=fgColor, cursor="hand2", font = ('TimesNew Roman bold',12))
        PrimsLabel.pack()
        PrimsLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Prim%27s_algorithm"))
        #2
        KruskalLabel = tk.Label(root, text="• Kruskal's Algorithm",bg=bgColor, fg=fgColor, cursor="hand2", font = ('TimesNew Roman bold',12))
        KruskalLabel.pack()
        KruskalLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Kruskal%27s_algorithm"))
        #3
        DijkstraLabel = tk.Label(root, text="• Dijkstra's Algorithm",bg=bgColor, fg=fgColor, cursor="hand2", font = ('TimesNew Roman bold',12))
        DijkstraLabel.pack()
        DijkstraLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm"))
        #4
        BellmanFordLabel = tk.Label(root, text="• BellmanFord's Algorithm",bg=bgColor, fg=fgColor, cursor="hand2", font = ('TimesNew Roman bold',12))
        BellmanFordLabel.pack()
        BellmanFordLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm"))
        #5
        FloydWarshallLabel = tk.Label(root, text="• FloydWarshall's Algorithm",bg=bgColor, fg=fgColor, cursor="hand2", font = ('TimesNew Roman bold',12))
        FloydWarshallLabel.pack()
        FloydWarshallLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm"))
        #6
        ClusteringCoefficientLabel = tk.Label(root, text="• Clustering Coefficient Algorithm",bg=bgColor, fg=fgColor, cursor="hand2", font = ('TimesNew Roman bold',12))
        ClusteringCoefficientLabel.pack()
        ClusteringCoefficientLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Clustering_coefficient"))
        #7
        BorůvkaLabel = tk.Label(root, text="• Borůvka's Algorithm",bg=bgColor, fg=fgColor, cursor="hand2", font = ('TimesNew Roman bold',12))
        BorůvkaLabel.pack()
        BorůvkaLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm"))
        
        #Buttons
        ExitButton = tk.Button(root, text="Exit", bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command=root.destroy).place(x=520, y=600)
        ProceedToGraphButton = tk.Button(root, text="Illustrate Graphs", bd="8",font=('TimesNew Roman bold',12,'bold'), fg=fgColor, command=self.MainPage).place(x=620, y=600)
        ProceedToAlgorithmsButton = tk.Button(root, text="Analyze Algorithms", bd="8",font=('TimesNew Roman bold',12,'bold'), fg=fgColor, command=self.AlgorithmPage).place(x=820, y=600)
    
    def MainPage(self):
        #Setting of Home and current Page
        self.MainWindow = tk.Toplevel(self.master)
        self.MainWindow.title('Graph Visualization')
        self.MainWindow.state('zoomed')
        self.MainWindow.configure(bg=bgColor)
        self.master.withdraw()

        #Headings annd Note Labels and text
        MainHeadingLabel = tk.Label(self.MainWindow,text="Graph Visualization",bg=bgColor, fg=fgColor,font=('TimesNew Roman bold',28,'bold', 'underline')).pack(pady=20);
        NoteLabel = tk.Label(self.MainWindow, text="Note: ",bg=bgColor, fg=fgColor, font=('TimesNew Roman bold',15,'bold', 'underline'),anchor='w').pack(fill='both');
        NoteTextLabel = tk.Label(self.MainWindow, text="You can select number of nodes to be illustrated on a graph from many options given below..", bg= bgColor, fg= 'White', font = ('TimesNew Roman bold',12),wraplengt=1000).place(x=75,y=95);
        #Combo Label and ComboBox
        InputLabel = tk.Label(self.MainWindow, text="Select no of Nodes: ",bg=bgColor, fg=fgColor,font=('TimesNew Roman bold',12)).place(x=400,y=178)
        self.genreCombo = ttk.Combobox(self.MainWindow, width=25, values=list(NoOfNodes), state="readonly")
        self.genreCombo.set("10")
        self.genreCombo.place(x=550,y=180)
        
        #Buttons
        ExitButton = tk.Button(self.MainWindow, text="Exit", bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command=self.master.destroy).place(x=450, y=250)
        ViewGraphButton = tk.Button(self.MainWindow, text="View Graph", bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command=self.ViewGraph).place(x=520, y=250)
        BackButton = tk.Button(self.MainWindow, text="BACK", bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command=lambda: [self.master.deiconify(),self.master.state('zoomed'),self.MainWindow.destroy()]).place(x=0, y=0)
   
    def ViewGraph(self):
        filename = "input" + self.genreCombo.get() + ".txt"
        print(filename)
        R = ReadEngine(filename)
        R.Display_Graph()

    def AlgorithmPage(self):
        #Setting of Home & Current Page
        self.AlgorithmWindow = tk.Toplevel(self.master)
        self.AlgorithmWindow.title('Algorithms Analysis')
        self.AlgorithmWindow.state('zoomed')
        self.AlgorithmWindow.configure(bg=bgColor)
        self.master.withdraw()
        #MainHeading and Input Label and Text
        MainHeadingLabel = tk.Label(self.AlgorithmWindow,text="Analyze Algorithms",bg=bgColor, fg=fgColor,font=('TimesNew Roman bold',28,'bold', 'underline')).pack(pady=20);
        NoteLabel = tk.Label(self.AlgorithmWindow, text="Note: ",bg=bgColor, fg=fgColor, font=('TimesNew Roman bold',15,'bold', 'underline'),anchor='w').pack(fill='both');
        NoteTextLabel = tk.Label(self.AlgorithmWindow, text="You can select number of nodes to be illustrated and select any algorithm from many options given below..", bg= bgColor, fg= 'White', font = ('TimesNew Roman bold',12),wraplengt=1000).place(x=75,y=95);
        #ComboBox1
        InputLabel = tk.Label(self.AlgorithmWindow, text="Select no of Nodes: ",bg=bgColor, fg=fgColor,font=('TimesNew Roman bold',12)).place(x=250,y=180)
        self.genreComboNodes = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(NoOfNodes))
        self.genreComboNodes.set("10")
        self.genreComboNodes.place(x=400,y=180)
        #ComboBox2
        Inputlabel1 = tk.Label(self.AlgorithmWindow, text="Select Algorithm: ",bg=bgColor, fg=fgColor,font=('TimesNew Roman bold',12)).place(x=580,y=180)
        self.genreComboAlgo = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(Algorithms))
        self.genreComboAlgo.set("Prims Algorithm")
        self.genreComboAlgo.place(x=730,y=180)

        BackButton = tk.Button(self.AlgorithmWindow, text="BACK", bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command=lambda: [self.master.deiconify(),self.master.state('zoomed'),self.AlgorithmWindow.destroy()]).place(x=0, y=0)
        self.nextBtn = tk.Button(self.AlgorithmWindow, text="Next", bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command= self.selectNodes).place(x=600, y=250)

    def selectNodes(self):

        Algo = self.genreComboAlgo.get()

        filename = "input" + self.genreComboNodes.get() + ".txt"
        print(filename)
        self.R = ReadEngine(filename)
        self.R.Initialize()

        self.genreComboAlgo.config(state="disabled")
        self.genreComboNodes.config(state="disabled")

        self.SRC_Nodes = []
        self.DEST_Nodes = ['ALL']

        for i in range(self.R.Total_nodes):
            self.SRC_Nodes.append(i)
            self.DEST_Nodes.append(i)

        SrcLabel = tk.Label(self.AlgorithmWindow, text="Source Node: ",bg=bgColor, fg=fgColor,font=('TimesNew Roman bold',12)).place(x=250,y=350)
        self.srcGenreCombo = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(self.SRC_Nodes))
        self.srcGenreCombo.set("1")
        self.srcGenreCombo.place(x=400,y=350)

        DescLabel = tk.Label(self.AlgorithmWindow, text="Destination Nodes: ",bg=bgColor, fg=fgColor,font=('TimesNew Roman bold',12)).place(x=580,y=350)
        self.destGenreCombo = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(self.DEST_Nodes))
        self.destGenreCombo.set("ALL")
        self.destGenreCombo.place(x=730,y=350)
        if Algo == Algorithms[0] or Algo == Algorithms[1] or Algo == Algorithms[2]:
            self.destGenreCombo.config(state="disabled")

        if Algo == Algorithms[6] or Algo == Algorithms[5]:
            self.srcGenreCombo.config(state="disabled")
            self.destGenreCombo.config(state="disabled")
            self.ViewGraphButton = tk.Button(self.AlgorithmWindow, text="View Graph", bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command=lambda: [self.ViewAlgoGraph(1)],state="disabled").place(x=600, y=450)
        else:
            self.ViewGraphButton = tk.Button(self.AlgorithmWindow, text="View Graph", bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command=lambda: [self.ViewAlgoGraph(1)]).place(x=600, y=450)
            
        self.ViewResultButton = tk.Button(self.AlgorithmWindow, text="View Result", bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command=lambda: [self.ViewAlgoGraph(0)]).place(x=450, y=450)

    def ViewAlgoGraph(self,Pos):

        self.resultLabelFlag = True

        G = Graph(self.R.Total_nodes)
        altG = Graph(self.R.Total_nodes)
        KG = KruskalGraph(self.R.Total_nodes)

        for u,v,w in self.R.graph:
            G.add_edge(u,v,w)
            KG.add_edge(u,v,w)

        for u,v,w in self.R.altGraph:
            altG.add_edge(u,v,w)

        Algo = self.genreComboAlgo.get()
        res=""
        
        Src = self.srcGenreCombo.get()
        dest = self.destGenreCombo.get()
        self.R.src = int(Src)
        print(self.R.src)

        if Algo == Algorithms[0]:
            P = Prims(G, self.R.src)
            P.Prims_MST()
            res = "Maximum Spanning Tree Cost = {}".format(round(P.PrimCost,2))
        if Algo == Algorithms[1]:
            KG.KruskalMST()
            print("Maximum Spanning Tree Cost = {}".format(round(KG.KruskalCost,2)))
            res = "Maximum Spanning Tree Cost = {}".format(round(KG.KruskalCost,2))
        if Algo == Algorithms[2]:
            KG.BoruvkaMST()
            print("Maximum Spanning Tree Cost = {}".format(KG.boruvkaCost))
            res = "Maximum Spanning Tree Cost = {}".format(round(KG.boruvkaCost,2))
        
        if Algo == Algorithms[3]:
            D = Djikstra(G, self.R.src)
            D.djikstra()

            if self.resultLabel is not None:
                self.resultLabel.destroy()

            if(Pos==0):   
                if dest != 'ALL':
                    d = int(dest)
                    print("Maximum Spanning Tree Cost = {}".format(D.cost[d]))
                    res = "Cost from {} to {} = {}".format(D.src,d,round(D.cost[d],2))
                else:
                    self.resultLabelFlag=False
                    ws  = Tk()
                    ws.state('zoomed')
                    ws.title('DIJIKSTRA RESULT')
                    ws['bg'] = '#AC99F2'
                    game_frame = ttk.Frame(ws)
                    game_frame.pack(fill='both', expand=True)
                    #scrollbar
                    h = Scrollbar(game_frame,orient='horizontal')
                    h.pack(side= BOTTOM,fill=X)

                    v = Scrollbar(game_frame)
                    v.pack(side=RIGHT, fill=Y)

                    my_game = ttk.Treeview(game_frame,xscrollcommand=h.set, yscrollcommand =v.set)


                    my_game.pack(fill='both', expand=True)

                    h.config(command=my_game.xview)
                    v.config(command=my_game.yview)
                    #define our column
                    
                    my_game['columns'] = ('Sno_Nodes', 'costs_of_nodes')

                    # format our column
                    my_game.column("#0", width=0,  stretch=NO)
                    my_game.column("Sno_Nodes",anchor=CENTER, width=80)
                    my_game.column("costs_of_nodes",anchor=CENTER, width=80)
                    
                    #Create Headings 
                    my_game.heading("#0",text="Id",anchor=CENTER)
                    my_game.heading("Sno_Nodes",text="Nodes",anchor=CENTER)
                    my_game.heading("costs_of_nodes",text="Costs",anchor=CENTER)
                    for i in range(G.V):
                        res = format(D.dist[i],'.2f')
                        my_game.insert(parent='',index='end',iid=i-1,text='', values=([i, res]))
                    my_game.pack()
                # my_game.place (x=200,y=200)


        if Algo == Algorithms[4]:
            BF = Ford(altG, self.R.src)
            BF.BellmanFord()

            if self.resultLabel is not None:
                self.resultLabel.destroy()

            if(Pos==0):   
                if dest != 'ALL':
                    d = int(dest)
                    print("Maximum Spanning Tree Cost = {}".format(BF.cost[d]))
                    res = "Cost from {} to {} = {}".format(BF.src,d,round(BF.cost[d]*10,2))
                else:
                    self.resultLabelFlag=False
                    ws  = Tk()
                    ws.state('zoomed')
                    ws.title('BELLMANFORD RESULT')
                    # ws.geometry('500x500')
                    ws['bg'] = '#AC99F2'

                    game_frame = ttk.Frame(ws)
                    game_frame.pack(fill='both', expand=True)
                    #scrollbar
                    h = Scrollbar(game_frame,orient='horizontal')
                    h.pack(side= BOTTOM,fill=X)

                    v = Scrollbar(game_frame)
                    v.pack(side=RIGHT, fill=Y)

                    my_game = ttk.Treeview(game_frame,xscrollcommand=h.set, yscrollcommand =v.set)


                    my_game.pack(fill='both', expand=True)

                    h.config(command=my_game.xview)
                    v.config(command=my_game.yview)
                    #define our column
                    
                    my_game['columns'] = ('Sno_Nodes', 'costs_of_nodes')

                    # format our column
                    my_game.column("#0", width=0,  stretch=NO)
                    my_game.column("Sno_Nodes",anchor=CENTER, width=80)
                    my_game.column("costs_of_nodes",anchor=CENTER, width=80)
                    
                    #Create Headings 
                    my_game.heading("#0",text="Id",anchor=CENTER)
                    my_game.heading("Sno_Nodes",text="Nodes",anchor=CENTER)
                    my_game.heading("costs_of_nodes",text="Costs",anchor=CENTER)

                    for i in range(G.V):
                        res = format(BF.val[i]*10,'.4f')
                        # res +=  format(i) + "\t|\t"  + format(BF.val[i],'.2f') + '\n'
                        my_game.insert(parent='',index='end',iid=i-1,text='', values=([i, res]))
                    my_game.pack()

        if Algo == Algorithms[5]:
            F = Floyd(altG)
            F.FloydWarshall()

            if(Pos==0):
                self.resultLabelFlag = False
                ws  = Tk()
                ws.state('zoomed')
                ws.title('FLOYDWARSHALL RESULT')
                ws['bg'] = '#AC99F2'

                game_frame = ttk.Frame(ws)
                game_frame.pack(fill='both', expand=True)
                #scrollbar
                h = Scrollbar(game_frame,orient='horizontal')
                h.pack(side= BOTTOM,fill=X)

                v = Scrollbar(game_frame)
                v.pack(side=RIGHT, fill=Y)

                my_game = ttk.Treeview(game_frame,xscrollcommand=h.set, yscrollcommand =v.set)


                my_game.pack(fill='both', expand=True)

                h.config(command=my_game.xview)
                v.config(command=my_game.yview)
                #define our column
                
                col = []    
                
                for i in range(G.V+1):
                    s = "{}".format(i)
                    col.append(s)

                print(col)
                col = tuple(col)
                print(col)

                my_game['columns']=col
                # # f)ormat our column

                my_game.column("#0",width=0,  stretch=NO)

                for i in range(G.V+1):
                    my_game.column("{}".format(i),anchor=CENTER)

                my_game.heading(0,text="",anchor=CENTER)
                
                for i in range(G.V):
                    my_game.heading("{}".format(i+1),text="{}".format(i),anchor=CENTER)

                array = []
                for i in range(G.V):
                    array.append(i)
                    # res+= "{0:.2f}  ".format(i)
                    for j in range(G.V):
                        array.append(format(F.dist[i][j]*10,'.4f'))
                    array = tuple(array)
                    print(array)
                    my_game.insert(parent='',index='end',iid=i, values=array)
                    array = list(array)
                    array.clear()

                    my_game.pack()
                    
        if Algo == Algorithms[6]:
            L = Cluster(self.R.G)
            L.Local_Clustering()
            res += "Average Clustering Cost = {0:.3f}".format(L.avg)      

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
        if(Pos==1):
            if(dest=='ALL'):
                self.showMST(self.R,obj,index)
            else:
                self.showMST(self.R,obj,index,self.R.src,int(dest))
        
        elif(Pos==0):
            if(self.resultLabelFlag):
                self.resultLabel = tk.Label(
                self.AlgorithmWindow, text=res , font="San-Serif",borderwidth=2,relief="solid"
                )
                self.resultLabel.place(x = 550, y = 550)

        self.resetBtn = tk.Button(self.AlgorithmWindow, text="Select Next Algo",bd="8", font=('TimesNew Roman bold',12,'bold'),fg=fgColor, command = lambda : [self.resetStates(Algo)]).place(x=750,y=450)
            #New Window

    def resetStates(self, Algo):
        self.genreComboAlgo.config(state="normal")
        self.genreComboNodes.config(state="normal")

        if(self.resultLabel is not None):
            self.resultLabel.destroy()

        if(Algo != Algorithms[6]):
            self.srcGenreCombo.config(state="disabled")
            self.destGenreCombo.config(state="disabled")

        

    def showMST(self,R,obj,index,src=None,dest=None):
        mst = MST_Graph(R.Index,R.X_points,R.Y_points)
        if index==0:
            mst.Prims_MST(obj.parent,obj.val)
        elif index==1:
            mst.Other_MST(obj.KruskalMst)
        elif index == 2:
            mst.Other_MST(obj.BoruvkaMst)
        elif (index == 3 or index==4) and dest is None:
            mst.Other_MST(obj.path)
        elif (index==3 or index==4) and dest is not None:
            mst.MST_SRC_DEST(src,dest,obj.parent,obj.cost)

root = tk.Tk()
root.iconify()
root.title('HomePage')
root.state('zoomed')
root.configure(bg=bgColor)
app = Application(root)
root.mainloop()