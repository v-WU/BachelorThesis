import networkx as nx
import matplotlib.pyplot as plt


def display(graph):
    G = graph
    nx.draw(G)
    plt.show()


def display_info(graph):
    G = graph
    print("Number of nodes: " + str(G.number_of_nodes()))
    print("Number of edges: " + str(G.number_of_edges()))
    print("List of nodes: " + str(list(G.nodes)))
    print("List of edges: " + str(list(G.edges)))


def display_degree(graph, node):
    G = graph
    print("Degree: " + str(G.degree[node]))


def display_neighbors(graph, node):
    G = graph
    print("List of neighbors: " + str(list(G.neighbors(node))))
