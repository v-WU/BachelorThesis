from ullmanAlgorithm import UllmanAlgorithm
import utility
import numpy as np
import networkx as nx
import re


class TestUllman():

    def test_create_adj_matrix(self):
        ullman = UllmanAlgorithm()
        G = utility.create_simple_graph()

        ullman.A = ullman.create_adj_matrix(G)
        assert (ullman.A[0][0] == 0)
        assert (ullman.A[0][1] == 1)
        assert (ullman.A[1][0] == 1)
        assert (ullman.A[1][1] == 0)

    def test_create_vector(self):
        ullman = UllmanAlgorithm()
        G = utility.create_simple_graph()

        ullman.F = ullman.create_vector(G)
        assert (len(ullman.F) == 2)
        assert (ullman.F[0] == 0)
        assert (ullman.F[1] == 0)

        ullman.F[0] = 1
        assert (ullman.F[0] == 1)

    # no attributes considered
    def test_create_rotation_matrix_1(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, [])

        assert (ullman.M[0][0] == 1)
        assert (ullman.M[0][1] == 1)
        assert (ullman.M[0][2] == 1)
        assert (ullman.M[0][3] == 1)
        assert (ullman.M[1][0] == 0)
        assert (ullman.M[1][1] == 1)
        assert (ullman.M[1][2] == 0)
        assert (ullman.M[1][3] == 0)
        assert (ullman.M[2][0] == 1)
        assert (ullman.M[2][1] == 1)
        assert (ullman.M[2][2] == 1)
        assert (ullman.M[2][3] == 1)

    # attributes not considered
    def test_create_rotation_matrix_with_matched_nodes_0(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.M = ullman.create_rotation_matrix(G1, G2, [0])

        assert (ullman.M[0][0] == 0)
        assert (ullman.M[0][1] == 1)
        assert (ullman.M[0][2] == 1)
        assert (ullman.M[0][3] == 1)
        assert (ullman.M[1][0] == 0)
        assert (ullman.M[1][1] == 1)
        assert (ullman.M[1][2] == 0)
        assert (ullman.M[1][3] == 0)
        assert (ullman.M[2][0] == 0)
        assert (ullman.M[2][1] == 1)
        assert (ullman.M[2][2] == 1)
        assert (ullman.M[2][3] == 1)

    def test_create_rotation_matrix_with_matched_nodes_11(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2 = utility.create_graph_11_nodes()
        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.M = ullman.create_rotation_matrix(G1, G2, [1])

        assert (ullman.M[0][1] == 0)
        assert (ullman.M[1][1] == 0)
        assert (ullman.M[2][1] == 0)

    def test_create_rotation_matrix_attr(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_letter_matching_graph()
        G2 = utility.create_letter_original_graph()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)
        ullman.create_rotation_matrix(G1, G2, [])

        assert (ullman.M[0][0] == 0)
        assert (ullman.M[0][1] == 1)
        assert (ullman.M[0][2] == 1)
        assert (ullman.M[0][3] == 0)
        assert (ullman.M[0][4] == 0)
        assert (ullman.M[1][0] == 0)
        assert (ullman.M[1][1] == 1)
        assert (ullman.M[1][2] == 0)
        assert (ullman.M[1][3] == 0)
        assert (ullman.M[1][4] == 0)
        assert (ullman.M[2][0] == 0)
        assert (ullman.M[2][1] == 0)
        assert (ullman.M[2][2] == 0)
        assert (ullman.M[2][3] == 1)
        assert (ullman.M[2][4] == 1)
        assert (ullman.M[3][0] == 1)
        assert (ullman.M[3][1] == 1)
        assert (ullman.M[3][2] == 0)
        assert (ullman.M[3][3] == 1)
        assert (ullman.M[3][4] == 1)

    def test_bedingung_step2(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)
        ullman.create_rotation_matrix(G1, G2, [])
        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_vector(G1)

        # d entspricht den Zeilen in der Rotationsmatrix
        # Assertion: "in jeder Zeile existiert ein j s.d. Fj=0 && mdj=1"
        # es werden NICHT die einzelnen Einträge überprüft, sondern die ganze Matrixzeile...
        for ullman.d in range(3):
            assert not (ullman.bedingung_step2())

    def test_bedingung_step2_F1(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, [])
        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_vector(G1)

        # Falls alle Einträge in F = 1
        for ullman.d in range(3):
            ullman.F.fill(1)
            assert ullman.bedingung_step2()

    def test_bedingung_step2_M0(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, [])
        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_vector(G1)

        # Falls alle Einträge in M = 0
        for ullman.d in range(3):
            ullman.M.fill(0)
            assert (ullman.bedingung_step2())

    def test_step2_else(self, mocker):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, [])
        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_vector(G1)
        ullman.H[0] = 1
        ullman.d = 0

        mocker.patch.object(ullman, 'step3', return_value=None)

        ullman.step2()
        assert (ullman.k == 1)
        assert np.array_equal(ullman.copyM[ullman.d], ullman.M)

        ullman.d = 2
        ullman.step2()
        assert (ullman.k == -1)
        assert np.array_equal(ullman.copyM[ullman.d], ullman.M)

    def test_step7_exit(self):
        ullman = UllmanAlgorithm()
        ullman.d = 0
        ullman.step7()
        assert not ullman.isomorphism

    def test_step7_else(self, mocker):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()
        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_vector(G1)
        ullman.F.fill(1)  # to make sure it changes back to 0
        ullman.H.fill(1)
        ullman.d = 2
        ullman.k = 0

        ullman.copyM[ullman.d - 1] = [[0, 0], [0, 0]]

        mocker.patch.object(ullman, 'step5', return_value=None)

        ullman.step7()
        assert np.array_equal(ullman.M, ullman.copyM[ullman.d])
        assert (ullman.F[1] == 0)  # Indizes manuell gesetzt, da k in step 7 nochmal verändert wird
        assert (ullman.d == 1)
        assert (ullman.k == 1)

    def test_bedingung_step5_F1(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, [])
        ullman.F = ullman.create_vector(G2)

        # Falls alle Einträge in F = 1
        for ullman.d in range(3):
            ullman.F.fill(1)
            assert ullman.bedingung_step5()

    def test_bedingung_step5_M0(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, [])
        ullman.F = ullman.create_vector(G2)

        # Falls alle Einträge in M = 0
        for ullman.d in range(3):
            ullman.M.fill(0)
            ullman.copyM[ullman.d] = np.copy(ullman.M)
            assert (ullman.bedingung_step5())

    def test_bedingung_step5_ok(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, [])
        ullman.F = ullman.create_vector(G2)

        # d entspricht den Zeilen in der Rotationsmatrix
        # Assertion: "in jeder Zeile existiert ein j s.d. Fj=0 && mdj=1"
        # es werden NICHT die einzelnen Einträge überprüft, sondern die ganze Matrixzeile...
        for ullman.k in range(1):  # Bedingung gilt im Beispiel nur für k=0,1
            for ullman.d in range(3):
                ullman.copyM[ullman.d] = np.copy(ullman.M)
                assert not (ullman.bedingung_step5())

    def test_bedingung_step5_fail(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, [])
        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_adj_matrix(G1)

        ullman.k = 3  # manuell gesetzt, s.d Bedingung j>k überprüft werden kann
        # d entspricht den Zeilen in der Rotationsmatrix
        for ullman.d in range(3):
            ullman.copyM[ullman.d] = np.copy(ullman.M)
            assert (ullman.bedingung_step5())

    def test_step3_k0d0(self, mocker):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)

        ullman.create_rotation_matrix(G1, G2, [])
        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_vector(G1)
        ullman.k = 0
        ullman.d = 0

        mocker.patch.object(ullman, 'step4', return_value=None)
        mocker.patch.object(ullman, 'refine', return_value=True)

        ullman.step3()

        assert (ullman.M[0][0] == 0)
        assert (ullman.M[0][1] == 1)
        assert (ullman.M[0][2] == 0)
        assert (ullman.M[0][3] == 0)
        assert (ullman.M[1][0] == 0)
        assert (ullman.M[1][1] == 1)
        assert (ullman.M[1][2] == 0)
        assert (ullman.M[1][3] == 0)
        assert (ullman.M[2][0] == 1)
        assert (ullman.M[2][1] == 1)
        assert (ullman.M[2][2] == 1)
        assert (ullman.M[2][3] == 1)

    def test_step6(self, mocker):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, _ = utility.create_test_original_graphs()

        ullman.F = ullman.create_vector(G2)
        ullman.H = ullman.create_vector(G1)

        ullman.H.fill(1)

        ullman.k = 0
        ullman.d = 0
        mocker.patch.object(ullman, 'step2', return_value=None)
        ullman.step6()

        assert (ullman.H[0] == 0)
        assert (ullman.F[0] == 1)
        assert (ullman.d == 1)

    def test_isomorphism_check_true(self):
        ullman = UllmanAlgorithm()
        ullman.A = [[2, 0], [2, 1]]
        ullman.B = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
        ullman.M = [[1, 0, 1], [0, 1, 0]]

        ullman.isomorphism_check()

        assert ullman.isomorphism

    def test_isomorphism_check_false(self):
        ullman = UllmanAlgorithm()
        ullman.A = [[1, 0], [1, 1]]
        ullman.B = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
        ullman.M = [[1, 0, 1], [0, 1, 0]]

        ullman.isomorphism_check()

        assert not ullman.isomorphism

    def test_isomorphism_check_true2(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)
        ullman.M = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]

        ullman.isomorphism_check()

        assert ullman.isomorphism

    def test_perform_ullman_algorithm_iso(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()
        ullman.perform_ullman_algorithm(G1, G2, [])
        assert ullman.isomorphism

    # attributes not considered
    def test_perform_ullman_algorithm_not_iso(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G1.add_node('4', chem="O", x=1, y=1)
        G1.add_edges_from([('2', '4')])
        G2, G3 = utility.create_test_original_graphs()
        G3.remove_edge('2', '4')
        G3.add_edges_from([('1', '4')])
        ullman.perform_ullman_algorithm(G1, G3, [])
        assert not ullman.isomorphism

    def test_refine_fail(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G1.add_node('4', chem="O", x=1, y=1)
        G1.add_edge('2', '4')
        G2, G3 = utility.create_test_original_graphs()
        G3.remove_edge('2', '4')
        G3.add_edges_from([('1', '4')])

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G3)
        ullman.M = ullman.create_rotation_matrix(G1, G3, [])
        print("M: " + str(ullman.M))
        ullman.H = ullman.create_vector(G1)
        ullman.F = ullman.create_vector(G3)
        ullman.matchingGraph = G1
        ullman.originalGraph = G3

        value = ullman.refine()
        assert not value

    def test_refinement_succeed_neighbors(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_letter_matching_graph()
        G2 = utility.create_letter_original_graph()
        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)
        ullman.M = ullman.create_rotation_matrix(G1, G2, [])
        ullman.H = ullman.create_vector(G1)
        ullman.F = ullman.create_vector(G2)
        ullman.matchingGraph = G1
        ullman.originalGraph = G2

        value = ullman.refine()
        assert value
        assert (ullman.M[0][0] == 0)
        assert (ullman.M[0][1] == 0)
        assert (ullman.M[0][2] == 1)
        assert (ullman.M[0][3] == 0)
        assert (ullman.M[0][4] == 0)
        assert (ullman.M[1][0] == 0)
        assert (ullman.M[1][1] == 1)
        assert (ullman.M[1][2] == 0)
        assert (ullman.M[1][3] == 0)
        assert (ullman.M[1][4] == 0)
        assert (ullman.M[2][0] == 0)
        assert (ullman.M[2][1] == 0)
        assert (ullman.M[2][2] == 0)
        assert (ullman.M[2][3] == 1)
        assert (ullman.M[2][4] == 0)
        assert (ullman.M[3][0] == 1)
        assert (ullman.M[3][1] == 0)
        assert (ullman.M[3][2] == 0)
        assert (ullman.M[3][3] == 1)
        assert (ullman.M[3][4] == 0)

    def test_check_rows_empty(self):
        ullman = UllmanAlgorithm()
        ullman.M = np.array([[1, 1, 0], [0, 0, 0]])
        assert ullman.check_rows()

    def test_check_rows_non_empty(self):
        ullman = UllmanAlgorithm()
        ullman.M = np.array([[1, 1, 0], [0, 1, 0]])
        assert not ullman.check_rows()

    def test_get_list_with_attributes_of_neighbor_in_matching_graph(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)
        ullman.M = ullman.create_rotation_matrix(G1, G2, [])
        ullman.H = ullman.create_vector(G1)
        ullman.F = ullman.create_vector(G2)
        ullman.matchingGraph = G1
        ullman.originalGraph = G2

        list1 = nx.get_node_attributes(ullman.matchingGraph,
                                       "chem")  # list with key and attributes, accessible with index
        keylist = re.findall(r'\d+', str(list1))  # list with only key, accessible with index
        list = ullman.get_list_with_attributes_of_neighbor_in_matching_graph(keylist, 0)
        assert (len(list) == 1)
        assert ("O" in list)

    def test_get_list_with_attributes_of_neighbor_in_original_graph(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()

        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)
        ullman.M = ullman.create_rotation_matrix(G1, G2, [])
        ullman.H = ullman.create_vector(G1)
        ullman.F = ullman.create_vector(G2)
        ullman.matchingGraph = G1
        ullman.originalGraph = G2

        list1 = nx.get_node_attributes(ullman.originalGraph,
                                       "chem")  # list with key and attributes, accessible with index
        keylist = re.findall(r'\d+', str(list1))  # list with only key, accessible with index
        list = ullman.get_list_with_attributes_of_neighbor_in_original_graph(keylist, 0)
        assert (len(list) == 1)
        assert ("O" in list)

    def test_refine_big(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_connected_component_1()
        G2 = utility.create_part_original_graph()
        ullman.A = ullman.create_adj_matrix(G1)
        ullman.B = ullman.create_adj_matrix(G2)
        ullman.M = ullman.create_rotation_matrix(G1, G2, [])
        ullman.H = ullman.create_vector(G1)
        ullman.F = ullman.create_vector(G2)
        ullman.matchingGraph = G1
        ullman.originalGraph = G2

        value = ullman.refine()
        assert value

    def test_refinement_iso_false(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_test_matching_graph()
        G2, G3 = utility.create_test_original_graphs()
        G1.add_node('4', chem="N", x=1, y=1)
        G1.add_edge('1', '4')

        ullman.perform_ullman_algorithm(G1, G2, [])

        assert not ullman.isomorphism

    def test_find_matched_nodes(self):
        ullman = UllmanAlgorithm()
        ullman.M = [[0, 0, 1], [0, 1, 0]]
        matched_nodes = ullman.find_matched_nodes()
        assert np.array_equal(matched_nodes, [2, 1])

    def test_letter_ullman_iso(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_letter_matching_graph()
        G2 = utility.create_letter_original_graph()
        ullman.perform_ullman_algorithm(G1, G2, [])
        assert ullman.isomorphism

    def test_letter_ullman_not_iso(self):
        ullman = UllmanAlgorithm()
        G1 = utility.create_letter_matching_graph()
        G2 = utility.create_letter_original_graph()
        G2.remove_edge(2, 3)
        ullman.perform_ullman_algorithm(G1, G2, [])
        assert not ullman.isomorphism

    def test_letter_iso_unconnected_true(self):
        ullman = UllmanAlgorithm()
        G1 = nx.Graph()
        G1.add_edges_from([(1, 2), (3, 4), (4, 5)])
        nx.set_node_attributes(G1, 1, "x")
        nx.set_node_attributes(G1, 1, "y")
        G2 = nx.Graph()
        G2.add_edges_from([(1, 2), (2, 3), (2, 4), (4, 5)])
        nx.set_node_attributes(G2, 1, "x")
        nx.set_node_attributes(G2, 1, "y")
        ullman.perform_ullman_algorithm(G1, G2, [])
        assert ullman.isomorphism

    def test_letter_iso_unconnected_false(self):
        ullman = UllmanAlgorithm()
        G1 = nx.Graph()
        G1.add_edges_from([(1, 2), (3, 4), (4, 5), (4, 6)])
        nx.set_node_attributes(G1, 1, "x")
        nx.set_node_attributes(G1, 1, "y")
        G2 = nx.Graph()
        G2.add_edges_from([(1, 2), (1, 3), (2, 4), (4, 5), (5, 6)])
        nx.set_node_attributes(G2, 1, "x")
        nx.set_node_attributes(G2, 1, "y")
        ullman.perform_ullman_algorithm(G1, G2, [])
        assert not ullman.isomorphism
