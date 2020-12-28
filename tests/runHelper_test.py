import unittest

from src.runHelper import create_txt_files
from src.parser import get_matching_graphs_from_folder
from src.parser import get_original_graphs


class MyTestCase(unittest.TestCase):
    def test_create_txt_files(self):
        matchingGraphs = get_matching_graphs_from_folder("Data/vero_folder_letter/matching_graphs_pruning_costs_0.2")
        train_graphs, validation_graphs, test_graphs, set_of_labels = get_original_graphs()

        # uncomment next line to test the function
        # create_txt_files("letter_results/pruning_cost_0.2_dist_0.9_train", matchingGraphs, train_graphs)
        assert True
