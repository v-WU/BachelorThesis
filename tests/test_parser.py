import unittest
import networkx as nx
from src.parser import read_graphs_from_folder
from src.parser import create_abs_path


class TestParser(unittest.TestCase):

    # change the String in assert() to the correct path on YOUR device
    def test_create_abs_path(self):
        rel_path = "Data/graphs_for_my_testing"
        abs_path = create_abs_path(rel_path)

        assert(abs_path == "C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/graphs_for_my_testing")


    def test_read_graphs_from_folder(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2])
        G.add_edge(1, 2)

        # change the (absolute) path to the correct one on YOUR device
        my_list = read_graphs_from_folder("C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/graphs_for_my_testing")
        imported_graph = my_list[0][0]
        graph_name = my_list[0][1]
        graph_label = my_list[0][2]

        assert(nx.is_isomorphic(G, imported_graph))
        assert(graph_name == "simple_testing_graph")
        assert(graph_label == "graphs_for_my_testing")


if __name__ == '__main__':
    unittest.main()
