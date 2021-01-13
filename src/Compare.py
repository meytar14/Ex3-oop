from GraphAlgo import GraphAlgo
from time import time
from os import listdir
import networkx as nx
import networkx.algorithms.components as a

# ga = GraphAlgo()
# path = "C:\matan\year 2\semester 3\OOP\Assignments\Ex3\data\\"
# file_name = "G_30000_240000_1.json"
# ga.load_from_json(path + file_name)
# start_time = time()
# ga.connected_components()
# end_time = time()
# print(file_name, "running time is:", end_time - start_time)


path = "C:\matan\year 2\semester 3\OOP\Assignments\Ex3\data\\"
file_names = ["G_10_80_1.json", "G_100_800_1.json", "G_1000_8000_1.json", "G_10000_80000_1.json", "G_20000_160000_1.json", "G_30000_240000_1.json"]

ga = GraphAlgo()
ga.load_from_json(path + file_names[0])
graph = nx.DiGraph()
for i in ga.graph.nodes:
    graph.add_node(i)
for i in ga.graph.nodes:
    for j in ga.graph.nodes[i].out_edges:
        graph.add_edge(i, j, weight=ga.graph.nodes[i].out_edges[j])
try:
    start_time = time()
    # nx.dijkstra_path(graph, 3, 8)
    t = a.strongly_connected.strongly_connected_components(graph)
    end_time = time()
    print(file_names[0], "running time is:", end_time - start_time)
except nx.NetworkXNoPath as e:
    print("no path", e)

# --------------------------------------------------------------------------------------------

ga = GraphAlgo()
ga.load_from_json(path + file_names[1])
graph = nx.DiGraph()
for i in ga.graph.nodes:
    graph.add_node(i)
for i in ga.graph.nodes:
    for j in ga.graph.nodes[i].out_edges:
        graph.add_edge(i, j, weight=ga.graph.nodes[i].out_edges[j])

try:
    start_time = time()
    # nx.dijkstra_path(graph, 3, 8)
    t = a.strongly_connected.strongly_connected_components(graph)
    end_time = time()
    print(file_names[1], "running time is:", end_time - start_time)
except nx.NetworkXNoPath as e:
    print("no path", e)

# --------------------------------------------------------------------------------
ga = GraphAlgo()
ga.load_from_json(path + file_names[2])
graph = nx.DiGraph()
for i in ga.graph.nodes:
    graph.add_node(i)
for i in ga.graph.nodes:
    for j in ga.graph.nodes[i].out_edges:
        graph.add_edge(i, j, weight=ga.graph.nodes[i].out_edges[j])

try:
    start_time = time()
    # nx.dijkstra_path(graph, 3, 8)
    t = a.strongly_connected.strongly_connected_components(graph)
    end_time = time()
    print(file_names[2], "running time is:", end_time - start_time)
except nx.NetworkXNoPath as e:
    print("no path", e)

# --------------------------------------------------------------------------------

ga = GraphAlgo()
ga.load_from_json(path + file_names[3])
graph = nx.DiGraph()
for i in ga.graph.nodes:
    graph.add_node(i)
for i in ga.graph.nodes:
    for j in ga.graph.nodes[i].out_edges:
        graph.add_edge(i, j, weight=ga.graph.nodes[i].out_edges[j])

try:
    start_time = time()
    # nx.dijkstra_path(graph, 3, 8)
    t = a.strongly_connected.strongly_connected_components(graph)
    end_time = time()
    print(file_names[3], "running time is:", end_time - start_time)
except nx.NetworkXNoPath as e:
    print("no path", e)

# --------------------------------------------------------------------------------

ga = GraphAlgo()
ga.load_from_json(path + file_names[4])
graph = nx.DiGraph()
for i in ga.graph.nodes:
    graph.add_node(i)
for i in ga.graph.nodes:
    for j in ga.graph.nodes[i].out_edges:
        graph.add_edge(i, j, weight=ga.graph.nodes[i].out_edges[j])

try:
    start_time = time()
    # nx.dijkstra_path(graph, 3, 8)
    t = a.strongly_connected.strongly_connected_components(graph)
    end_time = time()
    print(file_names[4], "running time is:", end_time - start_time)
except nx.NetworkXNoPath as e:
    print("no path", e)

# --------------------------------------------------------------------------------

ga = GraphAlgo()
ga.load_from_json(path + file_names[5])
graph = nx.DiGraph()
for i in ga.graph.nodes:
    graph.add_node(i)
for i in ga.graph.nodes:
    for j in ga.graph.nodes[i].out_edges:
        graph.add_edge(i, j, weight=ga.graph.nodes[i].out_edges[j])

try:
    start_time = time()
    # nx.dijkstra_path(graph, 3, 8)
    t = a.strongly_connected.strongly_connected_components(graph)
    end_time = time()
    print(file_names[5], "running time is:", end_time - start_time)
except nx.NetworkXNoPath as e:
    print("no path", e)