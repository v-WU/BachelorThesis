import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)

G.add_nodes_from([2, 3])

G.add_edge(1, 2)

G.add_edges_from([(1, 3), (2, 3)])

print("Number of edges: " + str(G.number_of_edges()))

x = list(G.nodes)

print("List of nodes: " + str(x))

y = list(G.adj[1])

print("Neighbors of node 1: " + str(y))

nx.draw(G)
plt.show()

# Pfad zum ausprobieren: "C:/Users/zhaox/PycharmProjects/Data/vero_folder/mutagenicity/graphmlFiles"
