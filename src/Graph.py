from GraphInterface import GraphInterface
from Node import Node


class Graph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edge_size = 0
        self.MC = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edge_size

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].getInEdges()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].getOutEdges()

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        self.nodes[id1].addNi(id2, weight)
        self.nodes[id2].addInNi(id1, weight)
        self.MC += 1
        self.edge_size += 1

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.keys().__contains__(node_id):
            return False
        node = Node(node_id, pos)
        self.nodes[node_id] = node
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        for ni in self.all_out_edges_of_node(node_id).keys():
            self.nodes[ni].removeNi(node_id)
        self.nodes.pop(node_id)

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        self.nodes[node_id1].removeNi(node_id2)
        self.nodes[node_id2].removeInNi(node_id1)

    def reversed_graph(self):  # return a reversed graph of this graph
        g = Graph()
        for node in self.nodes.values():
            g.add_node(node.getKey(), node.getLocation())
        for node in self.nodes.values():
            for dest in node.in_edges:
                g.add_edge(node.getKey(), dest, node.in_edges[dest])
        return g


class ReversedGraph:
    def __init__(self):
        self.nodes = {}

    def init(self, graph: Graph):
        for node in graph.nodes.values():
            self.add_node(node.getKey(), node)
        for node in graph.nodes.values():
            for dest in node.in_edges:
                self.add_edge(node.getKey(), dest, node.in_edges[dest])

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        self.nodes[id1].addNi(id2, weight)
        self.nodes[id2].addInNi(id1, weight)
        self.MC += 1
        self.edge_size += 1

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.keys().__contains__(node_id):
            return False
        node = Node(node_id, pos)
        self.nodes[node_id] = node
        self.MC += 1
        return True

