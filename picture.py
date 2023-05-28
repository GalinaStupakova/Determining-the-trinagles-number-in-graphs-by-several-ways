import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
nodes = [1, 2, 3, 4, 5]
edges = [(2, 4), (2, 5), (4, 5)]

# добавляем информацию в объект графа
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# рисуем граф и отображаем его
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()