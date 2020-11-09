import networkx as nx


def create_simple_graph():
    G = nx.Graph()
    G.add_nodes_from([1, 2])
    G.add_edge(1, 2)
    return G


def create_test_matching_graph():
    G1 = nx.Graph()
    G1.add_node('1', chem="H")
    G1.add_node('2', chem="O")
    G1.add_node('3', chem="H")
    G1.add_edge('1', '2')
    G1.add_edge('2', '3')
    return G1


def create_test_original_graphs():
    G2 = nx.Graph()
    G2.add_node('1', chem="H")
    G2.add_node('2', chem="O")
    G2.add_node('3', chem="H")
    G2.add_node('4', chem="C")
    G2.add_edge('1', '2')
    G2.add_edge('2', '3')
    G2.add_edge('2', '4')

    G3 = nx.Graph()
    G3.add_node('1', chem="H")
    G3.add_node('2', chem="H")
    G3.add_node('3', chem="H")
    G3.add_node('4', chem="H")
    G3.add_edge('1', '2')
    G3.add_edge('2', '3')
    G3.add_edge('2', '4')

    return G2, G3
