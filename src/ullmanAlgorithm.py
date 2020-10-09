import re

import networkx as nx
import numpy as np


def perform_ullman_algorithm(matchingGraph, originalGraph):
    isomorphism = False
    M, F, H = init(matchingGraph, originalGraph)
    M, F, H, d = step1(M, F, H)
    M, F, H, d, k = step2(M, F, H, d)
    return isomorphism


def init(matchingGraph, orignialGraph):
    A = create_adj_matrix(matchingGraph)
    B = create_adj_matrix(orignialGraph)
    F = create_vector(orignialGraph)
    H = create_vector(matchingGraph)
    M = create_rotation_matrix(matchingGraph, orignialGraph, A, B)
    return M, F, H


def create_adj_matrix(graph):
    G = np.array(nx.to_numpy_matrix(graph, dtype=int))
    return G


def create_rotation_matrix(matchingGraph, originalGraph, A, B):
    """
    :param (3) adj. Matrix of matchingGraph, (4) adj. Matrix of originalGraph
    :return: Rotationsmatrix M0
    """

    list1 = nx.get_node_attributes(matchingGraph, "chem")  # list with key and attributes, accessible with index
    attributelist1 = re.findall("([A-Z])", str(list1))  # list with only attributes, accessible with index
    list2 = nx.get_node_attributes(originalGraph, "chem")
    attributelist2 = re.findall("([A-Z])", str(list2))

    M = np.zeros(shape=(len(A), len(B)), dtype=int)

    degA = A.sum(axis=0)
    degB = B.sum(axis=0)

    for i in range(len(A)):
        for j in range(len(B)):
            if degB[j] >= degA[i]:
                chem1 = attributelist1[i]
                chem2 = attributelist2[j]
                if chem1 == chem2:
                    M[i][j] = 1

    return M


def create_vector(graph):
    """
    :param graph:
    :return: zerovector with length = number of nodes of graph
    """
    x = graph.number_of_nodes()
    F = np.zeros(x, dtype=int)
    return F


def step1(M, F, H):
    """
    implemented according to the paper even though it seems useless
    :param (1) Rotations matrix M, (2) Hilfsvektor F, (3) Hilfsvektor H
    :return: M, F, H, d
    """

    d = 1
    return M, F, H, d


def step2(M, F, H, d):
    """
    :param args: (1) Rotations matrix M, (2) Hilfsvektor F, (3) Hilfsvektor H, (4) Indizes d
    :return:
    """

    k = 0

    if bedingung_step2(M, F, d):
        step7()
    else:
        if d == 1:
            k = H[0]
        else:
            k = 0
    return M, F, H, d, k


def bedingung_step2(M, F, d):
    """
    :param args: (1) Rotationsmatrix, (2) Hilfsvektor F, (3) Variable d
    :return: True, if there is NO j s.d. Fj = 0 && mdj = 1
    """

    value = True
    for j in range(len(F)):
        if F[j] == 0 and M[d][j] == 1:
            value = False
            break

    return value


def step3():
    return


def step4():
    return


def step5():
    return


def step6():
    return


def step7():
    return
