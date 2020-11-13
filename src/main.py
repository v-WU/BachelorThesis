import time
import networkx as nx
import matplotlib.pyplot as plt

from src.parser import read_graphs_from_folder_structure
from src.parser import read_graphs_with_cxl

from ullmanAlgorithm import UllmanAlgorithm

import random

random.seed(246)  # or any integer
import numpy

numpy.random.seed(4812)

start_time = time.time()

# original_graphs, set_of_labels = read_graphs_with_cxl("Data/vero_folder/mutagenicity/graphmlFiles")

# no_pruning_graphs = read_graphs_from_folder_structure(
#     "Data/vero_folder/matching_graphs_no_pruning/graphml_files/mutagen")
# no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
#     "Data/vero_folder/matching_graphs_no_pruning/graphml_files/nonmutagen")
#
# pruning_graphs = read_graphs_from_folder_structure("Data/vero_folder/matching_graphs_pruning/graphml_files/mutagen")
# pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
#     "Data/vero_folder/matching_graphs_pruning/graphml_files/nonmutagen")

original_graph = read_graphs_from_folder_structure("Data/graphs_for_my_testing/original_graph_for_testing/mutagen")
original_graph = original_graph + read_graphs_from_folder_structure(
    "Data/graphs_for_my_testing/original_graph_for_testing/nonmutagen")
# print("Original graphs: " + str(original_graph))

matching_graph = read_graphs_from_folder_structure("Data/graphs_for_my_testing/matching_graphs/mutagen")
matching_graph = matching_graph + read_graphs_from_folder_structure(
    "Data/graphs_for_my_testing/matching_graphs/nonmutagen")
# print("Matching graphs: " + str(matching_graph))

# creates a list with all the (unconnected) subgraphs of the matching graph
conn_comps_lst = [sorted(elt) for elt in list(nx.connected_components(matching_graph[1][0]))]
connected_components = []
for ordered_nodes in conn_comps_lst:
    SG = nx.OrderedGraph()
    nodes_to_add = []
    for node in ordered_nodes:
        nodes_to_add.append((node, matching_graph[1][0].nodes[node]))
    SG.add_nodes_from(nodes_to_add)
    SG.add_edges_from((u, v) for (u, v) in matching_graph[1][0].edges() if u in SG if v in SG)
    connected_components.append(SG)

# for component in connected_components:
#     len(component)

# print(connected_components[1].nodes(data=True))
# print("nodes of all_inclusive: " + str(original_graph[3][0].nodes(data=True)))

# subgraphs = nx.connected_components(original_graph[2][0])
# print("Subgraphs: " + str(subgraphs))

print("Nodes of matching graph: " + str(matching_graph[1][0].nodes(data=True)))
print("Nodes of connected_components[1]: " + str(connected_components[1].nodes(data=True)))
print("Nodes of original graph: " + str(original_graph[2][0].nodes(data=True)))

# Vergleich GANZER Matching Graph mit Origial Graph
# ulli2 = UllmanAlgorithm()
# ulli2.perform_ullman_algorithm(matching_graph[1][0], original_graph[2][0], [])
# print("Isomorphism (matching graph 1960 and 4204) and molecule 4204: " + str(ulli2.isomorphism))


# 2er Molekül, Connected_components[0], Isomorphismus: True
# nx.draw(connected_components[0])
# plt.show()
ulli3 = UllmanAlgorithm()
ulli3.perform_ullman_algorithm(connected_components[1], original_graph[2][0], [])
print("Isomorphism component 1 and molecule 4204: " + str(ulli3.isomorphism))


print("Time taken with Ullman = " + str(time.time() - start_time))
