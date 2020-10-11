from ullmanAlgorithm import UllmanAlgorithm
import utility


class TestUllman():

    def test_create_adj_matrix(self):
        ullman = UllmanAlgorithm()
        G = utility.create_simple_graph()

        A = ullman.create_adj_matrix(G)
        assert (A[0][0] == 0)
        assert (A[0][1] == 1)
        assert (A[1][0] == 1)
        assert (A[1][1] == 0)

    def test_create_vector(self):
        ullman = UllmanAlgorithm()
        G = utility.create_simple_graph()

        ullman.F = ullman.create_vector(G)
        assert (len(ullman.F) == 2)
        assert (ullman.F[0] == 0)
        assert (ullman.F[1] == 0)

        ullman.F[0] = 1
        assert (ullman.F[0] == 1)

    def test_create_rotation_matrix(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)
        matrixG3 = ullman.create_adj_matrix(G3)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)

        assert (ullman.M[0][0] == 1)
        assert (ullman.M[0][1] == 0)
        assert (ullman.M[0][2] == 1)
        assert (ullman.M[0][3] == 0)
        assert (ullman.M[1][0] == 0)
        assert (ullman.M[1][1] == 1)
        assert (ullman.M[1][2] == 0)
        assert (ullman.M[1][3] == 0)
        assert (ullman.M[2][0] == 1)
        assert (ullman.M[2][1] == 0)
        assert (ullman.M[2][2] == 1)
        assert (ullman.M[2][3] == 0)

        ullman2 = UllmanAlgorithm()
        ullman2.create_rotation_matrix(G1, G3, matrixG1, matrixG3)

        assert (ullman2.M[0][0] == 1)
        assert (ullman2.M[0][1] == 1)
        assert (ullman2.M[0][2] == 1)
        assert (ullman2.M[0][3] == 1)
        assert (ullman2.M[1][0] == 0)
        assert (ullman2.M[1][1] == 0)
        assert (ullman2.M[1][2] == 0)
        assert (ullman2.M[1][3] == 0)
        assert (ullman2.M[1][3] == 0)
        assert (ullman2.M[2][0] == 1)
        assert (ullman2.M[2][1] == 1)
        assert (ullman2.M[2][1] == 1)
        assert (ullman2.M[2][1] == 1)

    def test_bedingung_step2(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)

        # d entspricht den Zeilen in der Rotationsmatrix
        # Assertion: "in jeder Zeile existiert ein j s.d. Fj=0 && mdj=1"
        # es werden NICHT die einzelnen Einträge überprüft, sondern die ganze Matrixzeile...
        for ullman.d in range(3):
            assert not (ullman.bedingung_step2())

    def test_bedingung_step2_F1(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)

        # Falls alle Einträge in F = 1
        for ullman.d in range(3):
            ullman.F.fill(1)
            assert ullman.bedingung_step2()

    def test_bedingung_step2_M0(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)

        # Falls alle Einträge in M = 0
        for ullman.d in range(3):
            ullman.M.fill(0)
            assert (ullman.bedingung_step2())

    def test_step2(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_vector(G1)
        ullman.H[0] = 1
        ullman.d = 1

        ullman.step2()
        assert (ullman.k == 1)

        ullman.d = 2
        ullman.step2()
        assert (ullman.k == 0)

    def test_step7_exit(self):
        ullman = UllmanAlgorithm()
        ullman.d = 1
        ullman.step7()
        assert not ullman.isomorphism

    def test_step7(self, mocker):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()
        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_vector(G1)
        ullman.F.fill(1)  # to make sure it changes back to 0
        ullman.H.fill(1)
        ullman.d = 2
        ullman.k = 0

        mocker.patch.object(ullman, 'step5', return_value=None)

        ullman.step7()
        assert (ullman.F[0] == 0)  # Indizes manuell gesetzt, da k in step 7 nochmal verändert wird
        assert (ullman.d == 1)
        assert (ullman.k == 1)

    def test_bedingung_step5_F1(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)

        # Falls alle Einträge in F = 1
        for ullman.d in range(3):
            ullman.F.fill(1)
            assert ullman.bedingung_step5()

    def test_bedingung_step5_M0(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)

        # Falls alle Einträge in M = 0
        for ullman.d in range(3):
            ullman.M.fill(0)
            assert (ullman.bedingung_step5())

    def test_bedingung_step5_ok(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)

        # d entspricht den Zeilen in der Rotationsmatrix
        # Assertion: "in jeder Zeile existiert ein j s.d. Fj=0 && mdj=1"
        # es werden NICHT die einzelnen Einträge überprüft, sondern die ganze Matrixzeile...
        for ullman.k in range(1):  # Bedingung gilt im Beispiel nur für k=0,1
            for ullman.d in range(3):
                assert not (ullman.bedingung_step5())

    def test_bedingung_step5_fail(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)

        ullman.k = 3  # manuell gesetzt, s.d Bedingung j>k überprüft werden kann
        # d entspricht den Zeilen in der Rotationsmatrix
        for ullman.d in range(3):
            assert (ullman.bedingung_step5())

    # ToDo implement test step5
    def test_step5(self, mocker):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)

        mocker.patch.object(ullman, 'step7', return_value='7')
        mocker.patch.object(ullman, 'step3', return_value='3')

        assert True

    def test_step3_k0d0(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        matrixG1 = ullman.create_adj_matrix(G1)
        matrixG2 = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, matrixG1, matrixG2)
        ullman.F = ullman.create_vector(G2)
        ullman.k = 0
        ullman.d = 0

        ullman.step3()

        assert (ullman.M[0][0] == 0)
        assert (ullman.M[0][1] == 0)
        assert (ullman.M[0][2] == 1)
        assert (ullman.M[0][3] == 0)
        assert (ullman.M[1][0] == 0)
        assert (ullman.M[1][1] == 1)
        assert (ullman.M[1][2] == 0)
        assert (ullman.M[1][3] == 0)
        assert (ullman.M[2][0] == 1)
        assert (ullman.M[2][1] == 0)
        assert (ullman.M[2][2] == 1)
        assert (ullman.M[2][3] == 0)

    def test_perform_ullman_algorithm(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()
        ullman.perform_ullman_algorithm(G1, G2)
        assert ullman.isomorphism
