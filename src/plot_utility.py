import pandas as pd
import glob
import numpy as np

from src.parser import get_iso_results
from src.parser import create_abs_path
from src.parser import read_txt_file


def create_matrix(string):
    """
    careful! you don't know the order of the MG! The OG are sorted by name.
    :param string: (relative) path of dictionary
    :return: Matrix with 0 and 1
    """
    M = []
    path = create_abs_path(string)
    list_of_files = glob.glob(path + "/*.txt")  # abs path of all txt files in the folder

    # sort files by class
    list_of_files = sorted(list_of_files, key=last_27chars)

    for file in list_of_files:
        value = get_iso_results(file)
        M.append(value)
    M = np.array(M)  # row: OG, columns: MG
    return M


def last_27chars(string):
    return string[-27:]


def create_table(string):
    path = create_abs_path(string)
    list_of_files = glob.glob(path + "/*.txt")  # abs path of all txt files in the folder

    # sort files by class
    list_of_files = sorted(list_of_files, key=last_27chars)

    names_MG = []  # array
    names_OG = []  # array
    overall_data = []  # nd array

    for file in list_of_files:
        matching_graph, original_graphs, data = read_txt_file(file)
        names_MG.append(matching_graph)
        if len(names_OG) == 0:
            names_OG = original_graphs
        overall_data.append(data)

    overall_data = np.array(overall_data)

    df = pd.DataFrame(data=overall_data, index=names_MG, columns=names_OG)
    return df
