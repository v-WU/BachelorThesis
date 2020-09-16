import networkx as nx
import glob
import re


# argument: (absolute) path of directory as a string WHERE for each file the path must look like .../label/name.graphml
# returns a list of graphs with the following information for each graph: [graph object itself, name, label]
def read_graphs_from_folder(string):
    path = string
    list_of_graphs = []
    list_of_files = glob.glob(path + "/*.graphml")

    for file_name in list_of_files:
        graph_information = [0, 0, 0]

        split_path = re.split(r'[/\\]', file_name)
        graph_name = split_path[-1][:-8]
        graph_label = split_path[-2]

        graph_information[0] = nx.read_graphml(file_name)
        graph_information[1] = graph_name
        graph_information[2] = graph_label

        list_of_graphs.append(graph_information)

    return list_of_graphs
