import sys
class Graph:
    def __init__(self):
        self.nodes=[]
        self.graph=[]
        self.nodecount=0
    def addnode(self,v):
        if v in self.nodes:
            print(v,"is already present")
        else:
            self.nodes.append(v)
            self.nodecount+=1
            for x in self.graph:
                x.append(0)
            temp=[]
            for i in range(self.nodecount):
                temp.append(0)
            self.graph.append(temp)
            print(v,"is added")
    def printGraph(self):
        print("",end=" ")
        print(*self.nodes)
        for i in range(len(self.graph)):
            print(self.nodes[i],end=" ")
            for j in range(len(self.graph[i])):
                print(self.graph[i][j],end=" ")
            print()

if __name__ == '__main__':
    obj=Graph()
    while True:
        print("\n1. (Insertion) add a node")
        print("2. Print Graph")
        print("0. Exit\n")
        n=int(input("Enter any number:"))
        if n==1:
            v=input("Enter vertex:")
            obj.addnode(v)
        elif n==2:
            obj.printGraph()
        elif n==0:
            sys.exit(0)


    
