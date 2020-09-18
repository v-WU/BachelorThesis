from src.parser import read_graphs_from_folder
from src.parser import create_abs_path

abs_path = create_abs_path("Data/vero_folder/matching_graphs_no_pruning/graphml_files/mutagen")
list1 = read_graphs_from_folder(abs_path)
print(list1[0:2])

list2 = read_graphs_from_folder("C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/vero_folder/matching_graphs_no_pruning/graphml_files/mutagen")
print(list2[0:2])
