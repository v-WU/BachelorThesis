import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from matplotlib.ticker import StrMethodFormatter

from src.plot_utility import create_matrix
from src.parser import create_abs_path
from src.parser import read_txt_file
from src.plot_utility import create_table

list_of_classes = ["A", "E", "F", "H", "I", "K", "L", "M", "N", "T", "V", "W", "X", "Y", "Z"]


def filter_original_graph_list_by_class(graph_name_list, class_name):
    filtered_list = [name for name in graph_name_list if name.startswith(class_name)]

    return filtered_list


def filter_matching_graph_list_by_class(graph_name_list, class_name):
    filtered_list = []

    for graph_name in graph_name_list:
        parsed_line = re.search('(\d+_\d+)([a-zA-Z])(.*)', graph_name)
        cl_nam = parsed_line.group(2)
        if cl_nam == class_name:
            filtered_list.append(graph_name)

    return filtered_list


# create the isomorphism matrix into an existing excel file
# M = create_matrix("letter_results/pruning_cost_1.6_dist_0.9_train")  # change data set
# df = pd.DataFrame(M)
#
# path = create_abs_path("letter_results/pruning_cost_1.6_dist_0.9_train")  # change data set
# filepath = path + "/isomorphism_matrix.xlsx"
#
# df.to_excel(filepath, index=False)


# create dataframe for 1 MG (table, not matrix)
# path = create_abs_path("letter_results/pruning_cost_1.6_dist_0.9_train/0_54AP1_0037_matching_graph.txt")
# name_mg, columns, data = read_txt_file(path)
# index = []
# index.append(name_mg)
# df = pd.DataFrame(data=data, index=columns, columns=index)
# df = df.transpose()
# print(df)

# store table (data frame) into an existing excel file
# path = create_abs_path("letter_results/pruning_cost_1.6_dist_0.9_train")  # change data set
# filepath = path + "/isomorphism_table.xlsx"
# df = create_table("letter_results/pruning_cost_1.6_dist_0.9_train")  # change data set
# df.to_excel(filepath)

def get_subset_columns_df(dataframe, col_names):
    return dataframe[col_names]


def get_subset_rows_df(dataframe, row_names):
    return dataframe.loc[row_names]


def count_occur_in_corr_class(df):
    corr_class = []
    corr_class = df.apply(lambda row: sum(row == 1), axis=1)
    corr_class.to_frame(name="same class")
    return corr_class


def count_occur_in_rest_class(df):
    rest_class = []
    rest_class = df.apply(lambda row: sum(row == 1), axis=1)
    rest_class.to_frame()
    return rest_class


path = create_abs_path("letter_results/pruning_cost_1.6_dist_0.9_train")

df, orig_names, mg_names = create_table("letter_results/pruning_cost_1.6_dist_0.9_train")
df.to_csv("C:/Users/zhaox/PycharmProjects/BachelorThesis/letter_results/pruning_cost_1.6_dist_0.9_train/isomorphism_table.csv")

# Split dataframe into subparts
# for class_nam in list_of_classes:
#     filtered_og_by_class = filter_original_graph_list_by_class(orig_names, class_nam)
#     filtered_mg_by_class = filter_matching_graph_list_by_class(mg_names, class_nam)
#
#     # test = df.loc[['21_63AP1_0007_matching_graph', '23_138AP1_0007_matching_graph']]
#     sub_df = get_subset_rows_df(df, filtered_mg_by_class)
#     sub_class_df = get_subset_columns_df(sub_df, filtered_og_by_class)
#
#     sub_class_rest_df = get_subset_columns_df(sub_df, set(orig_names) - set(filtered_og_by_class)) #left with og others
#
#     # ToDO: Count_things (sub_class_df)
#     # ToDo: count_things (rest)

#      sub_df.to_csv(path+ "/letter_{}_dataframe.csv".format(class_nam))

# split dataframe into subparts from class A

# filtered_og_by_A = filter_original_graph_list_by_class(orig_names, "A")
# filtered_mg_by_A = filter_matching_graph_list_by_class(mg_names, "A")
#
# df_mg_a = get_subset_rows_df(df, filtered_mg_by_A)
# # # print(df_mg_a)
# #
# df_mg_a_og_a = get_subset_columns_df(df_mg_a, set(orig_names) - (set(orig_names) - set(filtered_og_by_A))) #left with og A
# # print("Data frame mg a, og a: " + str(df_mg_a_og_a))
# #
# df_mg_a_og_rest = get_subset_columns_df(df_mg_a, set(orig_names) - set(filtered_og_by_A)) #left with og others
# # # print(df_mg_a_og_rest)
# #
# new_df = count_occur_in_corr_class(df_mg_a_og_a)
# # # print(new_df)
# #
# new_df_2 = count_occur_in_rest_class(df_mg_a_og_rest)
# # # print(new_df_2)
# #
# end_df = pd.concat([new_df, new_df_2], axis=1)
# end_df.rename(columns={0: 'same class', 1: 'different classes'}, inplace=True)
# print("end data frame: " + str(end_df))
# end_df.to_csv("C:/Users/zhaox/PycharmProjects/BachelorThesis/letter_results/pruning_cost_1.6_dist_0.9_train/MG_A_end_df.csv")
