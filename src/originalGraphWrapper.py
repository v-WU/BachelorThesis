import networkx as nx


class OriginalGraph:
    def __init__(self, graph, label):
        self._graph = graph
        self.label = label

    def get_label(self):
        return self.label
