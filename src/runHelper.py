import sys

from ullmanAlgorithm import UllmanAlgorithm
from src.parser import create_abs_path, get_matching_graphs_from_folder


def create_txt_files(path, matchingGraphs, originalGraphSubset):
    """
    creates and fills txt files. 1 MG per file (with all OG from this subset)
    :param path: (relative) path of directory where the files should go in e.g. "letter_results/pruning_cost_1.6_dist_0.9_validation"
    :param matchingGraphs: data set (list with elements: [MG, name, label])
    :return:
    """
    data_size = len(matchingGraphs)  # 1200

    for i in range(data_size):
        name_of_file = str(matchingGraphs[i][1])
        save_path = create_abs_path(path + "/" + name_of_file)
        complete_name = save_path + ".txt"
        sys.stdout = open(complete_name, "w")

        for graph in originalGraphSubset:
            ullman = UllmanAlgorithm()
            ullman.perform_ullman_algorithm(matchingGraphs[i][0], graph[0], [])
            print(
                "matching graph='" + str(matchingGraphs[i][1]) + "', class='" + str(
                    matchingGraphs[i][2]) + "' and original graph='" + str(
                    graph[1]) + "', class='" + str(graph[2]) + "': isomorphism=" + str(
                    ullman.isomorphism))

        sys.stdout.close()

    return
