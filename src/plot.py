import pandas as pd

from src.plot_utility import create_matrix
from src.parser import create_abs_path

M = create_matrix("letter_results/pruning_cost_1.6_dist_0.9_train")
df = pd.DataFrame(M)

path = create_abs_path("letter_results/pruning_cost_1.6_dist_0.9_train")
filepath = path + "/isomorphism_matrix.xlsx"

df.to_excel(filepath, index=False)
