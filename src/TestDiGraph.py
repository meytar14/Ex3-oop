from unittest import TestCase
from DiGraph import DiGraph
from Node import Node


class TestDiGraph(TestCase):
    def test_v_size(self):
        # init and set graph
        graph = DiGraph()
        self.assertEqual(0, graph.v_size())
        graph.add_node(1, (1, 1, 2))
        graph.add_node(2, (2, 2, 2))
        self.assertEqual(2, graph.v_size())
        graph.remove_node(1)
        self.assertEqual(1, graph.v_size())
        graph.remove_node(2)
        self.assertEqual(0, graph.v_size())

    def test_e_size(self):
        graph = DiGraph()
        graph.add_node(1, (1, 1, 2))
        graph.add_node(2, (2, 2, 2))
        graph.add_node(3, (3, 1, 2))
        graph.add_node(4, (4, 2, 2))
        self.assertEqual(0, graph.e_size())
        graph.add_edge(1, 2, 4)
        graph.add_edge(3, 1, 2.3)
        self.assertEqual(2, graph.e_size())
        graph.remove_edge(1, 2)
        self.assertEqual(1, graph.e_size())
        graph.remove_edge(3, 1)
        self.assertEqual(0, graph.e_size())

    def test_get_all_v(self):
        graph = DiGraph()
        node1 = Node(1, (1, 1, 2))
        node2 = Node(2, (2, 2, 2))
        node3 = Node(3, (3, 1, 2))
        node4 = Node(4, (4, 2, 2))
        graph.add_node(node1.getKey(), node1.getLocation())
        graph.add_node(node2.getKey(), node2.getLocation())
        graph.add_node(node3.getKey(), node3.getLocation())
        graph.add_node(node4.getKey(), node4.getLocation())

        res = {}
        res[node1.key] = node1
        res[node2.key] = node2
        res[node3.key] = node3
        res[node4.key] = node4

        for key in graph.get_all_v():
            node = graph.get_all_v()[key]
            self.assertEqual(res[key].getKey(), node.getKey())
            self.assertEqual(res[key].getTag(), node.getTag())
            self.assertEqual(res[key].getLocation(), node.getLocation())
            self.assertEqual(res[key].getInEdges(), node.getInEdges())
            self.assertEqual(res[key].getOutEdges(), node.getOutEdges())

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        node1 = Node(1, (1, 1, 2))
        node2 = Node(2, (2, 2, 2))
        node3 = Node(3, (3, 1, 2))
        node4 = Node(4, (4, 2, 2))
        graph.add_node(node1.getKey(), node1.getLocation())
        graph.add_node(node2.getKey(), node2.getLocation())
        graph.add_node(node3.getKey(), node3.getLocation())
        graph.add_node(node4.getKey(), node4.getLocation())
        graph.add_edge(1, 2, 4)
        graph.add_edge(3, 1, 2.3)
        graph.add_edge(1, 3, 2.3)
        graph.add_edge(3, 4, 2.3)

        res = {}
        res[1] = 4
        self.assertEqual(res, graph.all_in_edges_of_node(2))
        res.pop(1)
        res[3] = 2.3
        self.assertEqual(res, graph.all_in_edges_of_node(1))

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        node1 = Node(1, (1, 1, 2))
        node2 = Node(2, (2, 2, 2))
        node3 = Node(3, (3, 1, 2))
        node4 = Node(4, (4, 2, 2))
        graph.add_node(node1.getKey(), node1.getLocation())
        graph.add_node(node2.getKey(), node2.getLocation())
        graph.add_node(node3.getKey(), node3.getLocation())
        graph.add_node(node4.getKey(), node4.getLocation())
        graph.add_edge(1, 2, 4)
        graph.add_edge(3, 1, 2.3)
        graph.add_edge(1, 3, 2.3)
        graph.add_edge(3, 4, 2.3)

        res = {}
        res[2] = 4
        res[3] = 2.3
        self.assertEqual(res, graph.all_out_edges_of_node(1))
        res.pop(2)
        res.pop(3)
        res[1] = 2.3
        res[4] = 2.3
        self.assertEqual(res, graph.all_out_edges_of_node(3))

    def test_get_mc(self):
        graph = DiGraph()
        self.assertEqual(0, graph.get_mc())
        graph.add_node(1, (1, 1, 2))
        graph.add_node(2, (2, 2, 2))
        graph.add_node(3, (3, 1, 2))
        graph.add_node(4, (4, 2, 2))
        self.assertEqual(4, graph.get_mc())
        graph.add_edge(1, 2, 4)
        graph.add_edge(3, 1, 2.3)
        graph.add_edge(1, 3, 2.3)
        graph.add_edge(3, 4, 2.3)
        self.assertEqual(8, graph.get_mc())
        graph.remove_edge(1, 2)
        self.assertEqual(9, graph.get_mc())

        graph.remove_node(3)
        self.assertEqual(13, graph.get_mc())

    def test_add_edge(self):
        graph = DiGraph()
        graph.add_node(1, (1, 1, 2))
        graph.add_node(2, (2, 2, 2))
        graph.add_node(3, (3, 1, 2))
        graph.add_node(4, (4, 2, 2))
        graph.add_edge(1, 2, 4)
        self.assertFalse(graph.add_edge(1, 2, 4))
        graph.add_edge(3, 1, 2.3)
        graph.add_edge(1, 3, 2.3)
        self.assertFalse(graph.add_edge(-1, 2, 1))

    def test_add_node(self):
        graph = DiGraph()
        graph.add_node(1, (1, 1, 2))
        self.assertFalse(graph.add_node(1, (1, 1, 2)))
        graph.add_node(3, (1, 1, 2))
        self.assertFalse(graph.add_node(3, (0, 2, 3)))

    def test_remove_node(self):
        graph = DiGraph()
        graph.add_node(1, (1, 1, 2))
        graph.add_node(3, (1, 1, 2))
        self.assertTrue(graph.remove_node(1))
        self.assertFalse(graph.remove_node(1))
        self.assertTrue(graph.remove_node(3))

    def test_remove_edge(self):
        graph = DiGraph()
        graph.add_node(1, (1, 1, 2))
        graph.add_node(2, (2, 2, 2))
        graph.add_node(3, (3, 1, 2))
        graph.add_node(4, (4, 2, 2))
        graph.add_edge(1, 2, 4)
        graph.add_edge(3, 1, 2.3)
        graph.add_edge(1, 3, 2.3)
        graph.add_edge(3, 4, 2.3)
        self.assertFalse(graph.remove_edge(0, 3))
        self.assertFalse(graph.remove_edge(3, -1))
        self.assertFalse(graph.remove_edge(1, 4))
        self.assertTrue(graph.remove_edge(1, 3))
        self.assertFalse(graph.remove_edge(1, 3))

    def test_reversed_graph(self):
        self.fail()  # TODO write this test
