import os

import networkx as nx
import glob
import re


# argument: (relative) path of directory as a string
# returns the absolute path
def create_abs_path(string):
    rel_path = string
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    abs_path = BASE_DIR + "/" + rel_path
    abs_path = abs_path.replace("\\", "/")

    return abs_path


# argument: (absolute) path of directory as a string WHERE for each file the path must look like .../label/name.graphml
# returns a list of graphs with the following information for each graph: [graph object itself, name, label]
def read_graphs_from_folder_structure(string):
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


# argument: (absolute) path of directory as string, graphs and cxl files have to be in the same folder
# returns a list of graphs  with the following information for each graph: [graph object itself, name, label]
def read_graphs_with_cxl(string):
    path = string
    list_of_graphs = []
    list_of_files = glob.glob(path + "/*.graphml")

    for file_name in list_of_files:
        graph_information = [0, 0, 0]

        split_path = re.split(r'[/\\]', file_name)
        graph_name = split_path[-1][:-8]

        graph_information[0] = nx.read_graphml(file_name)
        graph_information[1] = graph_name

        name_n_labels = read_cxl_files()

        for x in range(len(name_n_labels)):
            split_info = re.split(r'["]', name_n_labels[x])
            name_cxl = split_info[1][:-8]
            label_cxl = split_info[3]
            if graph_name == name_cxl:
                graph_information[2] = label_cxl

        list_of_graphs.append(graph_information)

    return list_of_graphs


# reads exactly those 3 cxl files...
def read_cxl_files():
    name_n_labels = []

    abs_path = create_abs_path("Data/vero_folder/mutagenicity/graphmlFiles")
    file1 = abs_path + "/test.cxl"
    file2 = abs_path + "/validation.cxl"
    file3 = abs_path + "/train.cxl"
    files = [file1, file2, file3]

    for file in files:
        with open(file, 'r') as f:
            part = f.readlines()
            for x in range(3):
                part.remove(part[0])
            for x in range(2):
                part.remove(part[-1])
        name_n_labels = name_n_labels + part

    return name_n_labels
