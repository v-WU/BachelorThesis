from src.parser import read_graphs_from_folder_structure
from src.parser import create_abs_path
from src.parser import read_cxl_files
from src.parser import read_graphs_with_cxl

#
# abs_path = create_abs_path("Data/vero_folder/matching_graphs_no_pruning/graphml_files/mutagen")
# list1 = read_graphs_from_folder_structure(abs_path)
# print(list1[0:2])
#
# list2 = read_graphs_from_folder_structure("C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/vero_folder/matching_graphs_no_pruning/graphml_files/mutagen")
# print(list2[0:2])

print(read_graphs_with_cxl("C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/vero_folder/mutagenicity/graphmlFiles")[2720])

#print(read_cxl_files()[0])
# output: <print file="molecule_1.graphml" class="mutagen"/>
