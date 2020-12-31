import time
import sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

from src.parser import get_original_graphs
from src.parser import get_matching_graphs_from_folder
from src.runHelper import create_txt_files
from plot_utility import create_table, create_diagram_for_bsc, create_df_for_bsc, create_df_for_F, create_diagram_for_F, \
    create_df_for_F_2

pruning = ["pruning", "no_pruning"]
costs = [0.2, 0.3, 0.4, 0.6, 0.9, 1.6]
set_types = ["train", "validation", "test"]

# get original graphs
train_graphs, validation_graphs, test_graphs, set_of_labels = get_original_graphs()
dict = {"train": train_graphs, "test": test_graphs, "validation": validation_graphs}


for pr in pruning:
    for cost in costs:
        mg_path = "Data/vero_folder_letter/matching_graphs_{}_costs_{}".format(pr, cost)
        matching_graphs = get_matching_graphs_from_folder(mg_path)
        for set_type in set_types:
            path = "/letter_results/{}_cost_{}_dist_0.9_{}".format(pr, cost, set_type)
            create_txt_files(path, matching_graphs, dict[set_type])
            df, names_OG, names_MG = create_table(path)
            df.to_csv(path + "/isomorphism_table.csv")
            df.to_excel(path + "/isomorphism_table.xlsx")

            for cls in set_of_labels:
                subdf = create_df_for_bsc(df, names_OG, names_MG, cls)
                df.to_csv(path + "/diagrams/Mgs_" + cls + ".csv")
                df.to_excel(path + "/diagrams/Mgs_" + cls + ".xlsx")
                create_diagram_for_bsc(subdf, cls, path)  # get saved in folder

                subdf2 = create_df_for_F(df, names_OG, names_MG, cls, set_of_labels)
                df.to_csv(path + "/diagrams_for_F/Mgs_Class_" + cls + ".csv")
                df.to_excel(path + "/diagrams_for_F/Mgs_Class_" + cls + ".xlsx")
                create_diagram_for_F(subdf2, cls, path)  # get saved in folder

            create_df_for_F_2(df, orig_names=names_OG, mg_names=names_MG, set_of_classes=set_of_labels, path=path)  # gets saved in folder
