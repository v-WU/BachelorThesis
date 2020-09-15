import unittest
import networkx as nx

from matchingGraphWrapper import MatchingGraph


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_init(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2])
        G.add_edge(1, 2)

        Graph = MatchingGraph(G, true, true)


if __name__ == '__main__':
    unittest.main()
