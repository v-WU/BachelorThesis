from src.parser import read_graphs_from_folder

list = read_graphs_from_folder("C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/vero_folder/matching_graphs_no_pruning/graphml_files/mutagen")
print(list[0:10])
