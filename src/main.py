import time
import sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

from src.parser import get_original_graphs, create_abs_path
from src.parser import get_matching_graphs_from_folder
from src.runHelper import create_txt_files
from plot_utility import create_table, create_diagram_for_bsc, create_df_for_bsc, create_df_for_F, create_diagram_for_F, \
    create_df_for_F_2


# TODO delete all bsc .jpg and redo the bsc diagrams

# TODO for no_pruning_cost_1.6_dist_0.9 all sets
pruning = ["no_pruning"]
costs = [1.6]
# pruning = ["pruning", "no_pruning"]
# costs = [0.2, 0.3, 0.4, 0.6, 0.9, 1.6]
set_types = ["train", "validation", "test"]

# get original graphs
train_graphs, validation_graphs, test_graphs,_ = get_original_graphs()
set_of_labels = ["A", "E", "F", "H", "I", "K", "L", "M", "N", "T", "V", "W", "X", "Y", "Z"]

dict = {"train": train_graphs, "test": test_graphs, "validation": validation_graphs}

for pr in pruning:
    for cost in costs:
        mg_path = "Data/vero_folder_letter/matching_graphs_{}_costs_{}".format(pr, cost)
        matching_graphs = get_matching_graphs_from_folder(mg_path)
        matching_graphs = matching_graphs[:5]
        for set_type in set_types:
            path = "letter_results/{}_cost_{}_dist_0.9_{}".format(pr, cost, set_type)
            create_txt_files(path, matching_graphs, dict[set_type])  # comment when doing only the bsc diagrams
            df, names_OG, names_MG = create_table(path)
            path2 = create_abs_path(path)
            df.to_csv(path2 + "/isomorphism_table.csv")  # comment when doing only the bsc diagrams
            df.to_excel(path2 + "/isomorphism_table.xlsx")  # comment when doing only the bsc diagrams

            for cls in set_of_labels:
                subdf = create_df_for_bsc(df, names_OG, names_MG, cls)  # comment when doing only the bsc diagrams
                subdf.to_csv(path2 + "/diagrams/Mgs_" + cls + ".csv")  # comment when doing only the bsc diagrams
                subdf.to_excel(path2 + "/diagrams/Mgs_" + cls + ".xlsx")  # comment when doing only the bsc diagrams
                test = pd.read_csv(path2 + "/diagrams/Mgs_" + cls + ".csv")
                create_diagram_for_bsc(test, cls, path)  # get saved in folder

                # comment when doing only the bsc diagrams
                subdf2 = create_df_for_F(df, names_OG, names_MG, cls, set_of_labels)
                subdf2.to_csv(path2 + "/diagrams_for_F/Mgs_Class_" + cls + ".csv")
                subdf2.to_excel(path2 + "/diagrams_for_F/Mgs_Class_" + cls + ".xlsx")
                create_diagram_for_F(subdf2, cls, path)  # get saved in folder

            # comment when doing only the bsc diagrams
            create_df_for_F_2(df, orig_names=names_OG, mg_names=names_MG, set_of_classes=set_of_labels, path=path)  # gets saved in folder
