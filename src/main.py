import time

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
print(original_graph)

matching_graph = read_graphs_from_folder_structure("Data/graphs_for_my_testing/matching_graphs/mutagen")
matching_graph = matching_graph + read_graphs_from_folder_structure(
    "Data/graphs_for_my_testing/matching_graphs/nonmutagen")
print(matching_graph)

ullman = UllmanAlgorithm()
ullman.perform_ullman_algorithm(matching_graph[0][0], original_graph[0][0])
print("Isomorphism (matching graph 2328 and 3059) and molecule 2328: " + str(ullman.isomorphism))

ulli = UllmanAlgorithm()
ulli.perform_ullman_algorithm(matching_graph[0][0], original_graph[1][0])
print("Isomorphism (matching graph 2328 and 3059) and molecule 3059: " + str(ulli.isomorphism))


ullman2 = UllmanAlgorithm()
ullman2.perform_ullman_algorithm(matching_graph[1][0], original_graph[0][0])
print("Isomorphism (matching graph 1960 and 4204) and molecule 2328: " + str(ullman2.isomorphism))

ulli2 = UllmanAlgorithm()
ulli2.perform_ullman_algorithm(matching_graph[1][0], original_graph[2][0])
print("Isomorphism (matching graph 1960 and 4204) and molecule 4204: " + str(ulli2.isomorphism))

print("Time taken with Ullman = " + str(time.time() - start_time))
