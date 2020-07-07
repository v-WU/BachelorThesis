import unittest
import networkx as nx
from src.parser import read_graphs


class TestParser(unittest.TestCase):

    def test_read_graphs(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2])
        G.add_edge(1, 2)

        my_list = read_graphs("C:/Users/zhaox/PycharmProjects/Data/graphs_for_my_testing")

        assert(nx.is_isomorphic(G, my_list[0]))


if __name__ == '__main__':
    unittest.main()
