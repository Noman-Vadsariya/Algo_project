import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

Algorithms = ["Prims Algorithm","Kruskal Algorithm","Dijkstra Algorithm","Bellman Ford Algorithm",
              "Floyd Warshall","Clustering Coefficient Algorithm",
              "Borůvka's Algorithm"];
Files = ["Input10.txt","Input20.txt","Input30.txt","Input40.txt","Input50.txt","Input60.txt",
         "Input70.txt","Input80.txt","Input90.txt","Input100.txt"];
NoOfNodes = [10,20,30,40,50,60,70,80,90,100];

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.root = tk.Tk()
        self.title('ALGORITHMS & VISUALIZATION')
        self.create_IntroWidgets()

    def Graph(x,y):
        x = [0,1,2,3,4,5,6,7,8,9]
        y = [0,10,20,30,40,50,60,70,80,90]
        
        plt.plot(x,y)
        plt.show()
        
    def create_IntroWidgets(self):
        # root = tk.Tk()
        headingLabel = tk.Label(self, text="Graph Visualization", font="Roboto 12")
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        ttk.Separator(self, orient="horizontal").grid(row=1, column=0, columnspan=5, sticky='ew')

        # day = tk.Frame(self)
        # tk.Label(day, text="_______").pack()

        # tk.Label(day, text="TODAY", font='Helvetica 10 underline').pack()
        # tk.Label(day, text="").pack()
        # day.grid(row=2, column=0, padx=10)

        # tk.Label(self, text="Algorithms: ").grid(row=2, column=1, padx=(10,0))
        # self.genreCombo = ttk.Combobox(self, width=28, values=list(Algorithms), state="readonly")
        # self.genreCombo.set("Select Algorithm")
        # # self.genreCombo.bind('<<ComboboxSelected>>', self.updateMovies)
        # self.genreCombo.grid(row=2, column=2)


        tk.Label(self, text="Select no of Nodes: ").grid(row=2, column=3, padx=(10,0))
        self.genreCombo = ttk.Combobox(self, width=18, values=list(NoOfNodes), state="readonly")
        self.genreCombo.set("No of Nodes");
        # self.genreCombo.bind('<<ComboboxSelected>>', self.showsimplegraph)
        self.genreCombo.grid(row=2, column=4, padx=(0, 10))
        ttk.Separator(self, orient="horizontal").grid(row=3, column=0, columnspan=5, sticky='ew')
        B = tk.Button(self, text ="View Graph", bd = '5',command = Application.Graph)
        B1 = tk.Button(self, text ="Illustrate Algorithms", bd = '5', command = lambda:[self.createWidgets()])
        B2 = tk.Button(self, text ="Exit", bd = '5', command = self.destroy)
        B.grid(row=4, column=0)
        B1.grid(row=4,column=1)
        B2.grid(row=4, column=2)


    def createWidgets(self):
        newwindow = tk.Toplevel()
        # self.root.destroy();
        # self.protocol('newwindow', self.quit)
        # self.destroy()
        # self.destroy()
        headingLabel = tk.Label(newwindow, text="ALGORITHMS & VISUALIZATION", font="Roboto 12")
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        ttk.Separator(newwindow, orient="horizontal").grid(row=1, column=0, columnspan=5, sticky='ew')

        # day = tk.Frame(self)
        # tk.Label(day, text="_______").pack()

        # tk.Label(day, text="TODAY", font='Helvetica 10 underline').pack()
        # tk.Label(day, text="").pack()
        # day.grid(row=2, column=0, padx=10)

        tk.Label(newwindow, text="Algorithms: ").grid(row=2, column=1, padx=(10,0))
        self.genreCombo = ttk.Combobox(newwindow, width=28, values=list(Algorithms), state="readonly")
        self.genreCombo.set("Select Algorithm")
        # self.genreCombo.bind('<<ComboboxSelected>>', self.Algorithm)
        self.genreCombo.grid(row=2, column=2)
        # Algorithm():
            # x,y
            # self.Graph(x,y)

        tk.Label(newwindow, text="Select no of Nodes: ").grid(row=2, column=3, padx=(10,0))
        self.genreCombo = ttk.Combobox(newwindow, width=18, values=list(NoOfNodes), state="readonly")
        self.genreCombo.set("No of Nodes");
        # self.genreCombo.bind('<<ComboboxSelected>>', self.updateMovies)
        self.genreCombo.grid(row=2, column=4, padx=(0, 10))
        ttk.Separator(newwindow, orient="horizontal").grid(row=3, column=0, columnspan=5, sticky='ew')

app = Application()
app.mainloop()
