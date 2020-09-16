import unittest
import networkx as nx
from src.parser import read_graphs_from_folder


class TestParser(unittest.TestCase):

    def test_read_graphs(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2])
        G.add_edge(1, 2)

        self.folder = read_graphs_from_folder("C:/Users/zhaox/PycharmProjects/Data/graphs_for_my_testing")
        my_list = self.folder

        assert(nx.is_isomorphic(G, my_list[0]))


if __name__ == '__main__':
    unittest.main()
