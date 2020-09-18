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

        mega_list = read_cxl_files()

        for x in range(len(mega_list)):
            if graph_name in mega_list[x]:
                if "non" in mega_list[x]:
                    graph_label = "nonmutagen"
                    graph_information[2] = graph_label
                else:
                    graph_label = "mutagen"
                    graph_information[2] = graph_label

        list_of_graphs.append(graph_information)

    return list_of_graphs


# don't look at this...
def read_cxl_files():
    with open(r'C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/vero_folder/mutagenicity/graphmlFiles/train.cxl',
              'r') as f:
        thingy1 = f.readlines()
        thingy1.remove(thingy1[0])
        thingy1.remove(thingy1[0])
        thingy1.remove(thingy1[0])
        thingy1.remove(thingy1[-1])
        thingy1.remove(thingy1[-1])

    with open(r'C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/vero_folder/mutagenicity/graphmlFiles/test.cxl',
              'r') as f:
        thingy2 = f.readlines()
        thingy2.remove(thingy2[0])
        thingy2.remove(thingy2[0])
        thingy2.remove(thingy2[0])
        thingy2.remove(thingy2[-1])
        thingy2.remove(thingy2[-1])

    with open(
            r'C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/vero_folder/mutagenicity/graphmlFiles/validation.cxl',
            'r') as f:
        thingy3 = f.readlines()
        thingy3.remove(thingy3[0])
        thingy3.remove(thingy3[0])
        thingy3.remove(thingy3[0])
        thingy3.remove(thingy3[-1])
        thingy3.remove(thingy3[-1])

    name_n_labels = thingy1 + thingy2 + thingy3

    return name_n_labels
