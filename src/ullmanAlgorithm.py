import re
import sys

import networkx as nx
import numpy as np

sys.setrecursionlimit(5000)


class UllmanAlgorithm:

    def __init__(self):
        self.A = []
        self.B = []
        self.M = []
        self.copyM = {}
        self.F = []
        self.H = []
        self.d = 0
        self.k = -1  # paper k = 0 ist kein Indizes sondern "noch nicht in der Matrix"
        self.isomorphism = False
        self.counter = 0
        self.matchingGraph = None
        self.originalGraph = None
        self.matched_nodes_indizes = []  # contains indizes of matched nodes of prev runs and current run

    def perform_ullman_algorithm(self, matchingGraph, originalGraph, matched_nodes_indizes):
        self.init(matchingGraph, originalGraph, matched_nodes_indizes)
        if self.refine():
            self.step2()
        return self.isomorphism

    def init(self, matchingGraph, orignialGraph, matched_nodes_indizes):
        self.A = self.create_adj_matrix(matchingGraph)
        self.B = self.create_adj_matrix(orignialGraph)
        self.F = self.create_vector(orignialGraph)
        self.H = self.create_vector(matchingGraph)
        self.H.fill(-1)
        self.M = self.create_rotation_matrix(matchingGraph, orignialGraph, matched_nodes_indizes)
        self.d = 0  # index in python start at 0
        self.matchingGraph = matchingGraph
        self.originalGraph = orignialGraph
        self.matched_nodes_indizes = matched_nodes_indizes
        return

    def create_adj_matrix(self, graph):
        G = np.array(nx.to_numpy_matrix(graph, dtype=int))
        return G

    def create_rotation_matrix(self, matchingGraph, originalGraph, matched_nodes_indizes):
        """
        :param matchingGraph, originalGraph
        :return: Rotationsmatrix M0
        """

        list1_x = matchingGraph.nodes("x")
        list1_y = matchingGraph.nodes("y")
        list1 = []
        for node in matchingGraph.nodes:
            coordinate = (list1_x[node], list1_y[node])
            list1.append(coordinate)

        list2_x = originalGraph.nodes("x")
        list2_y = originalGraph.nodes("y")
        list2 = []
        for node in originalGraph.nodes:
            coordinate = (list2_x[node], list2_y[node])
            list2.append(coordinate)

        self.M = np.zeros(shape=(len(self.A), len(self.B)), dtype=int)

        degA = self.A.sum(axis=0)
        degB = self.B.sum(axis=0)

        for i in range(len(self.A)):
            for j in range(len(self.B)):
                if degB[j] >= degA[i]:
                    dist = np.linalg.norm(np.array(list1[i]).astype(float) - np.array(list2[j]).astype(float))
                    if dist < 0.6:
                        self.M[i][j] = 1

                if j in matched_nodes_indizes:
                    self.M[i][j] = 0

        return self.M

    def create_vector(self, graph):
        """
        :param graph:
        :return: zerovector with length = number of nodes of graph
        """
        x = graph.number_of_nodes()
        F = np.zeros(x, dtype=int)
        return F

    def step2(self):
        """
        :param args: (1) Rotations matrix M, (2) Hilfsvektor F, (3) Hilfsvektor H, (4) Indizes d
        :return:
        """

        if self.bedingung_step2():
            self.step7()
        else:
            assert self.d <= len(self.H) - 1
            assert self.k <= len(self.F) - 1
            self.copyM[self.d] = np.copy(self.M)
            if self.d == 0:  # python Indizes beginnt bei 0
                self.k = self.H[0]  # python Indizes beginnt bei 0
                assert self.k <= len(self.F) - 1
                self.step3()
            else:
                self.k = -1
                self.step3()
        return

    def bedingung_step2(self):
        """
        :return: True, if there is NO j s.d. Fj = 0 && mdj = 1
        """

        value = True
        assert self.d <= len(self.H) - 1
        for j in range(len(self.F)):
            if self.F[j] == 0 and self.M[self.d][j] == 1:
                value = False
                break

        return value

    def step3(self):
        assert (self.k <= len(self.F) - 1)
        self.k = self.k + 1
        while self.M[self.d][self.k] == 0 or self.F[self.k] == 1:
            self.k = self.k + 1
        for j in range(len(self.F)):
            if j != self.k:
                self.M[self.d][j] = 0
        if self.refine():
            self.step4()
        else:
            self.step5()
        return

    def step4(self):
        if self.d < len(self.H) - 1:  # Werte von d: 0 bis len(H)-1, wegen Indizesverschiebung von Python
            self.step6()
        else:
            # these lines are no longer necessary because the refinement is in place
            # self.isomorphism_check()
            # if self.isomorphism:
            #     return
            # else:
            #     self.step5()

            self.isomorphism = True
            # new_matches = self.find_matched_nodes()
            # self.matched_nodes_indizes = np.concatenate((self.matched_nodes_indizes, new_matches), 0)
            # self.matched_nodes_indizes = self.matched_nodes_indizes.astype(int)
            # print("all matched nodes indizes: " + str(self.matched_nodes_indizes))
            # self.isomorphism_check()
            # print("Isomorphism should be found! It is: " + str(self.isomorphism))
        return

    def step5(self):
        if self.bedingung_step5():
            self.step7()
        else:
            self.M = np.copy(self.copyM[self.d])
            self.step3()
        return

    def bedingung_step5(self):
        """
        :return: True, if there is NO j s.d. j>k && F[j]=0 && mdj=1
        """
        value = True
        # print("copyM = " + str(self.copyM))
        for j in range(len(self.F)):
            if self.F[j] == 0:
                if self.copyM[self.d][self.d][j] == 1:  # in self.M steht schon die veränderte Zeile mit nur einer 1
                    assert self.k <= len(self.F) - 1
                    if j > self.k:
                        value = False
                        break
        return value

    def step6(self):
        assert self.k <= len(self.F) - 1
        self.H[self.d] = self.k
        self.F[self.k] = 1
        self.d = self.d + 1
        assert self.d <= len(self.H) - 1
        self.step2()
        return

    def step7(self):
        if self.d == 0:  # python Indizes beginnt bei 0
            if not self.isomorphism:  # the algorithm should end here...
                # print("Step 7: There exists no subgraphisomorphism between these two graphs")
                return

        else:
            self.d = self.d - 1
            self.k = self.H[self.d]
            self.F[self.k] = 0
            self.M = np.copy(self.copyM[self.d])
            self.step5()
        return

    # this is no longer necessary because the refinement is in place
    def isomorphism_check(self):
        self.counter = self.counter + 1
        print(str(self.counter) + ". isomorphismus check ausgeführt.")
        # " mit M = " + str(self.M))
        C = np.matmul(self.M, np.matmul(self.M, self.B).transpose())
        alike = np.array_equal(self.A, C)
        if alike:
            self.isomorphism = True
            print("Yay, isomorphism found!")
        else:
            print("Nope, not isomorphic yet")
        return

    def refine(self):
        value = True
        # list1 = nx.get_node_attributes(self.matchingGraph,
        #                                "chem")  # list with key and attributes, accessible with index
        # keylist1 = re.findall(r'\d+', str(list1))  # list with only key, accessible with index
        #
        # list2 = nx.get_node_attributes(self.originalGraph,
        #                                "chem")  # list with key and attributes, accessible with index
        # keylist2 = re.findall(r'\d+', str(list2))  # list with only key, accessible with index

        keylist1 = list(self.matchingGraph.nodes)
        keylist2 = list(self.originalGraph.nodes)

        copy = None
        while not np.array_equal(copy, self.M):
            copy = self.M.copy()
            for i in range(len(self.H)):
                for j in range(len(self.F)):
                    if self.M[i][j] == 1:
                        node_id_matching_graph = keylist1[i]  # get node ID
                        key_neighbors_matching_graph = list(
                            self.matchingGraph.neighbors(node_id_matching_graph))  # list with keys of neighbors of Ai
                        node_id_original_graph = keylist2[j]  # get node ID
                        key_neighbors_original_graph = list(
                            self.originalGraph.neighbors(node_id_original_graph))  # list with keys of neighbors of Bj

                        for key_m in key_neighbors_matching_graph:
                            possible_neighbor = False
                            for key_o in key_neighbors_original_graph:
                                x = keylist1.index(key_m)
                                y = keylist2.index(key_o)
                                if self.M[x][y] == 1:
                                    possible_neighbor = True
                                    break
                            if not possible_neighbor:
                                self.M[i][j] = 0
                                empty_row = self.check_rows()
                                if empty_row:
                                    value = False

        return value

    def check_rows(self):
        empty_row = False
        degM = self.M.sum(axis=1)  # sum of each row in M
        for l in range(len(degM)):  # iterate through every colum
            if degM[l] == 0:
                empty_row = True
                break
        return empty_row

    def get_list_with_attributes_of_neighbor_in_matching_graph(self, keylist, i):
        node_id = keylist[i]  # get node ID
        key_neighbours = list(self.matchingGraph.neighbors(node_id))  # list with keys of neighbors of Ai
        attributes1 = nx.get_node_attributes(self.matchingGraph, 'chem')
        att_neighbors = []
        for x in key_neighbours:
            att_neighbors.append(attributes1[x])  # list with attributes of neighbors of Ai
        return att_neighbors

    def get_list_with_attributes_of_neighbor_in_original_graph(self, keylist, j):
        node_id = keylist[j]  # get node ID
        key_neighbors = list(
            self.originalGraph.neighbors(node_id))  # list with keys of neighbors of Ai
        attributes1 = nx.get_node_attributes(self.originalGraph, 'chem')
        att_neighbors = []
        for x in key_neighbors:
            att_neighbors.append(attributes1[x])  # list with attributes of neighbors of Ai
        return att_neighbors

    def find_matched_nodes(self):
        print("M: " + str(self.M))
        result = np.where(np.array(self.M) == 1)
        newly_matched_nodes_indizes = result[1]
        return newly_matched_nodes_indizes
