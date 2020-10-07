import unittest
import networkx as nx
import numpy as np
from ullmanAlgorithm import create_adj_matrix
from ullmanAlgorithm import create_vector
from ullmanAlgorithm import create_rotation_matrix


class MyTestCase(unittest.TestCase):
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
        assert (len(F) == 2)
        assert (F[0] == 0)
        assert (F[1] == 0)

        F[0] = 1
        assert (F[0] == 1)

    def test_create_rotation_matrix(self):
        G1 = nx.Graph()
        G1.add_node(1, chem="H")
        G1.add_node(2, chem="O")
        G1.add_node(3, chem="H")
        G1.add_edge(1, 2)
        G1.add_edge(2, 3)

        G2 = nx.Graph()
        G2.add_node(1, chem="H")
        G2.add_node(2, chem="O")
        G2.add_node(3, chem="H")
        G2.add_node(4, chem="C")
        G2.add_edge(1, 2)
        G2.add_edge(2, 3)
        G2.add_edge(2, 4)

        G3 = nx.Graph()
        G3.add_node(1, chem="H")
        G3.add_node(2, chem="H")
        G3.add_node(3, chem="H")
        G3.add_node(4, chem="H")
        G3.add_edge(1, 2)
        G3.add_edge(2, 3)
        G3.add_edge(2, 4)

        A = create_adj_matrix(G1)
        B1 = create_adj_matrix(G2)
        B2 = create_adj_matrix(G3)

        M = create_rotation_matrix(G1, G2, A, B1)

        assert (M[0][0] == 1)
        assert (M[0][1] == 0)
        assert (M[0][2] == 1)
        assert (M[0][3] == 0)
        assert (M[1][0] == 0)
        assert (M[1][1] == 1)
        assert (M[1][2] == 0)
        assert (M[1][3] == 0)
        assert (M[2][0] == 1)
        assert (M[2][1] == 0)
        assert (M[2][2] == 1)
        assert (M[2][3] == 0)

        N = create_rotation_matrix(G1, G3, A, B2)

        assert (N[0][0] == 1)
        assert (N[0][1] == 1)
        assert (N[0][2] == 1)
        assert (N[0][3] == 1)
        assert (N[1][0] == 0)
        assert (N[1][1] == 0)
        assert (N[1][2] == 0)
        assert (N[1][3] == 0)
        assert (N[1][3] == 0)
        assert (N[2][0] == 1)
        assert (N[2][1] == 1)
        assert (N[2][1] == 1)
        assert (N[2][1] == 1)


if __name__ == '__main__':
    unittest.main()
