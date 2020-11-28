import unittest
import networkx as nx
from src.parser import read_graphs_from_folder_structure, create_abs_path, create_cxl_files
from src.parser import read_cxl
from src.parser import read_cxl_files
from src.parser import read_graphs_with_cxl_all_sets
from src.parser import read_graphs_with_cxl
from src.parser import get_iso_results
from src.parser import read_txt_file


# some tests may fail because in src.parser create_cxl_files the path is hard coded...

class TestParser():

    def test_read_graphs_from_folder_structure(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2])
        G.add_edge(1, 2)

        my_list = read_graphs_from_folder_structure(
            "Data/graphs_for_my_testing")
        imported_graph = my_list[0][0]
        graph_name = my_list[0][1]
        graph_label = my_list[0][2]

        assert (nx.is_isomorphic(G, imported_graph))
        assert (graph_name == "simple_testing_graph")
        assert (graph_label == "graphs_for_my_testing")

    # will fail if argument in src.parser create_cxl_files has been changed
    def test_read_graphs_with_cxl_all_sets(self):
        graph_information, set_of_labels = read_graphs_with_cxl_all_sets(
            "Data/graphs_for_my_testing/original_graph_for_testing")
        assert (graph_information[0][1] == "molecule_1")
        assert (graph_information[0][2] == "mutagen")
        assert (graph_information[1][1] == "molecule_2747")
        assert (graph_information[1][2] == "nonmutagen")
        assert ('mutagen' in set_of_labels)
        assert ('nonmutagen' in set_of_labels)

    # only tests if the number of graphs is correct
    def test_read_cxl_files(self):
        name_n_labels = read_cxl_files("/test.cxl", "/validation.cxl", "/train.cxl")
        assert (str(len(name_n_labels) == "4337"))

    # tests only the first entry/graph and if the number of graphs is correct
    def test_read_cxl(self):
        abs_path = create_abs_path("Data/vero_folder/mutagenicity/graphmlFiles")
        file = abs_path + "/test.cxl"
        name_n_label = []

        name_n_label = read_cxl(file, name_n_label)

        assert ("molecule_1.graphml" in name_n_label[0])
        assert ("mutagen" in name_n_label[0])
        assert not ("nonmutagen" in name_n_label[0])

    # will fail if argument in src.parser create_cxl_files has been changed
    def test_create_cxl_files(self):
        files = []
        create_cxl_files("/test.cxl", files)
        assert (files[0] == create_abs_path("Data/vero_folder/mutagenicity/graphmlFiles/test.cxl"))

    # will fail if argument in src.parser create_cxl_files has been changed
    def test_read_graphs_with_cxl(self):
        graph_information, set_of_labels = read_graphs_with_cxl("Data/graphs_for_my_testing/original_graph_for_testing",
                                                                "/test.cxl")
        assert (graph_information[0][1] == "molecule_1")
        assert (graph_information[0][2] == "mutagen")

    def test_get_iso_results(self):
        path = create_abs_path("letter_results/pruning_cost_1.6_dist_0.9_train/0_17LP1_0045_matching_graph.txt")
        values = get_iso_results(path)

        # only checking the first few entries
        assert values[0] == 0
        assert values[1] == 1
        assert values[2] == 0
        assert values[3] == 0
        assert values[4] == 0

    def test_read_txt_file(self):
        path = create_abs_path("letter_results/pruning_cost_1.6_dist_0.9_train/0_17LP1_0045_matching_graph.txt")
        mg, og, result = read_txt_file(path)

        assert mg == "0_17LP1_0045_matching_graph"
        assert og[0] == "AP1_0000"
        assert og[1] == "AP1_0001"
        assert og[2] == "AP1_0002"
        assert len(og) == 750
        assert result[0] == 0
        assert result[1] == 1
        assert result[2] == 0
