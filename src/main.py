from src.parser import read_graphs_from_folder_structure
from src.parser import read_graphs_with_cxl

original_graphs = read_graphs_with_cxl("Data/vero_folder/mutagenicity/graphmlFiles")

no_pruning_graphs = read_graphs_from_folder_structure(
    "Data/vero_folder/matching_graphs_no_pruning/graphml_files/mutagen")
no_pruning_graphs = no_pruning_graphs + read_graphs_from_folder_structure(
    "Data/vero_folder/matching_graphs_no_pruning/graphml_files/nonmutagen")

pruning_graphs = read_graphs_from_folder_structure(("Data/vero_folder/matching_graphs_pruning/graphml_files/mutagen"))
pruning_graphs = pruning_graphs + read_graphs_from_folder_structure(
    ("Data/vero_folder/matching_graphs_pruning/graphml_files/nonmutagen"))
