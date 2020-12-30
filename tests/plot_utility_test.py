import unittest
import pandas as pd

from src.plot_utility import create_matrix, create_df_for_F
from src.plot_utility import create_table
from src.plot_utility import create_diagram_for_bsc
from src.plot_utility import create_df_for_bsc
from src.plot_utility import create_diagram_for_F


class MyTestCase(unittest.TestCase):
    def test_create_matrix(self):
        M = create_matrix("letter_results/pruning_cost_1.6_dist_0.9_train")
        assert len(M) == 1200

    def test_create_table(self):
        df, names_OG, names_MG = create_table("letter_results/pruning_cost_1.6_dist_0.9_test")
        assert len(df) == 1200  # number of MG
        assert len(df.columns) == 750  # number of OG in train set

    def test_create_diagram_for_bsc(self):
        # import MG A dataframe
        df = pd.read_csv("C:/Users/zhaox/PycharmProjects/BachelorThesis/letter_results/pruning_cost_1.6_dist_0"
                         ".9_train/MG_A_end_df.csv")
        create_diagram_for_bsc(df, "A", "letter_results/pruning_cost_1.6_dist_0.9_train")
        assert True

    def test_create_df_for_bsc(self):
        # create df containing all data
        df2, names_OG, names_MG = create_table("letter_results/pruning_cost_1.6_dist_0.9_train")
        # print("created df = \n" + str(df2))
        new_df2 = create_df_for_bsc(df2, names_OG, names_MG, "A")
        print("created subdf = \n " + str(new_df2))

        # import df containing all data
        # df = pd.read_csv("C:/Users/zhaox/PycharmProjects/BachelorThesis/letter_results/pruning_cost_1.6_dist_0"
        #                  ".9_train/isomorphism_table.csv")
        # print("imported df = \n"+str(df))
        # new_df = create_df_for_bsc(df, names_OG, names_MG, "A")
        # print("imported subdf = \n " + str(new_df))
        assert True

    def test_create_diagram_for_F(self):
        # create test dataframe
        data = {"MGs A": [10, 5, 5]}
        df = pd.DataFrame(data, index=['A', 'E', 'F'], columns=['MGs A'])
        path= "/letter_results/pruning_cost_1.6_dist_0.9_train"

        # uncomment next line to test, but check path-folder-situation
        # create_diagram_for_F(df, "A", path)
        assert True


    def test_create_df_for_F(self):
        # create df containing all data
        df2, names_OG, names_MG = create_table("letter_results/pruning_cost_1.6_dist_0.9_train")
        set_of_classes = ["A", "E", "F", "H", "I", "K", "L", "M", "N", "T", "V", "W", "X", "Y", "Z"]

        create_df_for_F(df2, names_OG, names_MG, "A", set_of_classes)

        assert True
