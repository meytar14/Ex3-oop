from unittest import TestCase
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from src.Node import Node


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        graph = DiGraph()
        graph.add_node(1, (1, 1, 2))
        graph.add_node(3, (3, 1, 2))
        graph.add_node(4, (4, 2, 2))
        graph.add_edge(3, 1, 2.3)
        graph.add_edge(1, 3, 2.3)
        graph.add_edge(3, 4, 2.3)
        ga = GraphAlgo(graph)
        self.assertEqual(graph, ga.get_graph())

    def test_load_from_json(self):
        graph = DiGraph()
        ga = GraphAlgo(graph)
        ga.load_from_json("load_test")

        g2=DiGraph()
        g2.add_node(0,(0,0,0))
        g2.add_node(1, (1, 1, 1))
        g2.add_node(2, (2, 2, 2))
        g2.add_node(3, (3, 3, 3))
        g2.add_edge(0,2,1.2)
        g2.add_edge(0,1,1)
        g2.add_edge(2, 3, 3)


        for node in g2.nodes.values():
            self.assertEqual(ga.graph.nodes[node.key].in_edges, node.in_edges)
            self.assertEqual(ga.graph.nodes[node.key].out_edges, node.out_edges)
        for node in ga.graph.nodes.values():
            self.assertEqual(g2.nodes[node.key].in_edges, node.in_edges)
            self.assertEqual(g2.nodes[node.key].out_edges, node.out_edges)





    def test_save_to_json(self):
        g2 = DiGraph()
        g2.add_node(0, (0, 0, 0))
        g2.add_node(1, (1, 1, 1))
        g2.add_node(2, (2, 2, 2))
        g2.add_node(3, (3, 3, 3))
        g2.add_edge(0, 2, 1.2)
        g2.add_edge(0, 1, 1)
        g2.add_edge(2, 3, 3)
        ga = GraphAlgo(g2)
        ga.save_to_json("save_test")
        g3=DiGraph()
        ga2=GraphAlgo(g3)
        ga2.load_from_json("save_test")

        for node in ga2.graph.nodes.values():
            self.assertEqual(ga.graph.nodes[node.key].in_edges, node.in_edges)
            self.assertEqual(ga.graph.nodes[node.key].out_edges, node.out_edges)
        for node in ga.graph.nodes.values():
            self.assertEqual(ga2.graph.nodes[node.key].in_edges, node.in_edges)
            self.assertEqual(ga2.graph.nodes[node.key].out_edges, node.out_edges)






    def test_shortest_path(self):
        graph = DiGraph()
        graph.add_node(1, (1, 1, 2))
        graph.add_node(2, (3, 1, 2))
        graph.add_node(3, (4, 2, 2))
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 1)
        graph.add_edge(1, 3, 3)
        ga = GraphAlgo(graph)
        res_list = [1, 2, 3]
        self.assertEqual((2, res_list), ga.shortest_path(1, 3))

    def test_connected_component(self):
        graph = DiGraph()
        graph.add_node(1, (1, 1, 2))
        graph.add_node(2, (2, 2, 2))
        graph.add_node(3, (3, 1, 2))
        graph.add_node(4, (4, 2, 2))
        graph.add_edge(1, 2, 4)
        graph.add_edge(3, 1, 2.3)
        graph.add_edge(1, 3, 2.3)
        graph.add_edge(3, 4, 2.3)
        ga = GraphAlgo(graph)
        self.assertIsNone(ga.connected_component(5))
        res = [3, 1]
        self.assertEqual(res, ga.connected_component(3))
        res = [2]
        self.assertEqual(res, ga.connected_component(2))
        res = [4]
        self.assertEqual(res, ga.connected_component(4))
        graph.add_node(7, (1, 1, 1))
        res = [7]
        self.assertEqual(res, ga.connected_component(7))

    def test_connected_components(self):
        graph = DiGraph()
        graph.add_node(1, (1, 1, 2))
        graph.add_node(2, (2, 2, 2))
        graph.add_node(3, (3, 1, 2))
        graph.add_node(4, (4, 2, 2))
        graph.add_edge(1, 2, 4)
        graph.add_edge(3, 1, 2.3)
        graph.add_edge(1, 3, 2.3)
        graph.add_edge(3, 4, 2.3)
        ga = GraphAlgo(graph)
        res = [[2], [4], [1, 3]]
        self.assertEqual(res.sort(), ga.connected_components().sort())

    def test_graph_range(self):
        graph = DiGraph()
        ga = GraphAlgo(graph)
        self.assertIsNone(ga.graph_range())
        graph.add_node(1, (1, 1, 2))
        graph.add_node(2, (2, 2, 2))
        graph.add_node(3, (3, 1, 2))
        graph.add_node(4, (4, 2, 2))
        x_range_min = 1
        x_range_max = 4
        y_range_min = 1
        y_range_max = 2
        self.assertEqual(x_range_min, ga.graph_range().x_range.min)
        self.assertEqual(x_range_max, ga.graph_range().x_range.max)
        self.assertEqual(y_range_min, ga.graph_range().y_range.min)
        self.assertEqual(y_range_max, ga.graph_range().y_range.max)
