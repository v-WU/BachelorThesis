import unittest
import pandas as pd

from src.plot_utility import create_matrix
from src.plot_utility import create_table


class MyTestCase(unittest.TestCase):
    def test_create_matrix(self):
        M = create_matrix("letter_results/pruning_cost_1.6_dist_0.9_train")
        assert len(M) == 1200

    def test_create_table(self):
        df = create_table("letter_results/pruning_cost_1.6_dist_0.9_train")
        assert len(df) == 1200  # number of MG
        assert len(df.columns) == 750  # number of OG in train set

    def test_create_histogram(self):
        # import MG A dataframe
        # C:/Users/zhaox/PycharmProjects/BachelorThesis/letter_results/pruning_cost_1.6_dist_0.9_train/
        df = pd.read_csv("C:/Users/zhaox/PycharmProjects/BachelorThesis/letter_results/pruning_cost_1.6_dist_0"
                           ".9_train/MG_A_end_df.csv")
        print(df)
        assert True
