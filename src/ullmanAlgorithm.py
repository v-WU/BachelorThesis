import networkx as nx
import numpy as np


def perform_ullman_algorithm(matchingGraph, originalGraph):
    init(matchingGraph, originalGraph)
    return


def init(matchingGraph, orignialGraph):
    A = create_adj_matrix(matchingGraph)
    B = create_adj_matrix(orignialGraph)
    F = create_vector(orignialGraph)
    H = create_vector(matchingGraph)
    M = create_rotation_matrix(matchingGraph, orignialGraph, A, B)
    return M, F, H


def create_adj_matrix(Graph):
    G = np.array(nx.to_numpy_matrix(Graph, dtype=int))
    return G


def create_rotation_matrix(*args):
    """
    :param args: (1) matching Graph, (2) original Graph, (3) adj. matrix matching Graph, (4) adj. matrix original Graph
    :return: M0
    """
    A = args[2]
    B = args[3]

    M = np.zeros(shape=(len(A), len(B)), dtype=int)

    degA = A.sum(axis=0)
    degB = B.sum(axis=0)

    for i in range(len(A)):
        for j in range(len(B)):
            if degB[j] >= degA[i]:
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
