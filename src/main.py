
from Graph import Graph
import matplotlib.pyplot as plt
from GraphAlgo import GraphAlgo
#fggggg
if __name__ == '__main__':
   graph=Graph()
   graph.add_node(1,(1,1,2))
   graph.add_node(2,(2,2,2))
   graph.add_node(3, (3, 1, 2))
   graph.add_node(4, (4, 2, 2))

   graph.add_edge(1,2,4)
   graph.add_edge(3,1,2.3)
   graph.add_edge(1,3,2.3)
   graph.add_edge(3,4,2.3)
   ga=GraphAlgo(graph)
   ga.plot_graph()

