class Node:
    def __init__(self,key:int,pos=(0,0,0)):
        self.key=key
        self.pos=pos
        self.tag=0
        self.in_edges={}
        self.out_edges={}

    def getKey(self):
        return self.key

    def getLocation(self):
        return self.pos

    def setLocation(self,pos):
        self.pos=pos

    def getTag(self):
        return self.tag

    def setTag(self,tag):
        self.tag=tag

    def addNi(self,key:int, weight:float):
        self.out_edges[key]=weight

    def addInNi(self,key,weight):
        self.in_edges[key]=weight

    def getInEdges(self):
        return self.in_edges

    def getOutEdges(self):
        return self.out_edges


    def removeNi(self,key:int):
        self.out_edges.pop(key)

    def removeInNi(self,key:int):
        self.in_edges.pop(key)






