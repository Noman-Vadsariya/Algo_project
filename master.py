from tkinter import *
import tkinter as tk
from tkinter import ttk
from prettytable import PrettyTable
# from tkinter.constants import LEFT
# from matplotlib.pyplot import text
# from tkhtmlview import HTMLLabel
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

    def callback(self, url):
        webbrowser.open_new(url)

    def HomePage(self,root):
        
        #Heading & Text Labels
        MainHeadingLabel = tk.Label(root,text="Graph Analysis & Simulator",bg='#396EB0', fg="#F58840",font=('TimesNew Roman bold',30,'bold', 'underline')).pack(pady=20);
        DescriptionHeadingLabel = tk.Label(root, text="Project-Description: ", bg='#396EB0' ,fg="#F58840", font=('TimesNew Roman bold',18,'bold', 'underline'),anchor='w').pack(fill='both');
        DescriptionTextLabel = tk.Label(root, text="'Graphs are a widely used model to describe structural relations. They are built of nodes, which are connected by edges (both directed or undirected). This Graph Simulator simulates different graph algorithms including Minimum Spanning Tree Algorithm, Shortest Path Algorithm and Local Node Clustering Algorithms on a benchmark having graphs with increasing no of nodes. The simulator also provides graphing utility to visualize input and resultant graphs.'", bg='#396EB0' ,fg="#F58840", font = ('TimesNew Roman bold',14,'bold'),wraplengt=1000).pack(pady=20);
        AlgorithmsHeadingLabel = tk.Label(root, text= "Algorithms:",bg='#396EB0', fg="#F58840", font=('TimesNew Roman bold',16,'bold', 'underline'),anchor='w').pack(fill='both') 
        AlgorithmsTextLabel = tk.Label(root, text="The Algorithms that could be used in analysis of graph are:", bg='#396EB0', fg="#F58840", font = ('TimesNew Roman bold',12,'bold'),anchor='w').pack(pady=20,ipadx=20);
        
        #HyperLinks
        #1
        PrimsLabel = tk.Label(root, text="• Prim's Algorithm",bg='#396EB0', fg="#F58840", cursor="hand2", font = ('TimesNew Roman bold',12))
        PrimsLabel.pack()
        PrimsLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Prim%27s_algorithm"))
        #2
        KruskalLabel = tk.Label(root, text="• Kruskal's Algorithm",bg='#396EB0', fg="#F58840", cursor="hand2", font = ('TimesNew Roman bold',12))
        KruskalLabel.pack()
        KruskalLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Kruskal%27s_algorithm"))
        #3
        DijkstraLabel = tk.Label(root, text="• Dijkstra's Algorithm",bg='#396EB0', fg="#F58840", cursor="hand2", font = ('TimesNew Roman bold',12))
        DijkstraLabel.pack()
        DijkstraLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm"))
        #4
        BellmanFordLabel = tk.Label(root, text="• BellmanFord's Algorithm",bg='#396EB0', fg="#F58840", cursor="hand2", font = ('TimesNew Roman bold',12))
        BellmanFordLabel.pack()
        BellmanFordLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm"))
        #5
        FloydWarshallLabel = tk.Label(root, text="• FloydWarshall's Algorithm",bg='#396EB0', fg="#F58840", cursor="hand2", font = ('TimesNew Roman bold',12))
        FloydWarshallLabel.pack()
        FloydWarshallLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm"))
        #6
        ClusteringCoefficientLabel = tk.Label(root, text="• Clustering Coefficient Algorithm",bg='#396EB0', fg="#F58840", cursor="hand2", font = ('TimesNew Roman bold',12))
        ClusteringCoefficientLabel.pack()
        ClusteringCoefficientLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Clustering_coefficient"))
        #7
        BorůvkaLabel = tk.Label(root, text="• Borůvka's Algorithm",bg='#396EB0', fg="#F58840", cursor="hand2", font = ('TimesNew Roman bold',12))
        BorůvkaLabel.pack()
        BorůvkaLabel.bind("<Button-1>", lambda e: self.callback("https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm"))
        
        #Buttons
        ExitButton = tk.Button(root, text="Exit", bd="8", font=('TimesNew Roman bold',12,'bold'),fg="red", command=root.destroy).place(x=520, y=600)
        ProceedToGraphButton = tk.Button(root, text="Illustrate Graphs", bd="8",font=('TimesNew Roman bold',12,'bold'), fg="red", command=self.MainPage).place(x=620, y=600)
        ProceedToAlgorithmsButton = tk.Button(root, text="Analyze Algorithms", bd="8",font=('TimesNew Roman bold',12,'bold'), fg="red", command=self.AlgorithmPage).place(x=820, y=600)
    
    def MainPage(self):
        #Setting of Home and current Page
        self.MainWindow = tk.Toplevel(self.master)
        self.MainWindow.title('Graph Visualization')
        self.MainWindow.state('zoomed')
        self.MainWindow.configure(bg='black')
        self.master.withdraw()
        #Headings annd Note Labels and text
        MainHeadingLabel = tk.Label(self.MainWindow,text="Graph Visualization",bg='black', fg="red",font=('TimesNew Roman bold',28,'bold', 'underline')).pack(pady=20);
        NoteLabel = tk.Label(self.MainWindow, text="Note: ",bg='black', fg="red", font=('TimesNew Roman bold',15,'bold', 'underline'),anchor='w').pack(fill='both');
        NoteTextLabel = tk.Label(self.MainWindow, text="You can select number of nodes to be illustrated on a graph from many options given below..", bg= 'Black', fg= 'White', font = ('TimesNew Roman bold',12),wraplengt=1000).place(x=75,y=95);
        #Combo Label and ComboBox
        InputLabel = tk.Label(self.MainWindow, text="Select no of Nodes: ",bg='black', fg="red",font=('TimesNew Roman bold',12)).place(x=400,y=178)
        self.genreCombo = ttk.Combobox(self.MainWindow, width=25, values=list(NoOfNodes), state="readonly")
        self.genreCombo.set("10")
        self.genreCombo.place(x=550,y=180)
        #Buttons
        ExitButton = tk.Button(self.MainWindow, text="Exit", bd="8", font=('TimesNew Roman bold',12,'bold'),fg="red", command=self.master.destroy).place(x=450, y=250)
        ViewGraphButton = tk.Button(self.MainWindow, text="View Graph", bd="8", font=('TimesNew Roman bold',12,'bold'),fg="red", command=self.ViewGraph).place(x=520, y=250)
        BackButton = tk.Button(self.MainWindow, text="BACK", bd="8", font=('TimesNew Roman bold',12,'bold'),fg="red", command=lambda: [self.master.deiconify(),self.master.state('zoomed'),self.MainWindow.destroy()]).place(x=0, y=0)
   
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
        self.AlgorithmWindow.configure(bg='black')
        self.master.withdraw()
        #MainHeading and Input Label and Text
        MainHeadingLabel = tk.Label(self.AlgorithmWindow,text="Analyze Algorithms",bg='black', fg="red",font=('TimesNew Roman bold',28,'bold', 'underline')).pack(pady=20);
        NoteLabel = tk.Label(self.AlgorithmWindow, text="Note: ",bg='black', fg="red", font=('TimesNew Roman bold',15,'bold', 'underline'),anchor='w').pack(fill='both');
        NoteTextLabel = tk.Label(self.AlgorithmWindow, text="You can select number of nodes to be illustrated and select any algorithm from many options given below..", bg= 'Black', fg= 'White', font = ('TimesNew Roman bold',12),wraplengt=1000).place(x=75,y=95);
        #ComboBox1
        InputLabel = tk.Label(self.AlgorithmWindow, text="Select no of Nodes: ",bg='black', fg="red",font=('TimesNew Roman bold',12)).place(x=250,y=180)
        self.genreComboNodes = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(NoOfNodes))
        self.genreComboNodes.set("10")
        self.genreComboNodes.place(x=400,y=180)
        #ComboBox2
        Inputlabel1 = tk.Label(self.AlgorithmWindow, text="Select Algorithm: ",bg='black', fg="red",font=('TimesNew Roman bold',12)).place(x=570,y=180)
        self.genreComboAlgo = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(Algorithms))
        self.genreComboAlgo.set("Prims Algorithm")
        self.genreComboAlgo.place(x=700,y=180)
        #Buttons
        self.ViewResultButton = tk.Button(self.AlgorithmWindow, text="View Result", bd="8", font=('TimesNew Roman bold',12,'bold'),fg="red", command=lambda: [self.ViewAlgoGraph(0)]).place(x=450, y=250)
        self.ViewGraphButton = tk.Button(self.AlgorithmWindow, text="View Graph", bd="8", font=('TimesNew Roman bold',12,'bold'),fg="red", command=lambda: [self.ViewAlgoGraph(1)]).place(x=600, y=250)
        BackButton = tk.Button(self.AlgorithmWindow, text="BACK", bd="8", font=('TimesNew Roman bold',12,'bold'),fg="red", command=lambda: [self.master.deiconify(),self.master.state('zoomed'),self.AlgorithmWindow.destroy()]).place(x=0, y=0)

    def ViewAlgoGraph(self,Pos):
        print('Index: ' + str(Pos))
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
        
                    #--------------------------------------- ADDED THIS FROM NOW ---------------------------------------
            if(Pos==0):
                ws  = Tk()
                ws.title('PythonGuides')
                ws.geometry('500x500')
                ws['bg'] = '#AC99F2'

                game_frame = Frame(ws)
                game_frame.pack()
                #scrollbar
                game_scroll = Scrollbar(game_frame,orient='horizontal')
                game_scroll.pack(side= BOTTOM,fill=X)

                game_scroll = Scrollbar(game_frame)
                game_scroll.pack(side=RIGHT, fill=Y)



                my_game = ttk.Treeview(game_frame,xscrollcommand=game_scroll.set, yscrollcommand =game_scroll.set)


                my_game.pack()

                game_scroll.config(command=my_game.xview)
                game_scroll.config(command=my_game.yview)
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


        #--------------------------------------- --------------------------------------- ---------------------------------------
                # res = "SOURCE = {}\n\nNode\t|Cost\n".format(D.src)
                for i in range(G.V):
                    # res +=  format(i) + "\t|\t"  + format(D.dist[i],'.2f') + '\n'
                    # indexes = i
                    res = format(D.dist[i],'.2f')
                #     x.field_names = ["Nodes","Cost"]

                #     x.add_row([i,res])
                #     # x.add_row(["Brisbane",  1146.4])

                # t.insert(INSERT,x)#Inserting table in text widget
                # t.place(x=100,y=200)
                        #add data 
                
                    my_game.insert(parent='',index='end',iid=i-1,text='', values=([i, res]))
                my_game.pack()
                # my_game.place (x=200,y=200)


        if Algo == Algorithms[4]:
            BF = Ford(G, R.src)
            BF.BellmanFord()
            #--------------------------------------- ADDED THIS FROM NOW ---------------------------------------
            if(Pos==0):
                ws  = Tk()
                ws.title('PythonGuides')
                ws.geometry('500x500')
                ws['bg'] = '#AC99F2'

                game_frame = Frame(ws)
                game_frame.pack()
                #scrollbar
                game_scroll = Scrollbar(game_frame,orient='horizontal')
                game_scroll.pack(side= BOTTOM,fill=X)

                game_scroll = Scrollbar(game_frame)
                game_scroll.pack(side=RIGHT, fill=Y)



                my_game = ttk.Treeview(game_frame,xscrollcommand=game_scroll.set, yscrollcommand =game_scroll.set)


                my_game.pack()

                game_scroll.config(command=my_game.xview)
                game_scroll.config(command=my_game.yview)
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


        #--------------------------------------- --------------------------------------- ---------------------------------------
            # res = "SOURCE = {}".format(BF.src)
            # res += "\nNode\t|\tCost\n"
                for i in range(G.V):
                    res = format(BF.val[i],'.2f')
                    # res +=  format(i) + "\t|\t"  + format(BF.val[i],'.2f') + '\n'
                    my_game.insert(parent='',index='end',iid=i-1,text='', values=([i, res]))
                my_game.pack()

        if Algo == Algorithms[5]:
            F = Floyd(G)
            F.FloydWarshall()
                                            #--------------------------------------- ADDED THIS FROM NOW ---------------------------------------
            if(Pos==0):
                ws  = Tk()
                ws.title('PythonGuides')
                ws.geometry('500x500')
                ws['bg'] = '#AC99F2'

                game_frame = Frame(ws)
                game_frame.pack()
                #scrollbar
                game_scroll = Scrollbar(game_frame,orient='horizontal')
                game_scroll.pack(side= BOTTOM,fill=X)

                game_scroll = Scrollbar(game_frame)
                game_scroll.pack(side=RIGHT, fill=Y)



                my_game = ttk.Treeview(game_frame,xscrollcommand=game_scroll.set, yscrollcommand =game_scroll.set)


                my_game.pack()

                game_scroll.config(command=my_game.xview)
                game_scroll.config(command=my_game.yview)
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


        #--------------------------------------- --------------------------------------- ---------------------------------------
            # res = "         " 1=1=1=1=1=100
            # for i in range(G.V):
            #     res+= "{}       ".format(i)
            # res+="\n"
                for i in range(G.V):
                    # res+= "{0:.2f}  ".format(i)
                    for j in range(G.V):
                    
                        res = format(F.dist[i][j],'.2f')
                    
                    my_game.insert(parent='',index='end',iid=i-1,text='', values=([i, res]))
                my_game.pack()
                        # res+= "{0:.2f}  ".format(F.dist[i][j])
                    # res+="\n"

        if Algo == Algorithms[6]:
            L = Cluster(R.G)
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
             self.showMST(R,obj,index)
        elif(Pos==0):
            self.Nodes = self.genreComboNodes.get()
            self.Algo = self.genreComboAlgo.get()

            self.genreComboNodes.destroy()
            self.genreComboAlgo.destroy()
            
            self.genreComboNodes = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(NoOfNodes), state='disabled')
            self.genreComboNodes.set(self.Nodes)
            self.genreComboNodes.place(x=400,y=180)

            self.genreComboAlgo = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(Algorithms), state='disabled')
            self.genreComboAlgo.set(self.Algo)
            self.genreComboAlgo.place(x=700,y=180)

            self.resultLabel = tk.Label(
            self.AlgorithmWindow, text=res , font="San-Serif",borderwidth=2,relief="solid"
            )
            self.resultLabel.place(x = 500, y = 350)
            self.resetBtn = tk.Button(self.AlgorithmWindow, text="Select Next Algo",bd="8", font=('TimesNew Roman bold',12,'bold'),fg="red", command = self.resetStates).place(x=750,y=250)
            #New Window

        

    def resetStates(self):
        self.resultLabel.destroy()
        self.genreComboNodes.destroy()
        self.genreComboAlgo.destroy()
        self.genreComboNodes = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(NoOfNodes))
        self.genreComboNodes.set(self.Nodes)
        self.genreComboNodes.place(x=400,y=180)

        self.genreComboAlgo = ttk.Combobox(self.AlgorithmWindow, width=22, values=list(Algorithms))
        self.genreComboAlgo.set(self.Algo)
        self.genreComboAlgo.place(x=700,y=180)

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

root = tk.Tk()
root.iconify()
root.title('HomePage')
# root.geometry("600x400")
root.state('zoomed')
root.configure(bg='#396EB0')
app = Application(root)
root.mainloop()