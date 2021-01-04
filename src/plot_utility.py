import glob
import numpy as np
import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy.ma as ma

from src.parser import get_iso_results
from src.parser import create_abs_path
from src.parser import read_txt_file

list_of_classes = ["A", "E", "F", "H", "I", "K", "L", "M", "N", "T", "V", "W", "X", "Y", "Z"]


def create_matrix(string):
    """
    careful! you don't know the order of the MG in the resulting  matrix! The OG are sorted by name.
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
    """
    :param string: (relative) path of directory
    :return: dataframe, names of original graphs, names of matching graphs
    """
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
    # df.to_csv(path + "/isomorphism_table.csv")

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
        if parsed_line is None:
            parsed_line = re.search('(\d+_)([a-zA-Z])(.*)', graph_name)
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


def count_occurences_in_row(df):
    """

    :param df: dataframe in which we want to count the occurences of MG
    :return: dataframe with col = MG names, row = #occurences
    """
    occurences = []
    occurences = df.apply(lambda row: sum(row == 1), axis=1)
    occurences.to_frame()
    return occurences


def count_occurences_in_columns(df):
    """

    :param df: dataframe in which we want to count the occurences of OG
    :return: dataframe with col = MG names, row = #occurences
    """
    occurences = []
    occurences = df.apply(np.sum, axis=0)
    occurences.to_frame()
    return occurences


def create_diagram_for_bsc(df, letter, path):
    """

    :param path: (relative) path of folder where the txt files and the df was stored --> path += "/diagrams
    :param letter: string e.g. "A" (needed for the diagram title)
    :param df: dataframe with rows = names of MG, columns(2) = #occur in correct class, #occur in other classes
    :return:
    """
    path = create_abs_path(path)
    path += "/diagrams"

    x = df.to_numpy()
    occur_same_class = []
    occur_diff_class = []
    number_of_rows = len(df.index)
    for i in range(number_of_rows):
        occur_same_class.append(x[i][1])

    for i in range(number_of_rows):
        occur_diff_class.append(x[i][2])

    # sort both arrays (high numbers first)
    sorted_occur_same_class = np.sort(occur_same_class)  # lowest first
    sorted_occur_diff_class = np.sort(occur_diff_class)  # lowest first
    sorted_occur_same_class = np.flip(sorted_occur_same_class)  # highest first
    sorted_occur_diff_class = np.flip(sorted_occur_diff_class)  # highest first

    # creating plot
    x1 = x2 = np.arange(number_of_rows)  # makes 80 'bins' on the x-axis
    y1 = sorted_occur_same_class
    y2 = sorted_occur_diff_class

    # create masks
    mask1 = ma.where(y1 >= y2)
    mask2 = ma.where(y2 >= y1)

    fig, ax = plt.subplots()
    p1 = ax.bar(x1[mask1], y1[mask1], color='darkorange')
    p2 = ax.bar(x2, y2, color='steelblue')
    p3 = ax.bar(x1[mask2], y1[mask2], color='darkorange')

    ax.set_title('Matching Graphs of Class ' + letter)
    ax.set_ylabel('Number of Occurrences')
    ax.set_xlabel('Matching Graphs')
    ax.legend()
    if len(p1.patches) == 0:
        plt.legend((p2, p3), ('same', 'different'))
    else:
        plt.legend((p1, p2), ('different', 'same'))

    fig.tight_layout()
    fig.savefig(path + "/MG_class_" + letter + ".jpg")
    # plt.show()

    plt.cla()
    plt.clf()
    plt.close()

    return


def create_df_for_bsc(df, orig_names, mg_names, letter):
    """
    :param df: dataframe with all the data
    :param orig_names: list of original graph names
    :param mg_names: list of matching graph names
    :param letter: letter class as a string e.g. "A"
    :return: dataframe with occurences for the same class and occurences for the other classes (all in 1)
    """
    names_filtered_by_og = filter_original_graph_list_by_class(orig_names, letter)
    names_filtered_by_mg = filter_matching_graph_list_by_class(mg_names, letter)

    # create necessary subdataframes
    df_mg = get_subset_rows_df(df, names_filtered_by_mg)  # MG from 1 class with OG from all classes
    df_mg_og = get_subset_columns_df(df_mg, set(orig_names) - set(
        names_filtered_by_og))  # MG from 1 class with OG from 1 (same) class
    df_mg_og_rest = get_subset_columns_df(df_mg, set(orig_names) - (
            set(orig_names) - set(names_filtered_by_og)))  # MG from 1 class with OG from 14 (other) classes

    # count occurences in the subdataframes
    occur_df_mg_og = count_occurences_in_row(df_mg_og)
    occur_df_mg_og_rest = count_occurences_in_row(df_mg_og_rest)

    # create end dataframe with the occurences
    end_df = pd.concat([occur_df_mg_og, occur_df_mg_og_rest], axis=1)
    end_df.rename(columns={0: 'same class', 1: 'different classes'}, inplace=True)

    return end_df


def create_diagram_for_F(df, letter, path):
    """

    :param df: colums = MGs A, index = A, E, F, ...
    :param letter:
    :param path: (relative) path of folder where the txt and csv files are --> path += "/diagrams_for_F
    :return:
    """

    path = create_abs_path(path)
    path += "/diagrams_for_F"

    # df2 = pd.DataFrame({'OG': ['A', 'E', 'F'], 'Occurrences': [10, 5, 5]})
    # ax = df2.plot.bar(x='OG', y='Occurrences', rot=0)

    ax = df.plot.bar(rot=0)
    ax.set_xlabel('Original Graph Classes')
    ax.set_title('Occurrences of MGs Class ' + letter)

    # plt.show()
    ax.figure.savefig(path + "/MGs_class_" + letter + ".jpg")
    plt.clf()
    plt.close()
    return


def create_df_for_F(df, orig_names, mg_names, letter, set_of_classes):
    """
    :param set_of_classes: all original classes A, F, E, ..., Z
    :param df: dataframe with all the data
    :param orig_names: list of original graph names
    :param mg_names: list of matching graph names
    :param letter: letter class as a string e.g. "A"
    :return: dataframe with MGs from 1 class in all OG classes. Index = A, E, F, ... , Z. Columns = e.g. MGs A.
    """
    names_filtered_by_mg = filter_matching_graph_list_by_class(mg_names, letter)

    data = []

    for cl in set_of_classes:
        names_filtered_by_og = filter_original_graph_list_by_class(orig_names, cl)
        subdf1 = create_subpart_df(df, names_filtered_by_og,
                                   names_filtered_by_mg)  # subdf with MGs from 'letter' and OGs from 1 class
        subdf2 = count_occurences_in_row(subdf1)  # subdf with occurrences per MG in 1 whole OG class
        occur = []
        len_of_subdf2 = len(subdf2)
        for i in range(len_of_subdf2):
            occur.append(subdf2[i])
        Sum = sum(occur)  # total sum of MG from class letter appearing in OG from class cl
        data.append(Sum)

    end_df = pd.DataFrame(data, columns=['MGs ' + letter], index=set_of_classes)

    return end_df


def create_df_for_F_2(df, orig_names, mg_names, set_of_classes, path):
    """

    :param df:
    :param orig_names:
    :param mg_names:
    :param set_of_classes:
    :return: dataframe with index=Original Graphs, columns=classes of MG's
    """
    path = create_abs_path(path)
    path += "/diagrams_for_F"

    parts = []  # dataframes with same index that need to be concat() in the end

    for cl in set_of_classes:
        names_filtered_by_mg = filter_matching_graph_list_by_class(mg_names, cl)
        subdf1 = create_subpart_df(df, orig_names, names_filtered_by_mg)
        var = subdf1.T
        subdf2 = count_occurences_in_row(var)
        subdf2.index = orig_names
        subdf2.columns = ['MGs ' + cl]
        parts.append(subdf2)

    # print(parts)

    end_df = pd.concat(parts, axis=1)
    end_df.columns = set_of_classes
    # print(end_df)

    end_df.to_csv(path + "/original_graph_table.csv")
    end_df.to_excel(path + "/original_graph_table.xlsx")

    return end_df
