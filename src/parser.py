import os

import networkx as nx
import glob
import re


def create_abs_path(string):
    """
    :param string: (relative) path of directory
    :return: absolute path
    """
    rel_path = string
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    abs_path = BASE_DIR + "/" + rel_path
    abs_path = abs_path.replace("\\", "/")

    return abs_path


def read_graphs_from_folder_structure(string):
    """
    :param string: (relative) path of directory as a string WHERE for each file the path must look like .../label/name.graphml
    :return: a list of graphs with the following information for each graph: [graph object itself, name, label]
    """
    path = create_abs_path(string)
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


def read_graphs_with_cxl_all_sets(string):
    """
    :param string: (relative) path of directory as string, graphs and cxl files have to be in the same folder
    :return: (1) a list of graphs  with the following information for each graph: [graph object itself, name, label],
            (2) a set of the existing labels
    """
    path = create_abs_path(string)
    list_of_graphs = []
    list_of_labels = []
    list_of_files = glob.glob(path + "/*.graphml")  # all graphs in folder

    name_n_labels = read_cxl_files("/test.cxl", "/validation.cxl", "/train.cxl")

    for file_name in list_of_files:
        graph_information = [0, 0, 0]

        split_path = re.split(r'[/\\]', file_name)
        graph_name = split_path[-1][:-8]

        graph_information[0] = nx.read_graphml(file_name)
        graph_information[1] = graph_name

        for x in range(len(name_n_labels)):
            split_info = re.split(r'["]', name_n_labels[x])
            name_cxl = split_info[1][:-8]
            label_cxl = split_info[3]

            list_of_labels.append(label_cxl)

            if graph_name == name_cxl:
                graph_information[2] = label_cxl
                break

        list_of_graphs.append(graph_information)

    set_of_labels = set(list_of_labels)

    return list_of_graphs, set_of_labels


def read_cxl_files(*args):
    name_n_labels = []
    files = []

    for i in args:
        create_cxl_files(i, files)

    for file in files:
        name_n_labels = read_cxl(file, name_n_labels)

    return name_n_labels


def read_cxl(file, name_n_labels):
    with open(file, 'r') as f:
        part = f.readlines()
        for x in range(3):
            part.remove(part[0])
        for x in range(2):
            part.remove(part[-1])
    name_n_labels = name_n_labels + part
    return name_n_labels


def create_cxl_files(string, files):
    abs_path = create_abs_path("Data/vero_folder_letter/letter/graphmlFiles")
    file = abs_path + string
    files = files.append(file)
    return files


def read_graphs_with_cxl(*args):
    """
    :param args: [0] string: (relative) path of directory as string, graphs and cxl files have to be in the same folder,
    [1] cxl file e.g. "/test.cxl"
    :return:
    """
    path = create_abs_path(args[0])
    list_of_graphs = []
    list_of_labels = []
    list_of_files = glob.glob(path + "/*.graphml")  # all graphs in thr folder

    # args[1] sould be something like this: "/test.cxl", "/validation.cxl" or "/train.cxl"
    name_n_labels = read_cxl_files(args[1])

    for file_name in list_of_files:
        graph_information = [0, 0, 0]

        split_path = re.split(r'[/\\]', file_name)
        graph_name = split_path[-1][:-8]

        graph_information[0] = nx.read_graphml(file_name)
        graph_information[1] = graph_name

        for x in range(len(name_n_labels)):
            split_info = re.split(r'["]', name_n_labels[x])
            name_cxl = split_info[1][:-8]
            label_cxl = split_info[3]

            list_of_labels.append(label_cxl)

            if graph_name == name_cxl:
                graph_information[2] = label_cxl
                list_of_graphs.append(graph_information)
                break

    set_of_labels = set(list_of_labels)

    return list_of_graphs, set_of_labels


def get_iso_results(directory, name):
    """
    This function does not retrieve the names of the graphs!
    :param directory: (relative) path of directory e.g. "letter_results/pruning_cost_1.6_dist_0.9_train"
    :param name: name of txt file e.g. "/0_17LP1_0045_matching_graph.txt"
    :return: array with 0, 1 corresponding to not-iso resp. iso
    """
    values = []
    path = create_abs_path(directory)
    file_name = path + name

    with open(file_name, "r") as file:
        for line in file:
            word_list = line.split()
            isomorphism_chunk = word_list[-1]  # e.g. isomorphism=True
            words = isomorphism_chunk.split("=")
            isomorphism = words[-1]
            if isomorphism == "True":
                values.append(1)
            else:
                values.append(0)

    return values
