from GraphAlgoInterface import GraphAlgoInterface
from Graph import Graph
import json
import matplotlib.pyplot as plt
# import numpy as np


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
                    p = (float(x), float(y), float(z))
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
        for node in self.graph.nodes.values():
            x_vals.append(node.getLocation()[0])
            y_vals.append((node.getLocation()[1]))
            for out_edge_key in node.out_edges:
                delta_x = self.graph.nodes[out_edge_key].getLocation()[0]-node.getLocation()[0]
                if(delta_x>0):
                    delta_x=delta_x-0.085
                if (delta_x < 0):
                    delta_x = delta_x+0.085
                delta_y = self.graph.nodes[out_edge_key].getLocation()[1]-node.getLocation()[1]
                if (delta_y > 0):
                    delta_y = delta_y - 0.085
                if(delta_y < 0):
                    delta_y = delta_y + 0.085
                plt.arrow(node.getLocation()[0], node.getLocation()[1], delta_x, delta_y,
                          head_length=0.1, head_width=0.1)
        plt.scatter(x_vals, y_vals)
        plt.show()


# def graph1test() -> None:
#     x_val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     y_val = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#     fig, ax = plt.subplots()
#
#     plt.annotate(xy=(5, 5), xytext=(1, 1), text="text", arrowprops=dict(facecolor='black', shrink=1))
#     ax.scatter(x_val, y_val)
#     # ax.annotate(33, (5, 5))
#     plt.plot(x_val, y_val)
#
#     # plt.grid()
#     # plt.legend()
#     plt.show()
#
# def graph2test() -> None:
#     x_val = [0, 1, 2, 7, 4, 5, 6, 3, 8, 9]
#     y_val = [0, 1, 4, 49, 16, 25, 36, 9, 64, 81]
#     fig, ax = plt.subplots()
#
#     # plt.annotate(xy=(5, 5), xytext=(1, 1), text="text", arrowprops=dict(facecolor='black', shrink=1))
#     ax.scatter(x_val, y_val)
#     # ax.annotate(33, (5, 5))
#     plt.plot(x_val, y_val)
#     ax.scatter(5.5, 15, color='yellow')
#     ax.scatter(5, 10, color='yellow')
#
#     # plt.grid()
#     # plt.legend()
#     plt.show()
#
#
# def graph3test() -> None:
#     x_val = [1, 5]
#     y_val = [1, 5]
#     fig, ax = plt.subplots()
#     # plt.plot(x_val, y_val, color="red")
#     plt.scatter(x_val, y_val, color="red")
#     x_val = [5, 3]
#     y_val = [1, 3]
#     # plt.plot(x_val, y_val, color="yellow")
#     plt.scatter(x_val, y_val, color="yellow")
#     plt.arrow(1, 1, 3, 3, head_length=0.1, head_width=0.1)
#     plt.arrow(3, 5, -2, -2, head_length=0.1, head_width=0.1)
#
#     plt.show()


# if __name__ == '__main__':
    # graph1test()
    # graph2test()
    # graph3test()
    # print("hey")
