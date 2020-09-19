import unittest
import networkx as nx
from src.parser import read_graphs_from_folder_structure
from src.parser import create_abs_path
from src.parser import read_cxl_files
from src.parser import read_graphs_with_cxl


class TestParser(unittest.TestCase):

    # change the String in assert() to the correct path on YOUR device
    def test_create_abs_path(self):
        rel_path = "Data/graphs_for_my_testing"
        abs_path = create_abs_path(rel_path)

        assert (abs_path == "C:/Users/zhaox/PycharmProjects/BachelorThesis/Data/graphs_for_my_testing")

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

    def test_read_graphs_with_cxl(self):
        graph_information = read_graphs_with_cxl(
            "Data/graphs_for_my_testing/original_graph_for_testing")
        assert (graph_information[0][1] == "molecule_1")
        assert (graph_information[0][2] == "mutagen")

    # tests only the first entry/graph and if the number of graphs is correct
    def test_read_cxl_files(self):
        assert ("molecule_1.graphml" in read_cxl_files()[0])
        assert ("mutagen" in read_cxl_files()[0])
        self.assertFalse("nonmutagen" in read_cxl_files()[0])

        assert (str(len(read_cxl_files())) == "4337")


if __name__ == '__main__':
    unittest.main()
