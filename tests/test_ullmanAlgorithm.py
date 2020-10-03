import unittest
import networkx as nx
from ullmanAlgorithm import create_adj_matrix
from ullmanAlgorithm import create_vector


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_create_adj_matrix(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2])
        G.add_edge(1, 2)

        A = create_adj_matrix(G)
        assert (A[0][0] == 0)
        assert (A[0][1] == 1)
        assert (A[1][0] == 1)
        assert (A[1][1] == 0)

    def test_create_vector(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2])
        G.add_edge(1, 2)

        F = create_vector(G)
        assert(len(F) == 2)
        assert(F[0] == 0)
        assert(F[1] == 0)

        F[0] = 1
        assert(F[0] == 1)



if __name__ == '__main__':
    unittest.main()
