import random


# class which represent each in the graph
class Node:
    def __init__(self, key: int, pos: tuple = (random.uniform(0.0, 10.0),
                                               random.uniform(0.0, 10.0), random.uniform(0.0, 10.0))):
        """
        init function for each node
        """
        self.key = key
        self.pos = pos
        self.tag = 0
        self.in_edges = {}
        self.out_edges = {}

    def getKey(self):
        return self.key

    def getLocation(self):
        return self.pos

    def setLocation(self, pos):
        self.pos = pos

    def getTag(self):
        return self.tag

    def setTag(self, tag):
        self.tag = tag

    def addNi(self, key: int, weight: float):
        """
        the function get a key and weight
        the function add an edge from this node to the node with the given key with the given weight
        """
        self.out_edges[key] = weight

    def addInNi(self, key, weight):
        """
        the function get a key and weight
        the function add an edge to this node from the node with the given key with the given weight
        """
        self.in_edges[key] = weight

    def getInEdges(self):
        return self.in_edges

    def getOutEdges(self):
        return self.out_edges

    def removeNi(self, key: int):
        if key in self.out_edges:
            self.out_edges.pop(key)

    def removeInNi(self, key: int):
        if key in self.in_edges:
            self.in_edges.pop(key)
