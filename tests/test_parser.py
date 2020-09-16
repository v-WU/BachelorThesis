import unittest
import networkx as nx
from src.parser import read_graphs_from_folder


class TestParser(unittest.TestCase):

    def test_read_graphs_from_folder(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2])
        G.add_edge(1, 2)

        my_list = read_graphs_from_folder("C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/graphs_for_my_testing")
        imported_graph = my_list[0][0]
        graph_name = my_list[0][1]
        graph_label = my_list[0][2]

        assert(nx.is_isomorphic(G, imported_graph))
        assert(graph_name == "simple_testing_graph")
        assert(graph_label == "graphs_for_my_testing")


if __name__ == '__main__':
    unittest.main()
