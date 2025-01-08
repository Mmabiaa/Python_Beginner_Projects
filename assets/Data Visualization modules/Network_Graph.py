import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from=['A', 'B', 'C', 'D', 'E']

edges = [('A', 'B'), ('A', 'C'), ('B', 'c'), ('B', 'D'), ('C', 'E')]
G.add_edges_from(edges)

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='yellow', node_size=1000,
        edge_color='gray', font_size=16, font_weight='bold')
plt.title('Network Graph Using Python')
plt.show()