import networkx as nx

class MatchingGraph:
    def __init__(self, graph, label):
        self.graph = graph
        self.label = label

    def getLabel(self):
        return self.label
