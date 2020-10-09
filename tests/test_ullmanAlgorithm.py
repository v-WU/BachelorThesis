import unittest
from ullmanAlgorithm import create_adj_matrix
from ullmanAlgorithm import create_vector
from ullmanAlgorithm import create_rotation_matrix
from ullmanAlgorithm import bedingung_step2
from ullmanAlgorithm import step2
import utility


class MyTestCase(unittest.TestCase):
    def test_create_adj_matrix(self):
        G = utility.create_simple_graph()

        A = create_adj_matrix(G)
        assert (A[0][0] == 0)
        assert (A[0][1] == 1)
        assert (A[1][0] == 1)
        assert (A[1][1] == 0)

    def test_create_vector(self):
        G = utility.create_simple_graph()

        F = create_vector(G)
        assert (len(F) == 2)
        assert (F[0] == 0)
        assert (F[1] == 0)

        F[0] = 1
        assert (F[0] == 1)

    def test_create_rotation_matrix(self):
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()

        matrixG1 = create_adj_matrix(G1)
        matrixG2 = create_adj_matrix(G2)
        matrixG3 = create_adj_matrix(G3)

        M = create_rotation_matrix(G1, G2, matrixG1, matrixG2)

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

        N = create_rotation_matrix(G1, G3, matrixG1, matrixG3)

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

    def test_bedingung_step2(self):
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = create_adj_matrix(G1)
        matrixG2 = create_adj_matrix(G2)

        M = create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        F = create_vector(G2)

        # d entspricht den Zeilen in der Rotationsmatrix
        for d in range(3):
            self.assertFalse(bedingung_step2(M, F, d))

        # Falls alle Einträge in F = 1
        for d in range(3):
            F.fill(1)
            self.assertTrue(bedingung_step2(M, F, d))

        # Falls alle Einträge in M = 0
        for d in range(3):
            M.fill(0)
            self.assertTrue(bedingung_step2(M, F, d))

    def test_step2(self):
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = create_adj_matrix(G1)
        matrixG2 = create_adj_matrix(G2)

        M = create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        F = create_vector(G2)
        H = create_vector(G1)
        H[0] = 1
        d = 1

        M, F, H, d, k = step2(M, F, H, d)
        assert (k == 1)

        d = 2
        M, F, H, d, k = step2(M, F, H, d)
        assert (k == 0)


if __name__ == '__main__':
    unittest.main()
