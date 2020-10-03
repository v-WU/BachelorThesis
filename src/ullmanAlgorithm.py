import networkx as nx
import numpy as np


def perform_ullman_algorithm(matchingGraph, originalGraph):
    init(matchingGraph, originalGraph)
    return


def init(matchingGraph, orignialGraph):
    A = create_adj_matrix(matchingGraph)
    B = create_adj_matrix(orignialGraph)
    H = create_vector(matchingGraph)
    F = create_vector(orignialGraph)
    create_rotation_matrix()
    return


def create_adj_matrix(graph):
    G = np.array(nx.to_numpy_matrix(graph, dtype=int))
    return G


def create_rotation_matrix():
    return


def create_vector(graph):
    x = graph.number_of_nodes()
    F = np.zeros(x, dtype=int)
    return F
