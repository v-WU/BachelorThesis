import pandas as pd
import glob
import numpy as np
import re

from src.parser import get_iso_results
from src.parser import create_abs_path
from src.parser import read_txt_file

list_of_classes = ["A", "E", "F", "H", "I", "K", "L", "M", "N", "T", "V", "W", "X", "Y", "Z"]


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
    return df, names_OG, names_MG


def create_subpart_df(dataframe, orig_names, mg_names):
    """
    :param dataframe: dataframe with all matching graphs and all original graphs
    :param orig_names: list of (filtered) original graph names which should appear in the new dataframe e.g. only OG from class A
    :param mg_names: list of (filtered) matching graph names which should appear in the new dataframe e.g. only MG from class A
    :return: new dataframe with "windowed" view
    """
    df_mg = get_subset_rows_df(dataframe, mg_names)  # df with filtered MG and all OG
    df_mg_og = get_subset_columns_df(df_mg, orig_names)  # df with filtered MG and filtered OG
    return df_mg_og


def filter_original_graph_list_by_class(graph_name_list, class_name):
    """
    :param graph_name_list: names of original graphs
    :param class_name: e.g. "A"
    :return: names of original graphs from class e.g. "A"
    """
    filtered_list = [name for name in graph_name_list if name.startswith(class_name)]
    return filtered_list


def filter_matching_graph_list_by_class(graph_name_list, class_name):
    """
    :param graph_name_list: names of matching graphs
    :param class_name: e.g. "A"
    :return: names of matching graphs from class e.g. "A"
    """
    filtered_list = []

    for graph_name in graph_name_list:
        parsed_line = re.search('(\d+_\d+)([a-zA-Z])(.*)', graph_name)
        cl_nam = parsed_line.group(2)
        if cl_nam == class_name:
            filtered_list.append(graph_name)

    return filtered_list


def get_subset_columns_df(dataframe, col_names):
    """

    :param dataframe:
    :param col_names: names of OG
    :return:
    """
    return dataframe[col_names]


def get_subset_rows_df(dataframe, row_names):
    """

    :param dataframe:
    :param row_names: names of MG
    :return:
    """
    return dataframe.loc[row_names]


def count_occurences(df):
    '''

    :param df: dataframe in which we want to count the occurences
    :return: dataframe with col = MG names, row = #occurences
    '''
    occurences = []
    occurences = df.apply(lambda row: sum(row == 1), axis=1)
    occurences.to_frame()
    return occurences
