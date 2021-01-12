from GraphInterface import GraphInterface
from Node import Node
import random


# class which represent each graph the we use
class DiGraph(GraphInterface):
    def __init__(self):
        """
        init function for Digraph
        """
        self.nodes = {}
        self.edge_size = 0
        self.MC = 0

    def v_size(self) -> int:
        """
        the function return the number of the nodes
        """
        return len(self.nodes)

    def e_size(self) -> int:
        """
        the function return the number of edges
        """
        return self.edge_size

    def get_all_v(self) -> dict:
        """
        the function return all the nodes
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        the function gets a node key and return all the edges to the node with the given key
        the function return Node if the node isn't in the graph
        """
        if id1 not in self.nodes:
            return None
        return self.nodes[id1].getInEdges()

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        the function gets a node key and return all the edges from the node with the given key
        the function return Node if the node isn't in the graph
        """
        if id1 not in self.nodes:
            return None
        return self.nodes[id1].getOutEdges()

    def get_mc(self) -> int:
        """
        return the number of changes made in this graph
        """
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        the function gets 2 keys and weight and create an edge from the first onr to the second
        the function return false if not both nodes are in the graph or the edge already exists
        else she return true
        """
        if id1 not in self.nodes or id2 not in self.nodes:
            return False
        if id2 in self.nodes[id1].out_edges:
            return False
        self.nodes[id1].addNi(id2, weight)
        self.nodes[id2].addInNi(id1, weight)
        self.MC += 1
        self.edge_size += 1
        return True

    def add_node(self, node_id: int, pos: tuple = (random.uniform(0.0, 10.0), random.uniform(0.0, 10.0), random.uniform(0.0, 10.0))) -> bool:
        """
        the function gets key and position
        she create new node with the given data and insert him the the graph
        the function return false if there is already an existing node if this key. else true
        """
        if node_id in self.nodes:
            return False
        node = Node(node_id, pos)
        self.nodes[node_id] = node
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        the function gets a key and remove the node with the given key from the graph
        the function return false if there is no node with this key. else true
        """
        if node_id not in self.nodes:
            return False
        removed_keys = []
        for ni_key in self.all_out_edges_of_node(node_id).keys():
            removed_keys.append(ni_key)
        for key in removed_keys:
            self.remove_edge(node_id, key)
        removed_keys.clear()
        for ni_key in self.all_in_edges_of_node(node_id):
            removed_keys.append(ni_key)
        for key in removed_keys:
            self.remove_edge(key, node_id)
        self.nodes.pop(node_id)
        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        the function gets 2 keys and remove the edge from the first node to the second
        the function return false if there if not both nodes are in the graph or there is no edge between the 2
        else she return true
        """
        if node_id1 not in self.nodes or node_id2 not in self.nodes:
            return False
        node1 = self.nodes[node_id1]
        if node_id2 not in node1.out_edges:
            return False
        self.nodes[node_id1].removeNi(node_id2)
        self.nodes[node_id2].removeInNi(node_id1)
        self.MC += 1
        self.edge_size -= 1
        return True

    def reversed_graph(self):  # return a reversed graph of this graph
        """
        the function return a reversed graph from self.graph
        """
        g = DiGraph()
        for node in self.nodes.values():
            g.add_node(node.getKey(), node.getLocation())
        for node in self.nodes.values():
            for dest in node.in_edges:
                g.add_edge(node.getKey(), dest, node.in_edges[dest])
        return g


# class which represent the reversed graph
# class ReversedGraph:
#     def __init__(self):
#         """
#         first set function for a reversed graph
#         """
#         self.nodes = {}
#         self.edge_size = 0
#         self.MC = 0
#
#     def init(self, graph: DiGraph):
#         """
#         the function gets a DiGraph and fill the data in our reversed graph
#         """
#         for node in graph.nodes.values():
#             self.add_node(node.getKey(), node)
#         for node in graph.nodes.values():
#             for dest in node.in_edges:
#                 self.add_edge(node.getKey(), dest, node.in_edges[dest])
#
#     def add_edge(self, id1: int, id2: int, weight: float) -> bool:
#         """
#         the function gets 2 keys and weight and create an edge from the first onr to the second
#         the function return false if not both nodes are in the graph or the edge already exists
#         else she return true
#         """
#         if id1 not in self.nodes or id2 not in self.nodes:
#             return False
#         if id2 in self.nodes[id1].out_edges:
#             return False
#         self.nodes[id1].addNi(id2, weight)
#         self.nodes[id2].addInNi(id1, weight)
#         self.MC += 1
#         self.edge_size += 1
#         return True
#
#     def add_node(self, node_id: int, pos: tuple = (random.uniform(0.0, 10.0), random.uniform(0.0, 10.0), random.uniform(0.0, 10.0))) -> bool:
#         """
#         the function gets key and position
#         she create new node with the given data and insert him the the graph
#         the function return false if there is already an existing node if this key. else true
#         """
#         if self.nodes.keys().__contains__(node_id):
#             return False
#         node = Node(node_id, pos)
#         self.nodes[node_id] = node
#         self.MC += 1
#         return True
