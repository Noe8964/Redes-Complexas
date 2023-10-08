import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
pos = nx.spring_layout(G, iterations=15, seed=1721)
fig, ax = plt.subplots(figsize=(15, 9))
ax.axis("off")
nx.draw_networkx(G, pos=pos, ax=ax)
plt.show()