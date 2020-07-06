import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G = nx.read_graphml("C:/Users/zhaox/Desktop/0_2328molecule_3059_matching_graph.graphml")

nx.draw(G)
plt.show()




