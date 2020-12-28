import os

import networkx as nx
import glob
import re
import numpy as np

list_of_classes = ["A", "E", "F", "H", "I", "K", "L", "M", "N", "T", "V", "W", "X", "Y", "Z"]

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


def get_iso_results(string):
    """
    This function does not retrieve the names of the graphs!
    :param string: (abs) path of file
    :return: array with 0, 1 corresponding to not-iso resp. iso
    """
    values = []

    with open(string, "r") as file:
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


def read_txt_file(string):
    '''

    :param string: (absolute) path of file
    :return: (1) name of matching graph, (2) array with names of the original graphs, (3) array with 0 and 1
    '''
    name_matching = ""
    name_orginal = []
    data = []

    with open(string, "r") as file:
        first_line = file.readline()
        chunks = first_line.split(", ")
        chunky_chunks = chunks[0].split("=")
        name_matching = chunky_chunks[1].strip("'")

    with open(string, "r") as f:
        for line in f:
            word_list = line.split(",")
            # print(word_list)
            wordy_word_list = word_list[1].split("=")
            name_orginal.append(wordy_word_list[2].strip("'"))

    data = get_iso_results(string)
    data = np.array(data)

    return name_matching, name_orginal, data


def last_27chars(string):
    return string[-23:]


def get_original_graphs():
    """
    get all original graphs (training set, validation set, test set)
    :return: 4 arrays (train_graphs, validation_graphs, test_graphs, set_of_labels)
    """
    train_graphs, set_of_labels = read_graphs_with_cxl("Data/vero_folder_letter/letter/graphmlFiles", "/train.cxl")
    # print("number of training graphs: " + str(len(train_graphs)))  # 750

    validation_graphs, _ = read_graphs_with_cxl("Data/vero_folder_letter/letter/graphmlFiles", "/validation.cxl")
    # print("number of validation graphs: " + str(len(validation_graphs)))  # 750

    test_graphs, _ = read_graphs_with_cxl("Data/vero_folder_letter/letter/graphmlFiles", "/test.cxl")
    # print("number of test graphs: " + str(len(test_graphs)))  # 750

    return train_graphs, validation_graphs, test_graphs, set_of_labels


def get_matching_graphs_from_folder(string):
    """
    :param string: (relative) path of folder e.g. "Data/vero_folder_letter/matching_graphs_no_pruning_costs_0.6"
    :return: array with all the matching graphs from this folder
    """
    matching_graphs = []
    list_of_folders = []

    for letter in list_of_classes:
        list_of_folders.append(string + "/graphml_files/" + letter)

    for folder in list_of_folders:
        matching_graphs = matching_graphs + read_graphs_from_folder_structure(folder)

    return matching_graphs
