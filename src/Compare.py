from GraphAlgo import GraphAlgo
from time import time
from os import listdir
import networkx as nx
import networkx.algorithms.components as a

ga = GraphAlgo()
path = ".\data\\"
file_names = ["G_10_80_1.json", "G_100_800_1.json", "G_1000_8000_1.json", "G_10000_80000_1.json", "G_20000_160000_1.json", "G_30000_240000_1.json"]

# ga.load_from_json(path + file_names[0])
# start_time = time()
# ga.connected_components()
# end_time = time()
# print(file_names[0], "running time is:", end_time - start_time)


# graph = nx.DiGraph()
# for i in ga.graph.nodes:
#     graph.add_node(i)
# for i in ga.graph.nodes:
#     for j in ga.graph.nodes[i].out_edges:
#         graph.add_edge(i, j, weight=ga.graph.nodes[i].out_edges[j])
# try:
#     start_time = time()
#     # nx.dijkstra_path(graph, 3, 8)
#     t = a.strongly_connected.strongly_connected_components(graph)
#     end_time = time()
#     print(file_names[0], "running time is:", end_time - start_time)
# except nx.NetworkXNoPath as e:
#     print("no path", e)
