import time
import networkx as nx
import matplotlib.pyplot as plt

from src.parser import read_graphs_from_folder_structure
from src.parser import read_graphs_with_cxl

from ullmanAlgorithm import UllmanAlgorithm

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
print("Original graphs: " + str(original_graph))

matching_graph = read_graphs_from_folder_structure("Data/graphs_for_my_testing/matching_graphs/mutagen")
matching_graph = matching_graph + read_graphs_from_folder_structure(
    "Data/graphs_for_my_testing/matching_graphs/nonmutagen")
print("Matching graphs: " + str(matching_graph))

# ullman = UllmanAlgorithm()
# ullman.perform_ullman_algorithm(matching_graph[0][0], original_graph[0][0])
# print("Isomorphism (matching graph 2328 and 3059) and molecule 2328: " + str(ullman.isomorphism))
#
# ulli = UllmanAlgorithm()
# ulli.perform_ullman_algorithm(matching_graph[0][0], original_graph[1][0])
# print("Isomorphism (matching graph 2328 and 3059) and molecule 3059: " + str(ulli.isomorphism))
#
#
# ullman2 = UllmanAlgorithm()
# ullman2.perform_ullman_algorithm(matching_graph[1][0], original_graph[0][0])
# print("Isomorphism (matching graph 1960 and 4204) and molecule 2328: " + str(ullman2.isomorphism))

connected_components = [matching_graph[1][0].subgraph(c).copy() for c in nx.connected_components(matching_graph[1][0])]
print("connectet components: " + str(connected_components))

#ulli2 = UllmanAlgorithm()
#ulli2.perform_ullman_algorithm(matching_graph[1][0], original_graph[2][0])
#print("Isomorphism (matching graph 1960 and 4204) and molecule 4204: " + str(ulli2.isomorphism))

# 2er Molekül
#ulli3 = UllmanAlgorithm()
# nx.draw(connected_components[0])
# plt.show()
#ulli3.perform_ullman_algorithm(connected_components[0], original_graph[2][0])
#print("Isomorphism component 0 and molecule 4204: " + str(ulli3.isomorphism))

# ulli4 = UllmanAlgorithm()
# nx.draw(connected_components[1])
# plt.show()
#ulli4.perform_ullman_algorithm(connected_components[1], original_graph[2][0])
#print("Isomorphism component 1 and molecule 4204: " + str(ulli4.isomorphism))

# 2er molekül
# ulli5 = UllmanAlgorithm()
# nx.draw(connected_components[2])
# plt.show()
# ulli5.perform_ullman_algorithm(connected_components[2], original_graph[2][0])
# print("Isomorphism component 2 and molecule 4204: " + str(ulli5.isomorphism))
# print("last M component 2: " + str(ulli5.M))

ulli6 = UllmanAlgorithm()
# nx.draw(connected_components[3])
# plt.show()
ulli6.perform_ullman_algorithm(connected_components[3], original_graph[2][0])
print("Isomorphism component 3 and molecule 4204: " + str(ulli6.isomorphism))

print("Time taken with Ullman = " + str(time.time() - start_time))
