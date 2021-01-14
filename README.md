# ex3-oop

## On the project 
In this project we are compering the running time of some algorithms on several graphs.
We are compering the graphs in: java project algorithms Ex2 (we took from the previous project which we did), python algorithms (which we write) and networkx algorithms.
The compered algorithms between the graphs are: shortest path, connected component of a node and connected components .
The graph are given and they are in the folder 'data' in the project.

## The algorithms which we compare by:
Shortest path - this algorithm finds the shortest path from the first given node to the other one. In addition this function returns the weight of the path.
Connected component of a node - this algorithm gets a node and return all the nodes in the graph which are connected component with this node.
Connected components - this algorithm returns a list of lists and everyone of those lists are a connected component in the graph.

## Java algorithms
In the java part of this project we used the java algorithms which  we wrote in the last project.
We added the Connected component of a node and the Connected components algorithms to the project so we can use them.

## python algorithms
For the python algorithms we wrote some classes to represent the graph and the algorithms that we do on it.
Main classes:
Node - class which we use to represent each node in the graph and his feature.
DiGraph - class which we use to represent directed weighted graph. The graph contain a list of nodes which are from the Node class
GraphAlgo - class which we use to represent the algorithms on our graphs.

## networkx algorithms
NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
By Default Networks doesn't have a Connected components algorithms so we needed to import it  
