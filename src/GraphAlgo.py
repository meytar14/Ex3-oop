from GraphAlgoInterface import GraphAlgoInterface
from Graph import Graph
import json
import matplotlib as plt
import numpy as np


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: Graph):
        self.graph = graph

    def get_graph(self) -> Graph:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                for node in data["Nodes"]:
                    x, y, z = node["pos"].split(",")
                    p = (x, y, z)
                    self.graph.add_node(node["id"], p)
                for edge in data["Edges"]:
                    self.graph.add_edge(edge["src"], edge["dest"], edge["w"])
        except IOError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        nodes = []
        edges = []
        for node in self.graph.nodes.values():
            x, y, z = node.getLocation()
            p = str(x) + "," + str(y) + "," + str(z)
            nodes.append({"id": node.getKey(), "pos": p})
            for dest in node.out_edges:
                edges.append({"src": node.getKey(), "w": node.out_edges[dest], "dest": dest})
        data = {"Nodes": nodes, "Edges": edges}
        with open(file_name, "w") as file:
            json.dump(data, fp=file)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if not self.graph:
            return None
        if not self.graph.nodes.__contains__(id1):
            return None
        if not self.graph.nodes.__contains__(id2):
            return None

        src_node = self.graph.nodes.get(id1)
        stack = [src_node]
        prev = {}

        for node_key in self.graph.nodes:
            self.graph.nodes.get(node_key).tag = -1
        src_node.tag = 0
        while len(stack) > 0:
            node = stack.pop(0)
            for neighbor_key in node.getOutEdges():
                if self.graph.nodes[neighbor_key].getTag() == -1:
                    self.graph.nodes[neighbor_key].setTag(node.getTag() + node.out_edges[neighbor_key])
                    prev[neighbor_key] = node.getKey()
                    stack.append(self.graph.nodes[neighbor_key])
                    stack.sort(key=lambda x: x.weight, reverse=False)
                else:
                    if self.graph.nodes[neighbor_key].getTag() > node.getTag() + node.out_edges[neighbor_key]:
                        self.graph.nodes[neighbor_key].setTag(node.getTag() + node.out_edges[neighbor_key])
                        prev[neighbor_key] = node.getKey()
                        stack.append(self.graph.nodes[neighbor_key])
                        stack.sort(key=lambda x: x.weight, reverse=False)
        path = [id2]
        temp_key = id2
        while prev[temp_key] != id1:
            path.append(prev[temp_key])
            temp_key = prev[temp_key]
        path.append(id1)
        path.reverse()

    def connected_component(self, id1: int) -> list:
        visited = []
        nextToVisit = [self.graph.nodes[id1]]
        visited.append(id1)
        while len(nextToVisit) > 0:
            node = nextToVisit.pop(0)
            for ni in node.out_edges:
                if not visited.__contains__(ni):
                    visited.append(ni)
                    nextToVisit.append(self.graph.nodes[ni])
        visited_reverse = []
        nextToVisit.clear()
        visited_reverse.append(id1)
        reversed_g = self.graph.reversed_graph()
        nextToVisit.append(reversed_g.nodes[id1])
        while len(nextToVisit) > 0:
            node = nextToVisit.pop(0)
            for ni in node.out_edges:
                if not visited_reverse.__contains__(ni):
                    visited_reverse.append(ni)
                    nextToVisit.append(reversed_g.nodes[ni])
        id1_connected_component = []
        for node in visited:
            if visited_reverse.__contains__(node):
                id1_connected_component.append(node)
        return id1_connected_component

    def connected_components(self) -> list:  # list of lists
        nodes_that_left = []  # the keys of the nodes that doesn't belong to another connected_component
        connected_components = []  # list of all the connected_components in this graph
        for node in self.graph.nodes:
            nodes_that_left.append(node)
        while len(nodes_that_left) > 0:
            n = nodes_that_left[0]
            n_connected_component = sorted(self.connected_component(n))  # the connected_component of n
            connected_components.append(n_connected_component)
            for key in n_connected_component:
                nodes_that_left.remove(key)
        return connected_components

    def plot_graph(self) -> None:
        x_vals = []
        y_vals = []

        for node in self.graph.nodes:
            x_vals.append(node.getLocation()[0])
            y_vals.append((node.getLocation()[1]))
        x_vals.sort()
        y_vals.sort()
        plt.scatter(x_vals, y_vals)

        # plt.xticks(rotation=90, fontsize=10)
        # plt.yticks(np.arange(0, 21, 1))
        # plt.xlabel("country name", fontsize=20)
        # plt.ylabel("average points", fontsize=20)
        # plt.title("The average points of each country", fontsize=20)

        plt.show()
        pass
