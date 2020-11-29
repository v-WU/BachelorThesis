import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

from src.plot_utility import create_matrix
from src.parser import create_abs_path
from src.parser import read_txt_file
from src.plot_utility import create_table
import re

list_of_classes = ["A","E","F","H","I","K","L","M","N","T","V","W","X","Y","Z"]


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

path = create_abs_path("letter_results/pruning_cost_1.6_dist_0.9_train")

df, orig_names, mg_names = create_table("letter_results/pruning_cost_1.6_dist_0.9_train")
# Split dataframe into subparts



for class_nam in list_of_classes:
    filtered_by_a = filter_original_graph_list_by_class(orig_names, class_nam)
    filtered_mg_by_a = filter_matching_graph_list_by_class(mg_names, class_nam)

    # test = df.loc[['21_63AP1_0007_matching_graph', '23_138AP1_0007_matching_graph']]
    sub_df = get_subset_rows_df(df,filtered_mg_by_a)
    sub_class_df = get_subset_columns_df(sub_df,filtered_by_a)

    sub_class_rest_df = get_subset_columns_df(sub_df, set(orig_names)-set(filtered_by_a))

    # ToDO: Count_things (sub_class_df)
    # ToDo: count_things (rest)

    # sub_df.to_csv(path+ "/letter_{}_dataframe.csv".format(class_nam))
# change data set
# df.hist()

