import time
import sys
import networkx as nx
import matplotlib.pyplot as plt

from src.parser import read_graphs_from_folder_structure
from src.parser import read_graphs_with_cxl
from src.parser import create_abs_path

from ullmanAlgorithm import UllmanAlgorithm

import random

random.seed(246)  # or any integer
import numpy

numpy.random.seed(4812)

start_time = time.time()

original_graphs, set_of_labels = read_graphs_with_cxl("Data/vero_folder_letter/letter/graphmlFiles")
print("number of original graphs: " + str(len(original_graphs)))
print("set of labels: " + str(set_of_labels))

no_pruning_graphs = read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/A")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/E")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/F")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/H")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/I")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/K")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/L")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/M")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/N")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/T")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/V")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/W")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/X")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/Y")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6/graphml_files/Z")

print("number of no pruning matching graphs: " + str(len(no_pruning_graphs)))

pruning_graphs = read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/A")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/E")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/F")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/H")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/I")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/K")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/L")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/M")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/N")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/T")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/V")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/W")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/X")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/Y")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder_letter/matching_graphs_pruning_costs_1.6/graphml_files/Z")

print("number of pruning matching graphs: " + str(len(pruning_graphs)))

print("Time taken to read graphs: " + str(time.time() - start_time))

for i in range(1200):
    name_of_file = str(pruning_graphs[i][1])  # change to no_pruning
    save_path = create_abs_path("letter_results/pruning/" + name_of_file)   # change to no_pruning
    complete_name = save_path + ".txt"
    sys.stdout = open(complete_name, "w")

    for graph in original_graphs:
        ullman = UllmanAlgorithm()
        ullman.perform_ullman_algorithm(pruning_graphs[i][0], graph[0], [])   # change to no_pruning
        print(
            "matching graph='" + str(pruning_graphs[i][1]) + "', class='" + str(  # change to no_pruning
                pruning_graphs[i][2]) + "' and original graph='" + str(  # change to no_pruning
                graph[1]) + "', class='" + str(graph[2]) + "': isomorphism=" + str(
                ullman.isomorphism))

    sys.stdout.close()

# creates a list with all the (unconnected) subgraphs of the matching graph
# conn_comps_lst = [sorted(elt) for elt in list(nx.connected_components(matching_graph[1][0]))]
# connected_components = []
# for ordered_nodes in conn_comps_lst:
#     SG = nx.OrderedGraph()
#     nodes_to_add = []
#     for node in ordered_nodes:
#         nodes_to_add.append((node, matching_graph[1][0].nodes[node]))
#     SG.add_nodes_from(nodes_to_add)
#     SG.add_edges_from((u, v) for (u, v) in matching_graph[1][0].edges() if u in SG if v in SG)
#     connected_components.append(SG)
