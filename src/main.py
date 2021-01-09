# This is a sample Python script.
from Graph import Graph
from GraphAlgo import GraphAlgo
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
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
