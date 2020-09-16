import networkx as nx
import glob


# argument: path of directory as a string
# returns a list of graphs
def read_graphs_from_folder(string):
    path = string
    list_of_graphs = []
    list_of_files = glob.glob(path + "/*.graphml")

    for file_name in list_of_files:
        list_of_graphs.append(nx.read_graphml(file_name))

    return list_of_graphs
