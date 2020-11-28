import pandas as pd

from src.plot_utility import create_matrix
from src.parser import create_abs_path
from src.parser import read_txt_file
from src.plot_utility import create_table

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
path = create_abs_path("letter_results/pruning_cost_1.6_dist_0.9_train")  # change data set
filepath = path + "/isomorphism_table.xlsx"
df, columns = create_table("letter_results/pruning_cost_1.6_dist_0.9_train")  # change data set
df.to_excel(filepath)
