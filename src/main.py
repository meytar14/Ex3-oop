
from Graph import Graph
from GraphAlgo import GraphAlgo
if __name__ == '__main__':
   graph=Graph()
   # graph.add_node(1,(0.7,3,2))
   # graph.add_node(2,(2,2.5,2))
   # graph.add_node(3, (3, 3, 2))
   # graph.add_node(4, (4, 3, 2))
   #
   # graph.add_edge(1,2,4)
   # graph.add_edge(3,1,2.3)
   # graph.add_edge(1,3,2.3)
   # graph.add_edge(3,4,2.3)
   ga=GraphAlgo(graph)
   ga.load_from_json("A2")
   print(ga.connected_components())
