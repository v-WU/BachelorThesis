import time
import networkx as nx
import random
import numpy

from src.parser import read_graphs_from_folder_structure
from src.parser import read_graphs_with_cxl

from ullmanAlgorithm import UllmanAlgorithm

random.seed(246)  # or any integer

numpy.random.seed(4812)

start_time = time.time()

original_graphs, set_of_labels = read_graphs_with_cxl("Data/vero_folder/mutagenicity/graphmlFiles")

no_pruning_graphs = read_graphs_from_folder_structure(
    "Data/vero_folder/matching_graphs_no_pruning/graphml_files/mutagen")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder/matching_graphs_no_pruning/graphml_files/nonmutagen")

pruning_graphs = read_graphs_from_folder_structure("Data/vero_folder/matching_graphs_pruning/graphml_files/mutagen")
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder/matching_graphs_pruning/graphml_files/nonmutagen")

print("Time taken to scan all the graphs = " + str(time.time() - start_time))
ullman_time = time.time()

for i in range(1):
    print("Matching graph: " + str(no_pruning_graphs[i][1]) + ", " + str(no_pruning_graphs[i][2]))

    # creates a list with all the (unconnected) subgraphs of the matching graph
    conn_comps_lst = [sorted(elt) for elt in list(nx.connected_components(no_pruning_graphs[i][0]))]
    connected_components = []
    for ordered_nodes in conn_comps_lst:
        SG = nx.OrderedGraph()
        nodes_to_add = []
        for node in ordered_nodes:
            nodes_to_add.append((node, no_pruning_graphs[i][0].nodes[node]))
        SG.add_nodes_from(nodes_to_add)
        SG.add_edges_from((u, v) for (u, v) in no_pruning_graphs[i][0].edges() if u in SG if v in SG)
        connected_components.append(SG)

    print("Number of components in matching graph: " + str(len(connected_components)))

    for graph in original_graphs:
        iso_counter = 0
        counter = 0
        # ullman1 = UllmanAlgorithm()
        # ullman1.perform_ullman_algorithm(no_pruning_graphs[i][0], graph[0], [])
        # entire_iso = ullman1.isomorphism
        for component in connected_components:
            counter = counter + 1
            ullman = UllmanAlgorithm()
            ullman.perform_ullman_algorithm(component, graph[0], [])
            if ullman.isomorphism:
                iso_counter = iso_counter + 1
        print("Original graph: " + str(graph[1]) + ", " + str(graph[2]) + ". Result: " + str(iso_counter) + " / " + str(
            counter) + " parts found.")  # Entire Matching Graph: " + str(entire_iso))

print("Time to perform Ullman = " + str(time.time() - ullman_time))
