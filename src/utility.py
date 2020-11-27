import networkx as nx


def create_simple_graph():
    G = nx.Graph()
    G.add_nodes_from([1, 2])
    G.add_edge(1, 2)
    return G


def create_test_matching_graph():
    G1 = nx.Graph()
    G1.add_node('1', chem="H", x=1, y=1)
    G1.add_node('2', chem="O", x=1, y=1)
    G1.add_node('3', chem="H", x=1, y=1)
    G1.add_edge('1', '2')
    G1.add_edge('2', '3')
    return G1


def create_test_original_graphs():
    G2 = nx.Graph()
    G2.add_node('1', chem="H", x=1, y=1)
    G2.add_node('2', chem="O", x=1, y=1)
    G2.add_node('3', chem="H", x=1, y=1)
    G2.add_node('4', chem="C", x=1, y=1)
    G2.add_edge('1', '2')
    G2.add_edge('2', '3')
    G2.add_edge('2', '4')

    G3 = nx.Graph()
    G3.add_node('1', chem="H", x=1, y=1)
    G3.add_node('2', chem="H", x=1, y=1)
    G3.add_node('3', chem="H", x=1, y=1)
    G3.add_node('4', chem="H", x=1, y=1)
    G3.add_edge('1', '2')
    G3.add_edge('2', '3')
    G3.add_edge('2', '4')

    return G2, G3


def create_connected_component_1():
    G = nx.Graph()
    G.add_node('17', chem="C", x=1, y=1)
    G.add_node('21', chem="C", x=1, y=1)
    G.add_node('25', chem="C", x=1, y=1)
    G.add_node('64', chem="H", x=1, y=1)
    G.add_node('65', chem="H", x=1, y=1)
    G.add_node('66', chem="H", x=1, y=1)
    G.add_edge('17', '64')
    G.add_edge('17', '21')
    G.add_edge('25', '21')
    G.add_edge('66', '21')
    G.add_edge('65', '21')

    return G


def create_part_original_graph():
    G = nx.Graph()
    G.add_node('23', chem="N", x=1, y=1)
    G.add_node('27', chem="C", x=1, y=1)
    G.add_node('32', chem="C", x=1, y=1)
    G.add_node('38', chem="C", x=1, y=1)
    G.add_node('69', chem="H", x=1, y=1)
    G.add_node('72', chem="H", x=1, y=1)
    G.add_node('75', chem="H", x=1, y=1)
    G.add_node('76', chem="H", x=1, y=1)

    G.add_edge('23', '27')
    G.add_edge('23', '69')
    G.add_edge('27', '72')
    G.add_edge('27', '32')
    G.add_edge('75', '32')
    G.add_edge('76', '32')
    G.add_edge('38', '32')

    return G


def create_graph_11_nodes():
    G = nx.Graph()
    G.add_node('1', chem="O", x=1, y=1)
    G.add_node('2', chem="H", x=1, y=1)
    G.add_node('3', chem="O", x=1, y=1)
    G.add_node('4', chem="O", x=1, y=1)
    G.add_node('5', chem="C", x=1, y=1)
    G.add_node('6', chem="C", x=1, y=1)
    G.add_node('7', chem="O", x=1, y=1)
    G.add_node('8', chem="H", x=1, y=1)
    G.add_node('9', chem="H", x=1, y=1)
    G.add_node('10', chem="O", x=1, y=1)
    G.add_node('11', chem="H", x=1, y=1)

    G.add_edge('1', '2')
    G.add_edge('3', '2')
    G.add_edge('4', '2')
    G.add_edge('5', '2')
    G.add_edge('6', '5')
    G.add_edge('6', '7')
    G.add_edge('7', '8')
    G.add_edge('9', '8')
    G.add_edge('10', '9')
    G.add_edge('11', '3')

    return G


def create_letter_matching_graph():
    G = nx.Graph()
    G.add_node(1, x=0, y=0)
    G.add_node(2, x=0.3, y=0.3)
    G.add_node(3, x=0.6, y=0.9)
    G.add_node(4, x=0.8, y=0.4)
    G.add_edges_from([(1, 2), (2, 3), (2, 4)])
    return G


def create_letter_original_graph():
    G = nx.Graph()
    G.add_node(1, x=0.8, y=0.1)
    G.add_node(2, x=0.3, y=0.2)
    G.add_node(3, x=0, y=0)
    G.add_node(4, x=0.7, y=0.4)
    G.add_node(5, x=0.6, y=0.7)
    G.add_edges_from([(1, 2), (2, 3), (2, 4), (4, 5)])
    return G
