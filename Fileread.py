import re
import matplotlib.pyplot as plt


class FileHandling:
    filename = 'benchmark/';
    Total_nodes = 0;
    Index = [];
    X_points = [];
    Y_points = [];
     
    def __init__(self, filename):
        self.filename = self.filename + filename; 
        # print(filename);
        # print(self.filename);
     
    def Read(self):
        with open(self.filename, 'r') as f:
            f.readline();
            f.readline();
            self.Total_nodes = f.readline();
            f.readline();
            print('Total Nodes: ',self.Total_nodes)
            for i in range(int(self.Total_nodes)):
                lines = f.readline()
                # print(lines)
                split_string = lines.split();
                # print(split_string)
                self.Index.append(split_string[0]);
                self. X_points.append(split_string[1]);
                self.Y_points.append(split_string[2]);
         
    def DisplayPoints(self):
        print(self.Index, self.X_points,self.Y_points);

    def DisplayGraph(self):
        plt.plot(self.X_points,self.Y_points);
        plt.show();

if __name__ == '__main__':
    F = FileHandling('input10.txt')
    F.Read();
    F.DisplayPoints();
    F.DisplayGraph();