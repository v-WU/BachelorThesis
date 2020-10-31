import re
import sys

import networkx as nx
import numpy as np


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

    def perform_ullman_algorithm(self, matchingGraph, originalGraph):
        self.init(matchingGraph, originalGraph)
        self.step2()
        return self.isomorphism

    def init(self, matchingGraph, orignialGraph):
        self.A = self.create_adj_matrix(matchingGraph)
        self.B = self.create_adj_matrix(orignialGraph)
        self.F = self.create_vector(orignialGraph)
        print("Initial F: " + str(self.F))
        self.H = self.create_vector(matchingGraph)
        self.H.fill(-1)
        print("Initial H: " + str(self.H))
        self.M = self.create_rotation_matrix(matchingGraph, orignialGraph)
        print("Initial M: " + str(self.M))
        self.d = 0  # index in python start at 0
        return

    def create_adj_matrix(self, graph):
        G = np.array(nx.to_numpy_matrix(graph, dtype=int))
        return G

    def create_rotation_matrix(self, matchingGraph, originalGraph):
        """
        :param matchingGraph, originalGraph
        :return: Rotationsmatrix M0
        """

        list1 = nx.get_node_attributes(matchingGraph, "chem")  # list with key and attributes, accessible with index
        attributelist1 = re.findall("([A-Z])", str(list1))  # list with only attributes, accessible with index
        list2 = nx.get_node_attributes(originalGraph, "chem")
        attributelist2 = re.findall("([A-Z])", str(list2))

        self.M = np.zeros(shape=(len(self.A), len(self.B)), dtype=int)

        degA = self.A.sum(axis=0)
        degB = self.B.sum(axis=0)

        for i in range(len(self.A)):
            for j in range(len(self.B)):
                chem1 = attributelist1[i]
                chem2 = attributelist2[j]
                if chem1 == chem2:
                    if degB[j] >= degA[i]:
                        self.M[i][j] = 1

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

        print("step 2")
        if self.bedingung_step2():
            self.step7()
        else:
            assert self.d <= len(self.H) - 1
            assert self.k <= len(self.F) - 1
            self.copyM[self.d] = np.copy(self.M)
            print("step 2: made a copy at depth " + str(self.d))
            print("step 2: M = " + str(self.M))
            if self.d == 0:  # python Indizes beginnt bei 0
                self.k = self.H[0]  # python Indizes beginnt bei 0
                print("step 2: k = " + str(self.k))
                assert self.k <= len(self.F) - 1
                self.step3()
            else:
                self.k = -1
                print("step 2: k = " + str(self.k))
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
        print("step 3")
        assert (self.k <= len(self.F) - 1)
        self.k = self.k + 1
        print("step 3: k = " + str(self.k))
        while self.M[self.d][self.k] == 0 or self.F[self.k] == 1:
            self.k = self.k + 1
            print("step 3: k = " + str(self.k))
        for j in range(len(self.F)):
            if j != self.k:
                self.M[self.d][j] = 0
        print("step 3: changed M to " + str(self.M))
        self.step4()
        return

    def step4(self):
        print("step 4")
        if self.d < len(self.H) - 1:  # Werte von d: 0 bis len(H)-1, wegen Indizesverschiebung von Python
            self.step6()
        else:
            self.isomorphism_check()
            if self.isomorphism:
                return
            else:
                self.step5()
        return

    def step5(self):
        print("step 5")
        if self.bedingung_step5():
            self.step7()
        else:
            self.M = np.copy(self.copyM[self.d])
            print("step 5: M = copyM at depth " + str(self.d))
            print("step 5: M = " + str(self.M))
            self.step3()
        return

    def bedingung_step5(self):
        """
        :return: True, if there is NO j s.d. j>k && F[j]=0 && mdj=1
        """
        value = True
        print("current d = " + str(self.d))
        print("copyM = " + str(self.copyM))
        for j in range(len(self.F)):
            if self.F[j] == 0: # and self.M[self.d][j] == 1:
               if self.copyM[self.d][self.d][j] == 1:
                    assert self.k <= len(self.F) - 1
                    if j > self.k:
                        value = False
                        break
        return value

    def step6(self):
        print("step 6")
        assert self.k <= len(self.F) - 1
        self.H[self.d] = self.k
        print("step 6: H = " + str(self.H))
        self.F[self.k] = 1
        print("step 6: F = " + str(self.F))
        self.d = self.d + 1
        print("step 6: d = " + str(self.d))
        assert self.d <= len(self.H) - 1
        self.step2()
        return

    def step7(self):
        print("step 7")
        if self.d == 0:  # python Indizes beginnt bei 0
            if self.isomorphism != True:  # the algorithm should end here...
                print("Step 7: There exists no subgraphisomorphism between these two graphs")
                return

        else:
            self.F[self.k] = 0
            print("step 7: F = " + str(self.F))
            self.d = self.d - 1
            print("step 7: d = " + str(self.d))
            self.M = np.copy(self.copyM[self.d])
            print("step 7: M = copyM at depth " + str(self.d))
            print("step 7: M = " + str(self.M))
            self.k = self.H[self.d]
            print("step 7: k = " + str(self.k))
            self.step5()
        return

    def isomorphism_check(self):
        print("isomorphismus check ausgeführt mit M = " + str(self.M))
        C = np.matmul(self.M, np.matmul(self.M, self.B).transpose())
        alike = np.array_equal(self.A, C)
        if alike:
            self.isomorphism = True
            print("Yay, isomorphism found!")
        # else:
        # print("Nope, not isomorphic yet")
        return
